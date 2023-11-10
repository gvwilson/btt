"""Ark shortcodes."""

from pathlib import Path
import re
from textwrap import dedent

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

    styled_bib = ark.site.config["_bib_"]
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
    return ark.site.config["_date_"]


@shortcodes.register("f")
def figure_ref(pargs, kwargs, node):
    """Handle [% f slug %] figure reference shortcodes."""
    util.require((len(pargs) == 1) and (not kwargs), f"Bad 'f' shortcode in {node}")
    slug = pargs[0]
    known = ark.site.config["_figures_"]
    util.require(slug in known, f"Unknown figure slug {slug} in {node}")
    return f'<a class="fig-ref" href="#{slug}">Figure&nbsp;{known[slug]}</a>'


@shortcodes.register("figure")
def figure_def(pargs, kwargs, node):
    """Handle figure definition."""
    allowed = {"cls", "scale", "slug", "img", "alt", "caption"}
    util.require(
        (not pargs) and allowed.issuperset(kwargs.keys()),
        f"Bad 'figure' shortcode {pargs} and {kwargs} in {node}",
    )

    cls = kwargs.get("cls", None)
    cls = f' class="{cls}"' if cls is not None else ""

    scale = kwargs.get("scale", None)
    scale = f' width="{scale}"' if scale is not None else ""

    slug = kwargs["slug"]
    img = kwargs["img"]
    alt = util.markdownify(kwargs["alt"], True)
    caption = util.markdownify(kwargs["caption"], True)

    util.require_file(node, img, "figure")
    known = ark.site.config["_figures_"]

    label = f"Figure&nbsp;{known[slug]}"
    return dedent(
        f"""\
        <figure id="{slug}"{cls}>
        <img src="./{img}" alt="{alt}"{scale}/>
        <figcaption markdown="1">{label}: {caption}</figcaption>
        </figure>
        """
    )


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
    for slug in ark.site.config["chapters"]:
        title = ark.site.config["_meta_"][slug]["title"]
        entry = f'<li><a href="@root/{slug}/">{title}</a></li>'
        if "tag" in ark.site.config["_meta_"][slug]:
            chapters.append(entry)
        else:
            appendices.append(entry)
    chapters = '<ol class="toc" type="1">\n' + "\n".join(chapters) + "\n</ol>"
    appendices = '<ol class="toc" type="A">\n' + "\n".join(appendices) + "\n</ol>"
    return f"{chapters}\n{appendices}"


@shortcodes.register("x")
def x_reference(pargs, kwargs, node):
    """Handle [%x slug %] cross-reference shortcode."""
    util.require(
        (len(pargs) == 1) and (not kwargs),
        f"Bad 'x' shortcode with {pargs} and {kwargs}",
    )
    slug = pargs[0]
    util.require(
        slug in ark.site.config["_number_"], f"Unknown key in 'x' shortcode {slug}"
    )
    kind = ark.site.config["_number_"][slug]["kind"]
    number = ark.site.config["_number_"][slug]["number"]
    return f"{kind}&nbsp;{number}"
