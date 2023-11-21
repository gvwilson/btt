"""Ark configuration file."""

title = "Building Tech Together"
slug = "btt"
repo = "https://github.com/gvwilson/${slug}"
author = "Greg Wilson"
draft = True

chapters = [
    "intro",
    "crunch",
    "meetings",
    "governance",
    "conflict",
    "learners",
    "cogload",
    "grading",
    "peereval",
    "topologies",
    "assemble",
    "join",
    "reteam",
    "productivity",
    "retro",
    "finale",
    "license",
    "bib",
    "conduct",
    "persuasion",
    "freelance",
    "fired",
    "credits",
    "syllabus",
]

theme = "mccole"

copy = [
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
    "*.yml",
    ".#*",
    "CODE_OF_CONDUCT.md",
    "LICENSE.md",
    "Makefile",
    "README.md",
    "requirements.txt",
]

lint = {
    "disable_h2_id": ["conduct", "license", "syllabus"],
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
    if sys.argv[1] == "--slug":
        print(slug)
    elif sys.argv[1] == "--title":
        print(title)
    else:
        assert False, f"Unknown flag {sys.argv[1]}"
