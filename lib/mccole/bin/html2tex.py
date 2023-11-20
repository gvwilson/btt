"""Convert HTML pages to LaTeX."""

import argparse
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

import util


def main():
    """Main driver."""
    args = parse_args()
    config = util.load_config(args.config)
    pages = util.collect_files(config, "html", False)
    doc = extract_contents(pages.values())
    body = "".join(do(doc, [], escape))
    head, title, foot = get_extra_tex(args.config, config)
    if args.outfile:
        save(open(args.outfile, "w"), head, title, body, foot)
    else:
        save(sys.stdout, head, title, body, foot)


def children(node, accum, escape, before=None, after=None):
    """Handle children of containing node."""
    if before is not None:
        accum.append(before)

    for child in node:
        do(child, accum, escape)

    if after is not None:
        accum.append(after)

    return accum


def citation(node, accum, escape):
    """Handle a group of citations."""
    cites = node.find_all("a")
    assert all(has_class(child, "bib-ref") for child in cites)
    keys = ",".join([c["href"].split("#")[1] for c in cites])
    accum.append(rf"\cite{{{keys}}}")


def do(node, accum, escape):
    """Dispatch to accumulate conversion for node."""

    # Text content => escape (or not).
    if isinstance(node, NavigableString):
        accum.append(escape(node.string))

    # Not a node => do nothing.
    elif not isinstance(node, Tag):
        pass

    # Root.
    elif match(node, "[document]"):
        children(node, accum, escape)

    # '<a class="fig-ref" href="...">' figure reference.
    elif match(node, "a", "fig-ref"):
        key = href_key(node)
        accum.append(rf"\figref{{{key}}}")

    # '<a class="tbl-ref" href="...">' table reference.
    elif match(node, "a", "tbl-ref"):
        key = href_key(node)
        accum.append(rf"\tblref{{{key}}}")

    # '<a href="...">' with no class.
    elif match(node, "a"):
        children(node, accum, escape)

    # '<blockquote>' quotation.
    elif match(node, "blockquote"):
        children(node, accum, escape, "\\begin{quotation}\n", "\\end{quotation}\n")

    # '<br>' line break.
    elif match(node, "br"):
        accum.append("\\\\\n")

    # '<code>' inline code.
    elif match(node, "code"):
        temp = "".join(children(node, [], escape))
        temp = temp.replace("'", r"{\textquotesingle}")
        accum.append(rf"\texttt{{{temp}}}")

    # '<div class="callout">' callout block.
    elif match(node, "div", "callout"):
        children(node, accum, escape, "\\begin{callout}\n", "\\end{callout}\n")

    # '<div class="center">' callout block.
    elif match(node, "div", "center"):
        children(node, accum, escape, "\\begin{center}\n", "\\end{center}\n")

    # '<div class="content">' whole chapter.
    elif match(node, "div", "content"):
        accum.append("FIXME: chapter title")
        children(node, accum, escape)

    # '<div class="fixme">' list of problems.
    elif match(node, "div", "fixme"):
        children(node, accum, escape, r"\begin{fixme}", r"\end{fixme}")

    # '<div class="notex">' skip.
    elif match(node, "div", "notex"):
        pass

    # '<dd>' body of labeled itemize.
    elif match(node, "dd"):
        children(node, accum, escape)
        accum.append("\n\n")

    # '<dl>' description list.
    elif match(node, "dl"):
        children(node, accum, escape)

    # '<dt>' description list key.
    elif match(node, "dt"):
        children(node, accum, escape, r"\noindent \textbf{", "}: ")

    # '<em>' italics.
    elif match(node, "em"):
        children(node, accum, escape, r"\emph{", "}")

    # '<figure>' figure.
    elif match(node, "figure"):
        figure(node, accum, escape)

    # 'h2' section title.
    elif match(node, "h2"):
        title = "".join(children(node, [], escape))
        if node.has_attr("id"):
            accum.extend([r"\section{", title, r"}\label{", node["id"], "}\n"])
        else:
            accum.extend([r"\section*{", title, "}\n"])

    # '<h3>' inside '<div class="callout">' callout title
    elif (
        (node.name == "h3")
        and (node.parent.name == "div")
        and has_class(node.parent, "callout")
    ):
        children(node, accum, escape, "\n\\subsubsection*{", "}\n")

    # other '<h3>' subsection
    elif match(node, "h3"):
        children(node, accum, escape, r"\subsection*{", "}\n")

    # '<li>' list item.
    elif match(node, "li"):
        children(node, accum, escape, r"\item ", "\n")

    # '<ol>' ordered list.
    elif match(node, "ol"):
        children(node, accum, escape, "\\begin{enumerate}\n", "\\end{enumerate}\n")

    # '<p class="continue"> unindented continuation paragraph.
    elif match(node, "p", "continue"):
        children(node, accum, escape, "\n\\noindent ", "\n")

    # '<p>' => paragraph.
    elif match(node, "p"):
        children(node, accum, escape)

    # '<span class="bib-ref">' citations.
    elif match(node, "span", "bib-ref"):
        citation(node, accum, escape)

    # '<span class="bibtex-protected">' inserted by other tool.
    elif match(node, "span", "bibtex-protected"):
        citation(node, accum, escape)

    # '<span class="fixme">' markers.
    elif match(node, "span", "fixme"):
        children(node, accum, escape, r"\textbf{FIXME: ", "}")

    # '<strong>' bold text.
    elif match(node, "strong"):
        children(node, accum, escape, r"\textbf{", "}")

    # '<table>' table.
    elif match(node, "table"):
        table(node, accum, escape)

    # '<ul>' unordered list.
    elif match(node, "ul"):
        children(node, accum, escape, "\\begin{itemize}\n", "\\end{itemize}\n")

    # Unhandled.
    else:
        util.fail(f"Unknown node type {type(node)} / {node.name}: '{node}'")

    # Report back.
    return accum


