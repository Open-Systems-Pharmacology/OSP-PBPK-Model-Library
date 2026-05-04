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
- SEO optimizations with meta tags, structured data, and semantic HTML
"""

import argparse
import os
import shutil
import glob
import yaml
import re
from urllib.parse import quote

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
MKDOCS_YML = os.path.join(REPO_ROOT, "mkdocs.yml")

# Folders to exclude (hidden directories and non-compound folders)
EXCLUDE_PREFIXES = (".", "_")

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug matching python-markdown's TOC behavior.

    Lowercases, replaces sequences of non-alphanumeric chars with a single hyphen,
    and trims leading/trailing hyphens.
    """
    slug = text.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug

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


def is_compound_folder(path: str) -> bool:
    """Return True if the folder contains a markdown evaluation report."""
    for f in os.listdir(path):
        if f.endswith(".md") and "evaluation_report" in f:
            return True
    return False


def categorize_compound(folder_path: str, md_files: list) -> str:
    """Categorize a compound based on keywords in its evaluation report."""
    # Default category
    category = "Other Compounds"

    # If no markdown files, return default
    if not md_files:
        return category

    # Read first few hundred characters of the evaluation report
    try:
        with open(sorted(md_files)[0], "r", encoding="utf-8") as fh:
            content = fh.read(4000).lower()

        # Check for drug class keywords
        if any(kw in content for kw in ["antibiotic", "aminoglycoside", "antimicrobial"]):
            category = "Antibiotics"
        elif any(kw in content for kw in ["antiviral", "hiv", "protease inhibitor", "antiretroviral"]):
            category = "Antivirals"
        elif any(kw in content for kw in ["opioid", "analgesic", "anesthesia", "alfentanil", "sufentanil", "fentanil"]):
            category = "Anesthetics & Analgesics"
        elif any(kw in content for kw in ["benzodiazepine", "anxiolytic", "sedative", "midazolam", "alprazolam", "triazolam"]):
            category = "Sedatives & Anxiolytics"
        elif any(kw in content for kw in ["anticonvulsant", "antiepileptic", "carbamazepine", "epilepsy"]):
            category = "Anticonvulsants"
        elif any(kw in content for kw in ["cardiovascular", "antiarrhythmic", "cardiac", "digoxin", "mexiletine", "felodipine", "verapamil"]):
            category = "Cardiovascular Agents"
        elif any(kw in content for kw in ["antifungal", "azole", "itraconazole", "fluconazole"]):
            category = "Antifungals"
        elif any(kw in content for kw in ["antibody", "monoclonal", "immunoglobulin", "mab"]):
            category = "Antibodies & Biologics"
        elif "pediatric" in content or "neonates" in content or "children" in content:
            category = "Pediatric Models"

    except Exception:
        pass

    return category

# ──────────────────────────────────────────────────────────────────────────────
# Per-compound processing
# ──────────────────────────────────────────────────────────────────────────────

def add_related_models_section(content: str, compound_name: str, category: str, all_compounds: list) -> str:
    """Add a 'Related Models' section at the end of the compound page."""
    # Find compounds in the same category (excluding the current one)
    related = [c for c in all_compounds if c["category"] == category and c["name"] != compound_name]

    if not related:
        return content

    # Limit to 5 related models
    related = sorted(related, key=lambda x: x["name"])[:5]

    # Build the related models section
    section = [
        "",
        "---",
        "",
        "## Related Models",
        "",
        f"Explore other {category} models in this library:",
        "",
    ]

    for model in related:
        section.append(f"- [{model['name']}](../{model['name']}/index.md) - PBPK model and evaluation report")

    section.extend([
        "",
        f"[View all {category} →](../index.md#{slugify(category)})",
        "",
        "[← Back to Model Library Home](../index.md)",
        "",
    ])

    return content + "\n".join(section)


def collect_folder_metadata(folder_path: str, folder_name: str) -> dict:
    """Collect metadata from a compound folder without writing files.

    Returns a dict with keys: name, pdf_files, pksim_files, category.
    """
    # Collect assets
    md_files   = glob.glob(os.path.join(folder_path, "*_evaluation_report.md"))
    pdf_files  = glob.glob(os.path.join(folder_path, "*.pdf"))
    pksim_files = glob.glob(os.path.join(folder_path, "*.pksim5"))

    # Collect basenames
    pdf_basenames   = sorted(os.path.basename(p) for p in pdf_files)
    pksim_basenames = sorted(os.path.basename(p) for p in pksim_files)

    # Determine category by analyzing the evaluation report
    category = categorize_compound(folder_path, md_files)

    return {
        "name":        folder_name,
        "pdf_files":   pdf_basenames,
        "pksim_files": pksim_basenames,
        "category":    category,
    }


