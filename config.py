"""Ark configuration file."""

title = "Building Tech Together"
repo = "https://github.com/gvwilson/btt"
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

theme = "book"

copy = [
    "*.png",
    "*.svg",
]

exclude = copy + [
    "*~",
    "*.csv",
    "*.png",
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
