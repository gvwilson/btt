"""Ark shortcodes."""

from pathlib import Path
import re

import ark
import pybtex.plugin
import shortcodes

import util


FIRST_H1 = re.compile(r"^#\s+.+$", re.MULTILINE)


@shortcodes.register("b")
def bibliography_ref(pargs, kwargs, node):
    """Handle [%b key1 key2 %] biblography references."""
    util.require(
        (len(pargs) > 0) and (not kwargs),
        f"Bad 'b' shortcode with {pargs} and {kwargs} in {node}",
    )
    base = "@root/bib"
    links = [f'<a class="bib-ref" href="{base}/#{k}">{k}</a>' for k in pargs]
    links = ", ".join(links)
    return f'<span class="bib-ref">[{links}]</span>'


@shortcodes.register("bibliography")
def bibliography(pargs, kwargs, node):
    """Handle [% bibliography %] shortcode."""

    def _fmt(key, body):
        return f'<dt id="{key}" class="bib-def">{key}</dt>\n<dd>{body}</dd>'

    util.require(
        (not pargs) and (not kwargs),
        f"Bad 'bibliography' shortcode with {pargs} and {kwargs} in {node}",
    )

    styled_bib = util.CACHE["bib"]
    html = pybtex.plugin.find_plugin("pybtex.backends", "html")()
    entries = [_fmt(entry.key, entry.text.render(html)) for entry in styled_bib]
    return '<dl class="bib-list">\n\n' + "\n\n".join(entries) + "\n\n</dl>"


@shortcodes.register("date")
def date(pargs, kwargs, node):
    """Handle [% date %] shortcode."""
    util.require(
        (not pargs) and (not kwargs),
        f"Bad 'date' shortcode with {pargs} and {kwargs}",
    )
    return util.get_date()


@shortcodes.register("rootpage")
def rootpage(pargs, kwargs, node):
    """Handle [% rootpage NAME.md %] shortcode."""
    util.require(
        len(pargs) == 1 and not kwargs,
        f"Bad 'rootpage' shortcode with {pargs} and {kwargs}",
    )
    path = Path(ark.site.home(), pargs[0])
    try:
        return FIRST_H1.sub("", path.read_text())
    except OSError:
        util.fail(f"cannot read .ark file {str(path)}")


@shortcodes.register("toc")
def toc(pargs, kwargs, node):
    """Handle [% toc %] table of contents shortcode."""
    util.require(
        (not pargs) and (not kwargs), f"Bad 'toc' shortcode with {pargs} and {kwargs}"
    )
    chapters = []
    appendices = []
    for slug, data in util.get_meta().items():
        entry = f'<li><a href="@root/{slug}/">{data["title"]}</a></li>'
        if "tag" in data:
            chapters.append(entry)
        else:
            appendices.append(entry)
    chapters = '<ol class="toc" type="1">\n' + "\n".join(chapters) + "\n</ol>\n"
    appendices = '<ol class="toc" type="A">\n' + "\n".join(appendices) + "\n</ol>\n"
    return f"{chapters}{appendices}"

@shortcodes.register("x")
def x_reference(pargs, kwargs, node):
    """Handle [%x slug %] cross-reference shortcode."""
    return "FIXME"