def process_folder(folder_path: str, folder_name: str, all_compounds: list) -> dict:
    """Copy and process one compound folder into docs/.

    Returns a dict with keys: name, pdf_files, pksim_files, category.
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

    # DO NOT copy PDF and pksim5 files - we'll use GitHub raw links instead
    # Just collect their basenames
    pdf_basenames   = sorted(os.path.basename(p) for p in pdf_files)
    pksim_basenames = sorted(os.path.basename(p) for p in pksim_files)

    # Determine category by analyzing the evaluation report
    category = categorize_compound(folder_path, md_files)

    # Write index.md from the evaluation report
    dest_md = os.path.join(dest, "index.md")
    if md_files:
        with open(sorted(md_files)[0], "r", encoding="utf-8") as fh:
            content = fh.read()

        # Add SEO frontmatter if not present
        if not content.startswith("---"):
            seo_frontmatter = f"""---
title: {folder_name} PBPK Model - Physiologically Based Pharmacokinetic Evaluation Report
description: PBPK (Physiologically Based Pharmacokinetic) model evaluation report for {folder_name}. Detailed pharmacokinetic modeling and simulation results using Open Systems Pharmacology platform.
keywords: {folder_name}, PBPK model, physiologically based pharmacokinetic model, {folder_name} pharmacokinetics, drug modeling, PK-Sim
---

"""
            content = seo_frontmatter + content

        # Add related models section
        content = add_related_models_section(content, folder_name, category, all_compounds)

        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(content)
    else:
        with open(dest_md, "w", encoding="utf-8") as fh:
            fh.write(f"""---
title: {folder_name} PBPK Model
description: PBPK model evaluation for {folder_name}
---

# {folder_name}
""")

    return {
        "name":        folder_name,
        "pdf_files":   pdf_basenames,
        "pksim_files": pksim_basenames,
        "category":    category,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Home page (index.md)
# ──────────────────────────────────────────────────────────────────────────────

def generate_index_md(chapters_data: list, docs_dir: str, repository_name: str, tag_or_branch: str) -> None:
    """Generate docs/index.md listing all compounds with download links and SEO metadata."""
    index_1_path = os.path.join(REPO_ROOT, ".github", "assets", "index_1.md")
    with open(index_1_path, "r", encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    lines.append("")

    # Group compounds by category
    from collections import defaultdict
    categories = defaultdict(list)
    for ch in chapters_data:
        categories[ch["category"]].append(ch)

    # Sort categories for consistent ordering
    category_order = [
        "Antibiotics",
        "Antivirals",
        "Antifungals",
        "Anesthetics & Analgesics",
        "Sedatives & Anxiolytics",
        "Anticonvulsants",
        "Cardiovascular Agents",
        "Antibodies & Biologics",
        "Pediatric Models",
        "Other Compounds",
    ]

    for category in category_order:
        if category not in categories:
            continue

        # Add H3 heading for each category
        lines.append(f"### {category}")
        lines.append("")
        lines.append("| Compound (HTML Report) | PDF Report | PK-Sim Project File(s) |")
        lines.append("|------------------------|:----------:|:----------------------:|")

        for ch in sorted(categories[category], key=lambda x: x["name"].lower()):
            name = ch["name"]
            base = f"{name}/"

            # Generate GitHub raw links for PDF files with alt text
            pdf_cell = " ".join(
                f'[:material-file-pdf-box:{{: .pdf-icon aria-label="Download {pdf} PDF report" title="Download {pdf} PDF report" }} {pdf}](https://raw.githubusercontent.com/{repository_name}/{tag_or_branch}/{quote(name, safe="")}/{quote(pdf, safe="")}){{: download="{pdf}" }}'
                for pdf in ch["pdf_files"]
            ) or "—"

            # Generate GitHub raw links for pksim5 files with alt text
            pksim_cell = " ".join(
                f'[:material-download:{{: .pksim-icon aria-label="Download {pksim} PK-Sim project file" title="Download {pksim} PK-Sim project file" }} {pksim}](https://raw.githubusercontent.com/{repository_name}/{tag_or_branch}/{quote(name, safe="")}/{quote(pksim, safe="")}){{: download="{pksim}" }}'
                for pksim in ch["pksim_files"]
            ) or "—"

            lines.append(f"| [{name}]({base}index.md) | {pdf_cell} | {pksim_cell} |")

        lines.append("")
    index_2_path = os.path.join(REPO_ROOT, ".github", "assets", "index_2.md")
    with open(index_2_path, "r", encoding="utf-8") as fh:
        lines.extend(fh.read().splitlines())
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


def generate_mkdocs_yml(nav: list, release_title: str = "") -> None:
    """Write the mkdocs.yml configuration file with SEO optimizations."""
    nav_yaml  = yaml.dump({"nav": nav}, default_flow_style=False, allow_unicode=True)
    nav_block = nav_yaml[len("nav:"):].rstrip()

    site_name = "OSP PBPK Model Library"
    if release_title:
        # Escape problematic characters for YAML double-quoted scalar
        escaped_title = release_title.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
        site_name += f" ({escaped_title})"

    content = f"""site_name: "{site_name}"
