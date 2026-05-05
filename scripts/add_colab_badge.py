#!/usr/bin/env python3
"""Add Google Colab and Binder launch badges to chapter pages and notebooks.

Inserts a Colab + Binder badge block near the top of every chapter Markdown
file that has a sibling Jupyter notebook, and prepends a matching badge cell
to every notebook under the book directory. Each badge deep-links to the
specific ``.ipynb``:

* Colab: ``colab.research.google.com/github/<owner>/<repo>/blob/<branch>/<path>``
* Binder: ``mybinder.org/v2/gh/<owner>/<repo>/<branch>?urlpath=lab/tree/<path>``

The script is idempotent: a file already containing either badge is left
unchanged. By default the GitHub slug is read from ``project.github`` in
``myst.yml``.

Usage:
    python scripts/add_colab_badge.py --dry-run
    python scripts/add_colab_badge.py
    python scripts/add_colab_badge.py --repo giswqs/GeoAI-Book --branch main
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import nbformat

COLAB_BADGE_SVG = "https://colab.research.google.com/assets/colab-badge.svg"
BINDER_BADGE_SVG = "https://mybinder.org/badge_logo.svg"
COLAB_OPEN_PREFIX = "https://colab.research.google.com/github/"
BINDER_OPEN_PREFIX = "https://mybinder.org/v2/gh/"
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


def make_badges(repo: str, branch: str, notebook_path: str) -> str:
    """Return the Markdown snippet for the Colab and Binder launch badges.

    Args:
        repo: GitHub ``owner/name`` slug.
        branch: Branch or ref to link to.
        notebook_path: Repo-relative POSIX path to the ``.ipynb`` file.

    Returns:
        A two-line Markdown block: one badge per line.
    """
    colab_url = f"{COLAB_OPEN_PREFIX}{repo}/blob/{branch}/{notebook_path}"
    binder_url = f"{BINDER_OPEN_PREFIX}{repo}/{branch}?urlpath=lab/tree/{notebook_path}"
    return (
        f"[![image]({COLAB_BADGE_SVG})]({colab_url})\n"
        f"[![image]({BINDER_BADGE_SVG})]({binder_url})"
    )


def has_launch_badge(text: str) -> bool:
    """Return True if ``text`` already contains a Colab or Binder badge."""
    return COLAB_BADGE_SVG in text or BINDER_BADGE_SVG in text


def insert_badges_into_markdown(md_text: str, badges: str) -> str:
    """Insert ``badges`` after the YAML frontmatter, before the body.

    Args:
        md_text: Original Markdown content.
        badges: Badge block to inject.

    Returns:
        New Markdown content with the badges inserted as their own paragraph.
    """
    match = FRONTMATTER_RE.match(md_text)
    if match:
        head = match.group(0)
        rest = md_text[match.end() :].lstrip("\n")
        return f"{head}\n{badges}\n\n{rest}"
    return f"{badges}\n\n{md_text.lstrip()}"


def process_markdown(
    md_path: Path,
    repo: str,
    branch: str,
    project_root: Path,
    dry_run: bool,
) -> str:
    """Add Colab and Binder badges to a Markdown file paired with a notebook.

    Args:
        md_path: Markdown file to update.
        repo: GitHub ``owner/name`` slug.
        branch: Branch or ref to link to.
        project_root: Repo root used to compute the relative notebook path.
        dry_run: If True, do not write changes.

    Returns:
        One of ``"added"``, ``"skipped"``, ``"no-notebook"``.
    """
    nb_path = md_path.with_suffix(".ipynb")
    if not nb_path.exists():
        return "no-notebook"
    text = md_path.read_text(encoding="utf-8")
    if has_launch_badge(text):
        return "skipped"
    rel = nb_path.relative_to(project_root).as_posix()
    new_text = insert_badges_into_markdown(text, make_badges(repo, branch, rel))
    if not dry_run:
        md_path.write_text(new_text, encoding="utf-8")
    return "added"


def process_notebook(
    nb_path: Path,
    repo: str,
    branch: str,
    project_root: Path,
    dry_run: bool,
) -> str:
    """Prepend a Colab + Binder badge cell to a notebook.

    Args:
        nb_path: Notebook file to update.
        repo: GitHub ``owner/name`` slug.
        branch: Branch or ref to link to.
        project_root: Repo root used to compute the relative notebook path.
        dry_run: If True, do not write changes.

    Returns:
        ``"added"`` or ``"skipped"``.
    """
    nb = nbformat.read(nb_path, as_version=4)
    existing = "\n".join(
        cell.get("source", "")
        for cell in nb.cells
        if cell.get("cell_type") == "markdown"
    )
    if has_launch_badge(existing):
        return "skipped"
    rel = nb_path.relative_to(project_root).as_posix()
    badge_cell = nbformat.v4.new_markdown_cell(make_badges(repo, branch, rel))
    nb.cells.insert(0, badge_cell)
    if not dry_run:
        nbformat.write(nb, nb_path)
    return "added"


def repo_from_myst_yml(project_root: Path) -> str | None:
    """Best-effort extraction of ``project.github`` from ``myst.yml``."""
    p = project_root / "myst.yml"
    if not p.exists():
        return None
    for line in p.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\s*github:\s*(\S+)", line)
        if m:
            slug = m.group(1).strip().strip("\"'")
            slug = slug.removeprefix("https://github.com/").rstrip("/")
            return slug
    return None


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Project root (defaults to the repository root).",
    )
    parser.add_argument(
        "--book-dir",
        default="book",
        help="Directory under root to scan (default: book).",
    )
    parser.add_argument(
        "--repo",
        default=None,
        help="GitHub owner/repo slug (default: read from myst.yml).",
    )
    parser.add_argument(
        "--branch",
        default="main",
        help="Branch or ref used in the Colab URL (default: main).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report planned changes without modifying any files.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point. Returns a process exit code."""
    args = parse_args()
    root = args.root.resolve()
    book = root / args.book_dir
    if not book.is_dir():
        print(f"error: {book} is not a directory", file=sys.stderr)
        return 1

    repo = args.repo or repo_from_myst_yml(root)
    if not repo:
        print(
            "error: --repo not given and could not infer it from myst.yml",
            file=sys.stderr,
        )
        return 1

    md_results: dict[str, list[str]] = {
        "added": [],
        "skipped": [],
        "no-notebook": [],
    }
    for md in sorted(book.rglob("*.md")):
        outcome = process_markdown(md, repo, args.branch, root, args.dry_run)
        md_results[outcome].append(md.relative_to(root).as_posix())

    nb_results: dict[str, list[str]] = {"added": [], "skipped": []}
    for nb in sorted(book.rglob("*.ipynb")):
        if ".ipynb_checkpoints" in nb.parts:
            continue
        outcome = process_notebook(nb, repo, args.branch, root, args.dry_run)
        nb_results[outcome].append(nb.relative_to(root).as_posix())

    prefix = "[dry-run] " if args.dry_run else ""
    print(
        f"{prefix}Markdown: added={len(md_results['added'])}, "
        f"skipped={len(md_results['skipped'])}, "
        f"no-notebook={len(md_results['no-notebook'])}"
    )
    for path in md_results["added"]:
        print(f"  + {path}")
    print(
        f"{prefix}Notebooks: added={len(nb_results['added'])}, "
        f"skipped={len(nb_results['skipped'])}"
    )
    for path in nb_results["added"]:
        print(f"  + {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
