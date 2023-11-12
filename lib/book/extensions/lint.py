"""Check configuration."""

import argparse
from bs4 import BeautifulSoup
from collections import defaultdict
import hashlib
from pathlib import Path
import re
import shortcodes

import bin_util
import regex
import util


def main():
    """Main driver."""
    args = parse_args()
    config = bin_util.load_config(args.config)
    content = {
        "bib": util.read_bibliography(),
        "html": _collect_files(config, "html"),
        "src": _collect_files(config, "markdown"),
    }
    for name, func in globals().items():
        if name.startswith("lint_"):
            func(args, config, content)


def lint_chapters_again_keys(args, config, content):
    """Check chapters against chapter keys."""
    expected = set(bin_util.source_dirs(args.src, config))
    actual = {str(p) for p in Path(args.src).glob("*") if p.is_dir()}
    report_diff("chapter keys vs. directories", expected, actual)


def lint_bibliography_key_order(args, config, content):
    """Check bibliography file keys for ordering."""
    content = Path("info", "bibliography.bib").read_text()
    keys = list(m for m in regex.BIB_KEY.findall(content))
    previous = None
    for k in keys:
        if (previous is not None) and k <= previous:
            print(f"bibliography key {k} out of order")
        previous = k
    

def lint_duplicate_files(args, config, content):
    """Check for duplicated files."""
    source_dirs = {
        Path(d): i for (i, d) in enumerate(bin_util.source_dirs(args.src, config))
    }
    ark_data = {
        src_dir: bin_util.load_ark_data(Path(src_dir), "copied", [])
        for src_dir in source_dirs
    }
    ark_lookup = {
        src_dir: {str(Path(args.src, x)) for x in data}
        for src_dir, data in ark_data.items()
    }
    duplicates = _find_duplicate_files(source_dirs)
    for group in duplicates:
        group = sorted(group, key=lambda filename: source_dirs[filename.parent])
        for i, current in list(enumerate(group))[1:]:
            previous = str(group[i - 1])
            if previous not in ark_lookup[current.parent]:
                print(f"{current} not listed as duplicate of {previous}")
            else:
                ark_lookup[current.parent].remove(previous)
    for src_dir, values in ark_lookup.items():
        if values:
            print(
                f"{src_dir}/{bin_util.ARK_FILE} contains unused {', '.join(sorted(values))}"
            )


def lint_shortcodes(args, config, content):
    """Check shortcode usage in a single pass."""

    def _collect_b(pargs, kwargs, extra):
        util.require(
            (len(pargs) > 0) and (not kwargs),
            f"Bad 'b' shortcode with {pargs} and {kwargs} in {extra['filename']}",
        )
        extra["b"].update(pargs)

    parser = shortcodes.Parser(inherit_globals=False, ignore_unknown=True)
    parser.register(_collect_b, "b")
    collector = {"b": set()}
    for filename in content["src"]:
        collector["filename"] = filename
        try:
            parser.parse(Path(filename).read_text(), collector)
        except shortcodes.ShortcodeSyntaxError as exc:
            util.fail(f"%b shortcode parsing error in {filename}: {exc}")
    _check_bibliography(collector["b"], content["bib"])


def lint_single_h1(args, config, content):
    """Check for a single H1 in every file."""
    for filepath, doc in content["html"].items():
        num = len(doc.find_all("h1"))
        if num != 1:
            print(f"{filepath} contains {num} H1 headings")


def lint_slug_format(args, config, content):
    """Check slugs in headings, figures, and tables."""

    def _check(node, slug, kind):
        """Check format of node's ID."""
        if "id" not in node.attrs:
            print(f"{filepath} {kind} missing 'id'")
        elif not node.attrs["id"].startswith(slug):
            print(f"{filepath} {kind} slug {node.attrs['id']} badly formatted")

    for filepath, doc in content["html"].items():
        slug = filepath.parts[-2]
        for figure in doc.find_all("figure"):
            _check(figure, slug, "figure")
        for table_div in doc.find_all("div", class_="table"):
            _check(table_div, slug, "table div")
        if slug not in bin_util.get_lint(config).get("disable_h2_id", {}):
            for heading in doc.find_all("h2"):
                _check(heading, slug, "H2 heading")


def lint_unresolved_markdown_links(args, config, content):
    """Look for Markdown [text][key] links that didn't resolve."""
    pat = re.compile(r"\]\[")
    for filepath, doc in content["html"].items():
        matches = doc.find_all(string=pat)
        matches = [m for m in matches if not _in_code(m)]
        if matches:
            matches = "\n".join(f"- {m.parent.sourceline}: {m}" for m in matches)
            print(f"{filepath} contains unresolved link(s):\n{matches}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="config file")
    parser.add_argument("--src", type=str, required=True, help="source directory")
    return parser.parse_args()


def report_diff(title, expected, actual):
    """Report mis-matches."""
    if diff := expected - actual:
        print(f"{title} missing: {', '.join(sorted(diff))}")
    if diff := actual - expected:
        print(f"{title} extra: {', '.join(sorted(diff))}")


def _check_bibliography(seen, available):
    """Check that citations exists and are used."""
    exists = {entry.key for entry in available}
    report_diff("bibliography keys", seen, exists)


def _collect_files(config, which):
    """Read text of source and output files."""

    def _same(x):
        return x

    def _parse(x):
        return BeautifulSoup(x, "html.parser")

    if which == "markdown":
        root_dir = config.src_dir
        filename = "index.md"
        transform = _same
    elif which == "html":
        root_dir = config.out_dir
        filename = "index.html"
        transform = _parse
    else:
        util.fail(f"unknown file type in collector {which}")

    paths = [
        Path(root_dir, filename),
        *[Path(root_dir, slug, filename) for slug in config.chapters],
    ]
    return {p: transform(p.read_text()) for p in paths}


def _find_duplicate_files(source_dirs):
    """Group files by duplicate hashes."""
    groups = defaultdict(set)
    for src_dir in source_dirs:
        for path in src_dir.glob("*"):
            if (not path.is_file()) or (str(path).endswith("~")):
                continue
            hash_code = hashlib.sha256(path.read_bytes()).hexdigest()
            groups[hash_code].add(path)
    return [group for group in groups.values() if len(group) > 1]


def _in_code(node):
    """Is this DOM node inside a code element?"""
    return any(p.tag == "code" for p in node.parents)


if __name__ == "__main__":
    main()