site_description: "Comprehensive library of validated PBPK (Physiologically Based Pharmacokinetic) models and qualification reports for drug development. Open-source whole-body PBPK modeling and simulation software for systems biology and multiscale physiological modeling."
site_url: https://open-systems-pharmacology.github.io/OSP-PBPK-Model-Library/
site_author: Open Systems Pharmacology Community
copyright: Copyright &copy; Open Systems Pharmacology Community
docs_dir: docs
site_dir: site

use_directory_urls: true

theme:
  name: material
  language: en
  custom_dir: overrides
  favicon: favicon.ico
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
    - navigation.tabs.sticky
    - navigation.indexes
    - navigation.path
    - toc.follow
    - search.highlight
    - search.suggest
    - search.share
    - content.code.copy
  icon:
    repo: fontawesome/brands/github

repo_url: https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library
repo_name: OSP-PBPK-Model-Library

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/Open-Systems-Pharmacology
      name: Open Systems Pharmacology on GitHub
    - icon: fontawesome/solid/globe
      link: https://www.open-systems-pharmacology.org/
      name: Open Systems Pharmacology Website
  generator: false

extra_css:
  - stylesheets/extra.css

plugins:
  - search:
      lang: en
      separator: '[\\s\\-,:!=\\[\\]()\"/]+|\\.(?!\\d)|&[lg]t;'
  - meta-descriptions

markdown_extensions:
  - attr_list
  - tables
  - admonition
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - toc:
      permalink: true
      permalink_title: Anchor link to this section for reference
      toc_depth: 3
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.superfences
  - pymdownx.details
  - md_in_html
  - abbr
  - def_list

