"""Ark configuration file."""

title = "Building Tech Together"
repo = "https://github.com/gvwilson/btt"
author = "Greg Wilson"
do_blank = True

chapters = [
    "intro",
    "crunch",
    "meetings",
    "governance",
    "conflict",
    "teams",
    "communicate",
    "projects",
    "process",
    "automation",
    "evaluation",
    "structure",
    "testing",
    "errors",
    "fairness",
    "learners",
    "cogload",
    "motivation",
    "delivery",
    "review",
    "roles",
    "property",
    "security",
    "rights",
    "responsibilities",
    "finale",
    "license",
    "bib",
    "conduct",
    "checklists",
    "persuasion",
    "join",
    "freelance",
    "fired",
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
    "disable_h2_id": ["conduct", "license"],
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
