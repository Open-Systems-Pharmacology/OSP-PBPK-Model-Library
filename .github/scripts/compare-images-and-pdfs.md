# Image and PDF Comparison GitHub Action

## Overview

This GitHub Action automatically compares images and PDFs in pull requests, providing:
- Visual similarity metrics for images using SSIM (Structural Similarity Index)
- Text comparison for PDF files

## Features

### Image Comparison
- Compares images visually using SSIM algorithm (0 = completely different, 1 = identical)
- Handles different image resolutions by scaling to a common size
- Supports multiple image formats: PNG, JPEG, GIF, BMP, TIFF, WebP
- Reports similarity range (min/max) across all images
- Provides per-image similarity scores with links to PR file changes

### PDF Comparison
- Extracts and compares text content from PDFs
- Shows unified diff format for easy review
- Handles added, modified, and removed files

## How It Works

1. **Triggered on Pull Request**: Runs automatically when a PR is opened, updated, or reopened
2. **File Detection**: Identifies all changed image and PDF files
3. **Image Analysis**:
   - Downloads both old and new versions of each image
   - Normalizes to the same resolution if needed
   - Converts to grayscale for comparison
   - Calculates SSIM score
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

### PDF Text Comparison Section
- Per-file comparison results
- Expandable diff sections showing text changes
- Clear indication of added/removed files

## Configuration

The workflow is configured in `.github/workflows/compare-images-and-pdfs.yml`

### Environment Variables Used
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- `GITHUB_REPOSITORY`: Repository name (owner/repo)
- `PR_NUMBER`: Pull request number

### Python Dependencies
- `Pillow`: Image processing
- `numpy`: Numerical computations
- `scikit-image`: SSIM calculation
- `pdfplumber`: PDF text extraction
- `requests`: API calls

## Technical Details

### SSIM (Structural Similarity Index)
- Perceptual metric that quantifies image quality degradation
- Considers luminance, contrast, and structure
- Range: 0.0 (completely different) to 1.0 (identical)
- More accurate than simple pixel-by-pixel comparison for visual perception

### Resolution Handling
- If images have different resolutions, both are scaled to the larger dimensions
- Uses LANCZOS resampling for high-quality scaling
- Comparison is performed on grayscale versions

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
- PDF comparison is text-based (formatting/layout differences not detected)
- Very large PDFs may have truncated diffs in the report

## Maintenance

### Files
- `.github/workflows/compare-images-and-pdfs.yml`: Workflow definition
- `.github/scripts/compare-images-and-pdfs.py`: Comparison script

### Updating Dependencies
Modify the `pip install` line in the workflow file to update or add dependencies.
