#!/usr/bin/env python3
"""
Build a MkDocs documentation site from the OSP-PBPK-Model-Library repository.

Each top-level folder becomes a chapter. Markdown content is rendered as-is,
with download buttons appended for the PDF report and .pksim5 model files.

Site features:
- OSP blue colour palette (matching docs.open-systems-pharmacology.org)
- Hamburger navigation menu on all screen sizes (replaces top nav-tabs)
- Floating sidebar table of contents on every report page
- Home page listing all reports with PDF / pksim5 download links
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

# ──────────────────────────────────────────────────────────────────────────────
# Extra CSS – injected into docs/stylesheets/extra.css
# ──────────────────────────────────────────────────────────────────────────────
EXTRA_CSS = """\
/* ============================================================
   OSP PBPK Model Library – Custom Styles
   Colour palette inspired by docs.open-systems-pharmacology.org
   ============================================================ */

/* --- Primary colour: OSP blue -------------------------------- */
:root,
[data-md-color-scheme="default"] {
  --md-primary-fg-color:              #1565c0;
  --md-primary-fg-color--light:       #1976d2;
  --md-primary-fg-color--dark:        #0d47a1;
  --md-accent-fg-color:               #2196f3;
  --md-accent-fg-color--transparent:  rgba(33, 150, 243, .1);
}

[data-md-color-scheme="slate"] {
  --md-primary-fg-color:              #1976d2;
  --md-primary-fg-color--light:       #42a5f5;
  --md-primary-fg-color--dark:        #0d47a1;
  --md-accent-fg-color:               #42a5f5;
  --md-accent-fg-color--transparent:  rgba(66, 165, 245, .1);
}

/* --- Hamburger menu: visible on ALL screen sizes ------------- */
@media screen and (min-width: 76.25em) {
  /* Reveal the hamburger / drawer toggle button on desktop */
  .md-header__button[for="__drawer"] {
    display: inline-flex !important;
  }

  /* Slide the primary navigation sidebar out of view by default */
  .md-sidebar--primary {
    position:  fixed     !important;
    top:       0         !important;
    left:      0         !important;
    width:     12.1rem   !important;
    height:    100vh     !important;
    z-index:   4         !important;
    transform: translateX(-100%) !important;
    transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1),
                box-shadow 0.25s ease !important;
    box-shadow: none !important;
    background: var(--md-default-bg-color) !important;
    overflow-y: auto !important;
  }

  /* Slide in when the drawer checkbox is checked */
  [data-md-toggle="drawer"]:checked ~ .md-container .md-sidebar--primary {
    transform:  translateX(0) !important;
    box-shadow: 0.2rem 0 0.8rem rgba(0, 0, 0, 0.25) !important;
  }

  /* Activate the dark overlay behind the open drawer */
  [data-md-toggle="drawer"]:checked ~ .md-overlay {
    opacity:        1    !important;
    pointer-events: auto !important;
  }

  /* Content fills the full width when the sidebar is hidden */
  .md-main__inner {
    margin-left: 0 !important;
  }

  .md-content {
    max-width: 56rem;
    margin:    0 auto;
  }
}

/* --- Floating / sticky table of contents --------------------- */
@media screen and (min-width: 60em) {
  .md-sidebar--secondary .md-sidebar__scrollwrap {
    position:   sticky   !important;
    top:        4rem     !important;
    max-height: calc(100vh - 4.5rem) !important;
    overflow-y: auto     !important;
  }
}

/* Highlight the currently active TOC link */
.md-nav--secondary .md-nav__link--active {
  color:       var(--md-accent-fg-color) !important;
  font-weight: 600;
}

