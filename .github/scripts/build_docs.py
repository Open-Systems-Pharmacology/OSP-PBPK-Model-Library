#!/usr/bin/env python3
"""
Build a MkDocs documentation site from the OSP-PBPK-Model-Library repository.

Each top-level folder becomes a chapter. Markdown content is rendered as-is,
with download buttons prepended for the PDF report and .pksim5 model files.
"""

import os
import shutil
import glob
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
MKDOCS_YML = os.path.join(REPO_ROOT, "mkdocs.yml")

# Folders to exclude (hidden directories and non-compound folders)
EXCLUDE_PREFIXES = (".", "_")


def is_compound_folder(path: str) -> bool:
    """Return True if the folder contains a markdown evaluation report."""
    for f in os.listdir(path):
        if f.endswith(".md") and "evaluation_report" in f:
            return True
    return False


def make_download_buttons(folder_name: str, pdf_files: list, pksim_files: list) -> str:
    """Return an HTML block with download buttons for all assets."""
    lines = [
        "",
        '<div class="download-section" markdown="1">',
        "",
        "## Downloads",
        "",
    ]
    for pdf in sorted(pdf_files):
        label = os.path.basename(pdf)
        lines.append(
            f'[:material-file-pdf-box: Download PDF Report]({label}){{: .md-button download="{label}" }}'
        )
        lines.append("")
    for pksim in sorted(pksim_files):
        label = os.path.basename(pksim)
        lines.append(
            f'[:material-download: Download PBPK Model ({label})]({label}){{: .md-button .md-button--primary download="{label}" }}'
        )
        lines.append("")
    lines.append("</div>")
    lines.append("")
    return "\n".join(lines)


def process_folder(folder_path: str, folder_name: str):
    """Copy and process one compound folder into docs/."""
    dest = os.path.join(DOCS_DIR, folder_name)
    os.makedirs(dest, exist_ok=True)

    # Collect assets
    md_files = glob.glob(os.path.join(folder_path, "*_evaluation_report.md"))
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    pksim_files = glob.glob(os.path.join(folder_path, "*.pksim5"))
    images_dir = os.path.join(folder_path, "images")

    # Copy images directory
    if os.path.isdir(images_dir):
        dest_images = os.path.join(dest, "images")
        if os.path.exists(dest_images):
            shutil.rmtree(dest_images)
        shutil.copytree(images_dir, dest_images)

    # Copy PDF files
    for pdf in pdf_files:
        shutil.copy2(pdf, dest)

    # Copy .pksim5 files
    for pksim in pksim_files:
        shutil.copy2(pksim, dest)

    # Process markdown — append download section
    if md_files:
        md_src = md_files[0]
        with open(md_src, "r", encoding="utf-8") as fh:
            content = fh.read()

        download_block = make_download_buttons(
            folder_name,
            [os.path.basename(p) for p in pdf_files],
            [os.path.basename(p) for p in pksim_files],
        )
        content = content + "\n" + download_block

        dest_md = os.path.join(dest, "index.md")
        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(content)
    else:
        # Fallback: create a minimal index page
        dest_md = os.path.join(dest, "index.md")
        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(f"# {folder_name}\n")
            download_block = make_download_buttons(
                folder_name,
                [os.path.basename(p) for p in pdf_files],
                [os.path.basename(p) for p in pksim_files],
            )
            fh.write(download_block)


def build_nav(chapters: list) -> list:
    """Build the MkDocs nav list."""
    nav = [{"Home": "index.md"}]
    for chapter in sorted(chapters):
        nav.append({chapter: f"{chapter}/index.md"})
    return nav


def generate_mkdocs_yml(nav: list):
    """Write the mkdocs.yml configuration file."""
    # Build the nav section using yaml for safe serialization
    nav_yaml = yaml.dump({"nav": nav}, default_flow_style=False, allow_unicode=True)
    nav_block = nav_yaml[len("nav:"):].rstrip()

    content = f"""site_name: OSP PBPK Model Library
site_description: Library of released PBPK substance models and evaluation reports
docs_dir: docs
site_dir: site

theme:
  name: material
  palette:
    - scheme: default
      primary: teal
      accent: teal
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: teal
      accent: teal
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.top
    - search.highlight
    - content.code.copy
  icon:
    repo: fontawesome/brands/github

markdown_extensions:
  - attr_list
  - tables
  - admonition
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - toc:
      permalink: true

nav:{nav_block}
"""

    with open(MKDOCS_YML, "w", encoding="utf-8") as fh:
        fh.write(content)


def main():
    # Clean and recreate docs dir
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    # Copy root README as index
    readme = os.path.join(REPO_ROOT, "README.md")
    if os.path.isfile(readme):
        shutil.copy2(readme, os.path.join(DOCS_DIR, "index.md"))
    else:
        with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as fh:
            fh.write("# OSP PBPK Model Library\n\nLibrary of released PBPK substance models and evaluation reports.\n")

    chapters = []
    for entry in os.listdir(REPO_ROOT):
        if entry.startswith(EXCLUDE_PREFIXES):
            continue
        full_path = os.path.join(REPO_ROOT, entry)
        if not os.path.isdir(full_path):
            continue
        if not is_compound_folder(full_path):
            continue
        process_folder(full_path, entry)
        chapters.append(entry)

    nav = build_nav(chapters)
    generate_mkdocs_yml(nav)

    print(f"Docs built: {len(chapters)} chapters → {DOCS_DIR}")
    print(f"MkDocs config written → {MKDOCS_YML}")


if __name__ == "__main__":
    main()
