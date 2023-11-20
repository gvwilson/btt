"""Utilities."""

import importlib.util
from pathlib import Path
import sys

from bs4 import BeautifulSoup


def collect_files(config, which):
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


def fail(msg):
    """Fail unilaterally."""
    print(msg, file=sys.stderr)
    sys.exit(1)


def get_lint(config):
    """Get a lint setting or empty list."""
    return config.lint if hasattr(config, "lint") else {}


def load_config(filename):
    """Load configuration file as module."""
    spec = importlib.util.spec_from_file_location("config", filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(cond, msg):
    """Fail if condition untrue."""
    if not cond:
        fail(msg)


def source_dirs(src, config, exclude=[]):
    """Generate list of source directories."""
    exclude = set(exclude)
    return [f"{src}/{key}" for key in config.chapters if key not in exclude]


def warning(msg):
    """Print message but do not fail."""
    print(msg, file=sys.stderr)