/* --- Download section button spacing ------------------------- */
.download-section .md-button {
  margin: 0.2rem 0.4rem 0.2rem 0;
}
"""


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def is_compound_folder(path: str) -> bool:
    """Return True if the folder contains a markdown evaluation report."""
    for f in os.listdir(path):
        if f.endswith(".md") and "evaluation_report" in f:
            return True
    return False

# ──────────────────────────────────────────────────────────────────────────────
# Per-compound processing
# ──────────────────────────────────────────────────────────────────────────────

def process_folder(folder_path: str, folder_name: str) -> dict:
    """Copy and process one compound folder into docs/.

    Returns a dict with keys: name, pdf_files, pksim_files.
    """
    dest = os.path.join(DOCS_DIR, folder_name)
    os.makedirs(dest, exist_ok=True)

    # Collect assets
    md_files   = glob.glob(os.path.join(folder_path, "*_evaluation_report.md"))
    pdf_files  = glob.glob(os.path.join(folder_path, "*.pdf"))
    pksim_files = glob.glob(os.path.join(folder_path, "*.pksim5"))
    images_dir = os.path.join(folder_path, "images")

    # Copy images directory
    if os.path.isdir(images_dir):
        dest_images = os.path.join(dest, "images")
        if os.path.exists(dest_images):
            shutil.rmtree(dest_images)
        shutil.copytree(images_dir, dest_images)

    # Copy binary assets
    for pdf in pdf_files:
        shutil.copy2(pdf, dest)
    for pksim in pksim_files:
        shutil.copy2(pksim, dest)

    pdf_basenames   = sorted(os.path.basename(p) for p in pdf_files)
    pksim_basenames = sorted(os.path.basename(p) for p in pksim_files)

    # Write index.md from the evaluation report
    dest_md = os.path.join(dest, "index.md")
    if md_files:
        with open(sorted(md_files)[0], "r", encoding="utf-8") as fh:
            content = fh.read()
        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(content)
    else:
        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(f"# {folder_name}\n")

    return {
        "name":        folder_name,
        "pdf_files":   pdf_basenames,
        "pksim_files": pksim_basenames,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Home page (index.md)
# ──────────────────────────────────────────────────────────────────────────────

def generate_index_md(chapters_data: list, docs_dir: str) -> None:
    """Generate docs/index.md listing all compounds with download links."""
    lines = [
        "# Open Systems Pharmacology PBPK Model Library",
        "",
        "Library of released PBPK substance models and evaluation reports from the"
        " [Open Systems Pharmacology](https://www.open-systems-pharmacology.org/) project.",
        "",
        "## Available Reports",
        "",
        "| Compound (HTML Report) | PDF Report | PK-Sim Project File(s) |",
        "|------------------------|:----------:|:----------------------:|",
    ]

    for ch in sorted(chapters_data, key=lambda x: x["name"].lower()):
        name = ch["name"]
        base = f"{name}/"

        pdf_cell = " ".join(
            f'[:material-file-pdf-box: {pdf}]({base}{pdf}){{: download="{pdf}" }}'
            for pdf in ch["pdf_files"]
        ) or "—"

        pksim_cell = " ".join(
            f'[:material-download: {pksim}]({base}{pksim}){{: download="{pksim}" }}'
            for pksim in ch["pksim_files"]
        ) or "—"

        lines.append(f"| [{name}]({base}index.md) | {pdf_cell} | {pksim_cell} |")

    lines.append("")

    with open(os.path.join(docs_dir, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ──────────────────────────────────────────────────────────────────────────────
# MkDocs configuration
# ──────────────────────────────────────────────────────────────────────────────

def build_nav(chapters: list) -> list:
    """Build the MkDocs nav list."""
    nav = [{"Home": "index.md"}]
    for chapter in sorted(chapters):
        nav.append({chapter: f"{chapter}/index.md"})
    return nav


def generate_mkdocs_yml(nav: list) -> None:
    """Write the mkdocs.yml configuration file."""
    nav_yaml  = yaml.dump({"nav": nav}, default_flow_style=False, allow_unicode=True)
    nav_block = nav_yaml[len("nav:"):].rstrip()

    content = f"""site_name: Open Systems Pharmacology PBPK Model Library
site_description: Library of released PBPK substance models and evaluation reports
docs_dir: docs
site_dir: site

theme:
  name: material
  palette:
    - scheme: default
      primary: blue
      accent: blue
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: blue
      accent: blue
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.sections
    - navigation.top
    - toc.follow
    - search.highlight
    - search.suggest
    - content.code.copy
  icon:
    repo: fontawesome/brands/github

extra_css:
  - stylesheets/extra.css

markdown_extensions:
  - attr_list
  - tables
  - admonition
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - toc:
      permalink: true
      toc_depth: 3

nav:{nav_block}
"""

    with open(MKDOCS_YML, "w", encoding="utf-8") as fh:
        fh.write(content)


# ──────────────────────────────────────────────────────────────────────────────
# Asset generation
# ──────────────────────────────────────────────────────────────────────────────

def generate_assets(docs_dir: str) -> None:
    """Write extra CSS into docs/stylesheets/extra.css."""
    css_dir = os.path.join(docs_dir, "stylesheets")
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, "extra.css"), "w", encoding="utf-8") as fh:
        fh.write(EXTRA_CSS)


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # Clean and recreate docs dir
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    # Write extra CSS
    generate_assets(DOCS_DIR)

    # Process each compound folder
    chapters_data = []
    for entry in sorted(os.listdir(REPO_ROOT)):
        if entry.startswith(EXCLUDE_PREFIXES):
            continue
        full_path = os.path.join(REPO_ROOT, entry)
        if not os.path.isdir(full_path):
            continue
        if not is_compound_folder(full_path):
            continue
        chapters_data.append(process_folder(full_path, entry))

    # Generate home page listing all reports
    generate_index_md(chapters_data, DOCS_DIR)

    # Build nav and write mkdocs.yml
    chapters = [ch["name"] for ch in chapters_data]
    nav      = build_nav(chapters)
    generate_mkdocs_yml(nav)

    print(f"Docs built: {len(chapters)} chapters → {DOCS_DIR}")
    print(f"MkDocs config written → {MKDOCS_YML}")


if __name__ == "__main__":
    main()
