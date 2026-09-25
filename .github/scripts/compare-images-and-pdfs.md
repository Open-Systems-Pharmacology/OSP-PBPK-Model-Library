# Image and PDF Comparison GitHub Action

## Overview

This GitHub Action automatically compares images and PDFs in pull requests, providing:
- A content-based similarity metric for images that ignores the plot background
- Text comparison for PDF files

## Features

### Image Comparison
- Compares only the *plotted content* (curves, dots, ranges, error bars, labels), ignoring the background
- Tolerates small layout shifts introduced by the plotting engine (configurable, default 2 pixels)
- Handles different image resolutions by scaling both images onto a common canvas
- Supports multiple image formats: PNG, JPEG, GIF, BMP, TIFF, WebP
- Reports similarity range (min/max) across all images
- Provides per-image similarity scores and an assessment, with links to PR file changes

### PDF Comparison
- Extracts and compares text content from PDFs
- Shows unified diff format for easy review
- Handles added, modified, and removed files

## How It Works

1. **Triggered on Pull Request**: Runs automatically when a PR is opened, updated, or reopened
2. **File Detection**: Identifies all changed image and PDF files
3. **Image Analysis**:
   - Downloads both old and new versions of each image
   - Scales both onto a common canvas if the resolutions differ
   - Estimates the background colour of each image (its dominant colour)
   - Builds a content mask of all pixels that deviate from that background
   - Counts content pixels in one image that have no content pixel in the other image
     within the shift tolerance, and reports the share of matched content
4. **PDF Analysis**:
   - Extracts text from both versions
   - Generates unified diff
5. **Reporting**: Posts results as a PR comment (updates existing comment if present)

## Output Format

The workflow posts a comment to the PR with two sections:

### Image Similarity Section
- Similarity range across all images
- Table with:
  - Image filename (linked to PR file diff)
  - Similarity score (0.0000 to 1.0000)
  - Assessment derived from the score

### PDF Text Comparison Section
- Per-file comparison results
- Expandable diff sections showing text changes
- Clear indication of added/removed files

## Configuration

The workflow is configured in `.github/workflows/compare-images-and-pdfs.yml`

### Workflow Input
- `curve_shift_tolerance_px` (optional, default `2`): maximum displacement in pixels by
  which plotted content may move between two revisions and still count as unchanged.
  Available for `workflow_dispatch` and `workflow_call`; pull request runs use the default.
  It is forwarded to the script as `--curve-shift-tolerance-px`.

### Environment Variables Used
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- `GITHUB_REPOSITORY`: Repository name (owner/repo)
- `PR_NUMBER`: Pull request number

### Python Dependencies
- `Pillow`: Image processing
- `numpy`: Numerical computations
- `scikit-image`: SSIM calculation (fallback metric)
- `pdfplumber`: PDF text extraction
- `requests`: API calls

## Technical Details

### Content-Based Similarity
Scientific plots consist almost entirely of uniform background — typically more than 95 %
of all pixels. A whole-image metric is therefore dominated by pixels that carry no
information, and scientifically very different plots still score above 0.95. The metric
used here removes the background from the calculation:

1. The dominant colour of each image is determined from a coarsely quantised colour
   histogram and taken as the background colour.
2. Every pixel deviating from that background by more than a fixed tolerance in any
   channel is treated as content.
3. A content pixel is considered *matched* if the other image has content within
   `curve_shift_tolerance_px` pixels of it.
4. The score is `1 - unmatched content pixels / total content pixels`, evaluated in both
   directions, and therefore ranges from 0.0 (nothing in common) to 1.0 (identical).

### Shift Tolerance
Plot engines occasionally displace the whole panel content by about one pixel between
runs without any change in the underlying data. Without a tolerance such runs would be
reported as substantial changes. A tolerance of 2 pixels suppresses this rendering noise
while still detecting shifted curves and moved data points.

### Assessment Bands
- `>= 0.99`: identical or rendering noise
- `0.95 - 0.99`: minor change
- `< 0.95`: review required

### Fallback
If an image has no dominant background colour covering at least half of its pixels — for
example a plot with a fully shaded or dark background — the content mask is not
meaningful. In that case the script falls back to whole-image SSIM on the grayscale
versions and marks the score accordingly in the report.

### Resolution Handling
- If images have different resolutions, both are scaled proportionally onto a canvas of
  the larger dimensions, preserving aspect ratio
- Uses LANCZOS resampling for high-quality scaling

### PDF Text Extraction
- Extracts text page by page
- Performs unified diff comparison
- Limits diff output to 500 lines to avoid extremely long comments

## Example Use Case

Perfect for repositories containing:
- Scientific plots and visualizations
- Generated reports with charts
- Documentation with screenshots
- PDF reports with text content

The action helps reviewers quickly identify:
- Whether "changed" images are actually visually different
- What text content changed in PDF files
- Metadata-only changes vs. actual content changes

## Limitations

- Image comparison is visual only (metadata differences ignored)
- Colour changes are only detected where they also change which pixels are background
- Rescaling between revisions introduces resampling differences that slightly lower the score
- PDF comparison is text-based (formatting/layout differences not detected)
- Very large PDFs may have truncated diffs in the report

## Maintenance

### Files
- `.github/workflows/compare-images-and-pdfs.yml`: Workflow definition
- `.github/scripts/compare-images-and-pdfs.py`: Comparison script

### Updating Dependencies
Modify the `pip install` line in the workflow file to update or add dependencies.
