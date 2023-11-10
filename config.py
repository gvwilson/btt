"""Ark configuration file."""

title = "Building Tech Together"
repo = "https://github.com/gvwilson/btt"
author = "Greg Wilson"

chapters = [
    "intro",
    "finale",
    "license",
    "bib",
    "conduct",
    "credits",
]

theme = "book"

copy = [
    "*.svg",
]

exclude = copy + [
    "*~",
    "*.csv",
    "*.py",
    "*.yml",
    ".#*",
    "CODE_OF_CONDUCT.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "requirements.txt",
]

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}

src_dir = "src"
out_dir = "docs"

extension = "/"