def escape(text):
    """Escape special characters."""
    return (
        text
        .replace("{", "ACTUAL-LEFT-CURLY-BRACE")
        .replace("}", "ACTUAL-RIGHT-CURLY-BRACE")
        .replace("\\", r"{\textbackslash}")
        .replace("$", r"\$")
        .replace("%", r"\%")
        .replace("_", r"\_")
        .replace("^", r"{\textasciicircum}")
        .replace("#", r"\#")
        .replace("&", r"\&")
        .replace("<<<", r"<\null<\null<")
        .replace(">>>", r">\null>\null>")
        .replace("<<", r"<\null<")
        .replace(">>", r">\null>")
        .replace("~", r"$\sim$")
        .replace("©", r"{\textcopyright}")
        .replace("μ", r"{\textmu}")
        .replace("…", "...")
        .replace("ACTUAL-LEFT-CURLY-BRACE", r"\{")
        .replace("ACTUAL-RIGHT-CURLY-BRACE", r"\}")
    )


def escape_noop(text):
    """Pretend to escape (needed to simplify calling)."""
    return text


def extract_contents(pages):
    """Extract all content sections from pages."""
    doc = BeautifulSoup()
    for p in pages:
        doc.append(p.find("div", class_="content"))
    return doc


def figure(node, accum, escape):
    """Handle figure."""
    util.warning("FIGURE")


def get_extra_tex(config_path, config):
    """Get extra LaTeX."""
    root_dir = Path(config_path).parent
    head = Path(root_dir, "lib", config.theme, "info", "head.tex").read_text()
    title = f"\\title{{{config.title}}}\n\\author{{{config.author}}}\n"
    foot = Path(root_dir, "lib", config.theme, "info", "foot.tex").read_text()
    return head, title, foot


def has_class(node, class_):
    """Check if node has one of the specified classes."""
    if not node.has_attr("class"):
        return False
    if isinstance(class_, str):
        return class_ in node["class"]
    return any(c in node["class"] for c in class_)


def href_key(node):
    """Get key from href attribute if available."""
    if "#" in node["href"]:
        return node["href"].split("#")[1]
    return node["href"]


def match(node, name, class_=None):
    """Does this node match requirements?"""
    if node.name != name:
        return False
    if class_ is None:
        return True
    return has_class(node, class_)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, required=True, help="config file")
    parser.add_argument("--outfile", type=str, default=None, help="output file")
    return parser.parse_args()


def save(writer, *items):
    """Save results."""
    for i in items:
        writer.write(i)


def table(node, accum, escape):
    """Handle table."""
    util.warning("TABLE")


if __name__ == "__main__":
    main()