nav:{nav_block}
"""

    with open(MKDOCS_YML, "w", encoding="utf-8") as fh:
        fh.write(content)


# ──────────────────────────────────────────────────────────────────────────────
# Asset generation
# ──────────────────────────────────────────────────────────────────────────────

def generate_assets(docs_dir: str) -> None:
    """Write extra CSS and HTML overrides for SEO."""
    # Write extra CSS into docs/stylesheets/extra.css
    css_dir = os.path.join(docs_dir, "stylesheets")
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, "extra.css"), "w", encoding="utf-8") as fh:
        fh.write(EXTRA_CSS)

    # Copy favicon from .github/assets to docs root
    favicon_src = os.path.join(REPO_ROOT, ".github", "assets", "favicon.ico")
    if os.path.exists(favicon_src):
        favicon_dest = os.path.join(docs_dir, "favicon.ico")
        shutil.copy2(favicon_src, favicon_dest)

    # Create overrides directory for custom HTML templates
    overrides_dir = os.path.join(REPO_ROOT, "overrides")
    os.makedirs(overrides_dir, exist_ok=True)

    # Generate robots.txt in docs root
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://open-systems-pharmacology.github.io/OSP-PBPK-Model-Library/sitemap.xml
"""
    with open(os.path.join(docs_dir, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(robots_txt)

    # Generate main.html with structured data
    structured_data_script = """
{% extends "base.html" %}

{% block extrahead %}
  {{ super() }}

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{{ page.canonical_url if page else config.site_url }}">
  <meta property="og:title" content="{{ page.title | default(config.site_name, true) if page else config.site_name }}">
  <meta property="og:description" content="{{ page.meta.description if page and page.meta and page.meta.description else config.site_description }}">
  <meta property="og:site_name" content="{{ config.site_name }}">
  <meta property="og:image" content="https://www.open-systems-pharmacology.org/assets/images/logo.png">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{{ page.canonical_url if page else config.site_url }}">
  <meta name="twitter:title" content="{{ page.title | default(config.site_name, true) if page else config.site_name }}">
  <meta name="twitter:description" content="{{ page.meta.description if page and page.meta and page.meta.description else config.site_description }}">
  <meta name="twitter:image" content="https://www.open-systems-pharmacology.org/assets/images/logo.png">

  <!-- Structured Data (JSON-LD) for SEO -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": {{ config.site_name | tojson }},
    "description": {{ config.site_description | tojson }},
    "url": {{ config.site_url | tojson }},
    "publisher": {
      "@type": "Organization",
      "name": "Open Systems Pharmacology",
      "url": "https://www.open-systems-pharmacology.org/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.open-systems-pharmacology.org/assets/images/logo.png"
      }
    },
    "potentialAction": {
      "@type": "SearchAction",
      "target": {{ (config.site_url ~ '?q={search_term_string}') | tojson }},
      "query-input": "required name=search_term_string"
    }
  }
  </script>

  <!-- Dataset Schema for PBPK Model Library -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Dataset",
    "name": "Open Systems Pharmacology PBPK Model Library",
    "description": "Comprehensive library of validated PBPK (Physiologically Based Pharmacokinetic) models for drug development and pharmaceutical research",
    "url": {{ config.site_url | tojson }},
    "keywords": ["PBPK", "pharmacokinetic modeling", "drug development", "PK-Sim", "MoBi", "systems pharmacology", "ADME"],
    "license": "https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library#license",
    "creator": {
      "@type": "Organization",
      "name": "Open Systems Pharmacology",
      "url": "https://www.open-systems-pharmacology.org/"
    },
    "distribution": {
      "@type": "DataDownload",
      "encodingFormat": "application/zip",
      "contentUrl": "https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library"
    }
  }
  </script>

  <!-- SoftwareApplication Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "PK-Sim PBPK Models",
    "applicationCategory": "ScientificApplication",
    "operatingSystem": "Windows",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    },
    "description": "Validated PBPK models for use with PK-Sim and MoBi software for pharmaceutical research and drug development",
    "url": {{ config.site_url | tojson }},
    "publisher": {
      "@type": "Organization",
      "name": "Open Systems Pharmacology"
    }
  }
  </script>

  {% if page and page.meta and page.meta.title %}
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "{{ page.meta.title | default(page.title, true) }}",
    "description": "{{ page.meta.description | default('PBPK model documentation', true) }}",
    "author": {
      "@type": "Organization",
      "name": "Open Systems Pharmacology"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Open Systems Pharmacology",
      "url": "https://www.open-systems-pharmacology.org/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.open-systems-pharmacology.org/assets/images/logo.png"
      }
    },
    "url": "{{ page.canonical_url }}",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "{{ page.canonical_url }}"
    },
    "keywords": "{{ page.meta.keywords | default('PBPK, physiologically based pharmacokinetic modeling, drug development', true) }}"
  }
  </script>
  {% endif %}

  {% if page and page.meta and page.meta.keywords %}
  <meta name="keywords" content="{{ page.meta.keywords }}">
  {% endif %}

  {% if page %}
  <link rel="canonical" href="{{ page.canonical_url }}">
  {% endif %}

  <!-- Language -->
  <meta http-equiv="content-language" content="en">
  <meta name="language" content="English">

{% endblock %}
"""

    with open(os.path.join(overrides_dir, "main.html"), "w", encoding="utf-8") as fh:
        fh.write(structured_data_script)


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build MkDocs documentation site.")
    parser.add_argument(
        "--release-title",
        default="",
        help="Release title to append in brackets to the home page header.",
    )
    parser.add_argument(
        "--tag-or-branch",
        required=True,
        help="Tag or branch name for generating GitHub raw links.",
    )
    parser.add_argument(
        "--repository-name",
        required=True,
        help="Repository name including user (e.g., 'Open-Systems-Pharmacology/OSP-PBPK-Model-Library').",
    )
    args = parser.parse_args()

    # Clean and recreate docs dir
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    # Write extra CSS
    generate_assets(DOCS_DIR)

    # First pass: collect all compound metadata (for categorization)
    chapters_data = []
    compound_folders = []
    for entry in sorted(os.listdir(REPO_ROOT)):
        if entry.startswith(EXCLUDE_PREFIXES):
            continue
        full_path = os.path.join(REPO_ROOT, entry)
        if not os.path.isdir(full_path):
            continue
        if not is_compound_folder(full_path):
            continue
        compound_folders.append((full_path, entry))
        # First pass: collect metadata without writing files
        chapters_data.append(collect_folder_metadata(full_path, entry))

    # Second pass: process folders with cross-linking and write files
    for full_path, entry in compound_folders:
        process_folder(full_path, entry, all_compounds=chapters_data)

    # Generate home page listing all reports
    generate_index_md(chapters_data, DOCS_DIR, args.repository_name, args.tag_or_branch)

    # Build nav and write mkdocs.yml
    chapters = [ch["name"] for ch in chapters_data]
    nav      = build_nav(chapters)
    generate_mkdocs_yml(nav, args.release_title)

    print(f"Docs built: {len(chapters)} chapters → {DOCS_DIR}")
    print(f"MkDocs config written → {MKDOCS_YML}")


if __name__ == "__main__":
    main()
