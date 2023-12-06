"""Ark configuration file."""

title = "Building Tech Together"
slug = "btt"
repo = f"https://github.com/gvwilson/{slug}"
author = "Greg Wilson"
draft = True
debug = False

chapters = [
    "intro",
    "cogload",
    "meetings",
    "decomp",
    "teaming",
    "grading",
    "property",
    "finale",
]

appendices = [
    "license",
    "bib",
    "conduct",
    "contrib",
    "credits",
    "syllabus",
]

contents = chapters + appendices

theme = "mccole"

copy = [
    "*.jpg",
    "*.png",
    "*.svg",
]

exclude = copy + [
    "*~",
    "*.csv",
    "*.png",
    "*.pdf",
    "*.py",
    "*.tbl",
    "*.txt",
    "*.yml",
    ".#*",
    "CODE_OF_CONDUCT.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "requirements.txt",
]

lint = {
    "disable_h2_id": ["@root", "conduct", "contrib", "license", "syllabus"],
}

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

# Display values for LaTeX generation.
if __name__ == "__main__":
    import sys

    assert len(sys.argv) == 2, "Expect exactly one argument"
    if sys.argv[1] == "--order":
        print(" ".join(contents))
    elif sys.argv[1] == "--slug":
        print(slug)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
