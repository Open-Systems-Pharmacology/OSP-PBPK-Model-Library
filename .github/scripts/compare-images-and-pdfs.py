#!/usr/bin/env python3
"""
Script to compare images and PDFs in a pull request.
Performs visual comparison of images using SSIM and text comparison of PDFs.
"""

import os
import sys
import json
import requests
from io import BytesIO
from typing import List, Dict, Tuple, Any
import difflib

# Image processing imports
try:
    from PIL import Image
    import numpy as np
    from skimage.metrics import structural_similarity as ssim
except ImportError as e:
    print(f"Error importing required libraries: {e}")
    print("Please ensure Pillow, numpy, and scikit-image are installed")
    sys.exit(1)

# PDF processing imports
try:
    import pdfplumber
except ImportError:
    print("Warning: pdfplumber not installed. PDF comparison will be skipped.")
    pdfplumber = None


# Timeout (in seconds) applied to every network request so the script fails
# fast instead of hanging indefinitely on network issues.
REQUEST_TIMEOUT = 30


class ImagePDFComparator:
    """Compares images and PDFs from a pull request"""

    def __init__(self):
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.repo = os.environ.get('GITHUB_REPOSITORY')
        self.pr_number = os.environ.get('PR_NUMBER')

        if not all([self.github_token, self.repo, self.pr_number]):
            raise ValueError("Missing required environment variables: GITHUB_TOKEN, GITHUB_REPOSITORY, PR_NUMBER")

        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        self.base_url = f'https://api.github.com/repos/{self.repo}'
        self._base_sha = None

    def get_pr_files(self) -> List[Dict[str, Any]]:
        """Get list of changed files in the PR.

        Paginates through every page of the files endpoint so large PRs do not
        silently miss changed files.
        """
        url = f'{self.base_url}/pulls/{self.pr_number}/files'
        files: List[Dict[str, Any]] = []
        page = 1

        while True:
            response = requests.get(
                url,
                headers=self.headers,
                params={'per_page': 100, 'page': page},
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code != 200:
                raise Exception(f"Failed to fetch PR files: {response.status_code} {response.text}")

            batch = response.json()
            if not batch:
                break

            files.extend(batch)
            page += 1

        return files

    def download_file(self, url: str) -> bytes:
        """Download a file from a URL"""
        response = requests.get(url, headers=self.headers, timeout=REQUEST_TIMEOUT)

        if response.status_code == 404:
            raise FileNotFoundError(f"File not found at {url}")

        if response.status_code != 200:
            raise Exception(f"Failed to download file from {url}: {response.status_code}")

        return response.content

    def get_base_sha(self) -> str:
        """Return the PR base SHA, fetching PR data only once per run."""
        if self._base_sha is None:
            pr_data = self.get_pr_data()
            self._base_sha = pr_data['base']['sha']
        return self._base_sha

    def normalize_image_size(self, img1: Image.Image, img2: Image.Image) -> Tuple[np.ndarray, np.ndarray]:
        """Normalize two images to the same size and convert to grayscale"""
        # Convert to RGB if needed (to handle different modes)
        if img1.mode != 'RGB':
            img1 = img1.convert('RGB')
        if img2.mode != 'RGB':
            img2 = img2.convert('RGB')

        # Get dimensions
        w1, h1 = img1.size
        w2, h2 = img2.size

        # Use a common canvas sized to the larger dimensions. Each image is
        # scaled proportionally to fit within that canvas and then padded
        # (letterboxed) so aspect ratios are preserved and SSIM is not skewed
        # by non-uniform stretching.
        target_width = max(w1, w2)
        target_height = max(h1, h2)

        def fit_to_canvas(img: Image.Image) -> Image.Image:
            w, h = img.size
            scale = min(target_width / w, target_height / h)
            new_size = (max(1, round(w * scale)), max(1, round(h * scale)))
            resized = img.resize(new_size, Image.LANCZOS)
            canvas = Image.new('RGB', (target_width, target_height), (255, 255, 255))
            offset = ((target_width - new_size[0]) // 2,
                      (target_height - new_size[1]) // 2)
            canvas.paste(resized, offset)
            return canvas

        img1_resized = fit_to_canvas(img1)
        img2_resized = fit_to_canvas(img2)

        # Convert to grayscale numpy arrays
        img1_gray = np.array(img1_resized.convert('L'))
        img2_gray = np.array(img2_resized.convert('L'))

        return img1_gray, img2_gray

    def compare_images(self, file_info: Dict[str, Any]) -> Dict[str, Any]:
        """Compare two versions of an image using SSIM"""
        filename = file_info['filename']

        try:
            # Download both versions
            if file_info['status'] == 'removed':
                return {
                    'filename': filename,
                    'status': 'removed',
                    'similarity': None,
                    'error': None
                }
            elif file_info['status'] == 'added':
                return {
                    'filename': filename,
                    'status': 'added',
                    'similarity': None,
                    'error': None
                }

            # For modified files, compare old and new versions
            raw_url = file_info.get('raw_url')
            if not raw_url:
                return {
                    'filename': filename,
                    'status': file_info['status'],
                    'similarity': None,
                    'error': 'No raw URL available'
                }

            # Get the new version
            new_content = self.download_file(raw_url)
            new_img = Image.open(BytesIO(new_content))

            # Get the old version (from previous commit). For renamed files the
            # previous content lives under previous_filename, so use that when
            # present to avoid comparing against a 404.
            old_filename = file_info.get('previous_filename') or filename
            base_sha = self.get_base_sha()

            old_url = f"https://raw.githubusercontent.com/{self.repo}/{base_sha}/{old_filename}"
            try:
                old_content = self.download_file(old_url)
                old_img = Image.open(BytesIO(old_content))
            except FileNotFoundError:
                # The old file genuinely does not exist, so treat it as added.
                # Auth, rate-limit, and network errors are left to surface.
                return {
                    'filename': filename,
                    'status': 'added',
                    'similarity': None,
                    'error': None
                }

            # Normalize and compare
            img1_gray, img2_gray = self.normalize_image_size(old_img, new_img)

            # Calculate SSIM
            similarity_score = ssim(img1_gray, img2_gray)

            return {
                'filename': filename,
                'status': file_info['status'],
                'similarity': similarity_score,
                'error': None
            }

        except Exception as e:
            return {
                'filename': filename,
                'status': file_info.get('status', 'unknown'),
                'similarity': None,
                'error': str(e)
            }

    def extract_pdf_text(self, pdf_content: bytes) -> str:
        """Extract text from a PDF"""
        if pdfplumber is None:
            return ""

        try:
            with pdfplumber.open(BytesIO(pdf_content)) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        except Exception as e:
            raise Exception(f"Failed to extract PDF text: {str(e)}")

    def compare_pdfs(self, file_info: Dict[str, Any]) -> Dict[str, Any]:
        """Compare text content of two PDF versions"""
        filename = file_info['filename']

        if pdfplumber is None:
            return {
                'filename': filename,
                'status': file_info['status'],
                'differences': [],
                'error': 'pdfplumber not available'
            }

        try:
            if file_info['status'] == 'removed':
                return {
                    'filename': filename,
                    'status': 'removed',
                    'differences': ['File was removed'],
                    'error': None
                }
            elif file_info['status'] == 'added':
                return {
                    'filename': filename,
                    'status': 'added',
                    'differences': ['File was added'],
                    'error': None
                }

            # For modified files
            raw_url = file_info.get('raw_url')
            if not raw_url:
                return {
                    'filename': filename,
                    'status': file_info['status'],
                    'differences': [],
                    'error': 'No raw URL available'
                }

            # Get new version
            new_content = self.download_file(raw_url)
            new_text = self.extract_pdf_text(new_content)

            # Get old version. For renamed files the previous content lives
            # under previous_filename, so use that when present.
            old_filename = file_info.get('previous_filename') or filename
            base_sha = self.get_base_sha()
            old_url = f"https://raw.githubusercontent.com/{self.repo}/{base_sha}/{old_filename}"

            try:
                old_content = self.download_file(old_url)
                old_text = self.extract_pdf_text(old_content)
            except FileNotFoundError:
                # The old file genuinely does not exist, so treat it as added.
                # Auth, rate-limit, and network errors are left to surface.
                return {
                    'filename': filename,
                    'status': 'added',
                    'differences': ['File was added'],
                    'error': None
                }

            # Compare texts
            old_lines = old_text.splitlines(keepends=True)
            new_lines = new_text.splitlines(keepends=True)

            diff = list(difflib.unified_diff(old_lines, new_lines,
                                            fromfile=f'a/{filename}',
                                            tofile=f'b/{filename}',
                                            lineterm=''))

            return {
                'filename': filename,
                'status': file_info['status'],
                'differences': diff if diff else ['No differences found'],
                'error': None
            }

        except Exception as e:
            return {
                'filename': filename,
                'status': file_info.get('status', 'unknown'),
                'differences': [],
                'error': str(e)
            }

    def get_pr_data(self) -> Dict[str, Any]:
        """Get PR data including base and head SHA"""
        url = f'{self.base_url}/pulls/{self.pr_number}'
        response = requests.get(url, headers=self.headers, timeout=REQUEST_TIMEOUT)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch PR data: {response.status_code}")

        return response.json()

    def format_report(self, image_results: List[Dict], pdf_results: List[Dict]) -> str:
        """Format the comparison results as a markdown report"""
        report = "# Image and PDF Comparison Report\n\n"

        # Image similarity section
        if image_results:
            report += "## Image Similarity\n\n"

            # Calculate min/max similarity
            similarities = [r['similarity'] for r in image_results if r['similarity'] is not None]

            if similarities:
                min_sim = min(similarities)
                max_sim = max(similarities)
                report += f"**Similarity Range:** {min_sim:.4f} - {max_sim:.4f}\n\n"
            else:
                report += "**No valid similarity scores calculated**\n\n"

            # Table of results
            report += "| Image | Similarity Score |\n"
            report += "|-------|------------------|\n"

            # Sort by similarity (low to high), with None values first
            sorted_image_results = sorted(
                image_results,
                key=lambda r: (r['similarity'] is not None, r['similarity'] if r['similarity'] is not None else 0)
            )

            for result in sorted_image_results:
                filename = result['filename']
                pr_file_url = f"https://github.com/{self.repo}/pull/{self.pr_number}/files#diff-{self.get_file_hash(filename)}"

                if result['similarity'] is not None:
                    sim_display = f"{result['similarity']:.4f}"
                elif result['status'] in ['added', 'removed']:
                    sim_display = f"N/A ({result['status']})"
                else:
                    sim_display = f"Error: {result.get('error', 'Unknown')}"

                report += f"| [{filename}]({pr_file_url}) | {sim_display} |\n"

            report += "\n"
        else:
            report += "## Image Similarity\n\nNo image files were changed in this PR.\n\n"

        # PDF comparison section
        if pdf_results:
            report += "## PDF Text Comparison\n\n"

            for result in pdf_results:
                filename = result['filename']
                report += f"### {filename}\n\n"

                if result.get('error'):
                    report += f"**Error:** {result['error']}\n\n"
                    continue

                differences = result.get('differences', [])

                if differences == ['No differences found']:
                    report += "✅ No text differences found\n\n"
                elif differences == ['File was added']:
                    report += "➕ File was added in this PR\n\n"
                elif differences == ['File was removed']:
                    report += "➖ File was removed in this PR\n\n"
                else:
                    report += "<details>\n<summary>Text Differences (click to expand)</summary>\n\n"
                    report += "```diff\n"
                    # Limit the diff output to avoid extremely long comments
                    diff_lines = differences[:500]  # Limit to 500 lines
                    if len(differences) > 500:
                        report += '\n'.join(diff_lines)
                        report += f"\n... (truncated {len(differences) - 500} lines)\n"
                    else:
                        report += '\n'.join(diff_lines)
                    report += "\n```\n\n"
                    report += "</details>\n\n"
        else:
            report += "## PDF Text Comparison\n\nNo PDF files were changed in this PR.\n\n"

        return report

    def get_file_hash(self, filename: str) -> str:
        """Return the GitHub diff anchor hash for a file.

        GitHub builds the `#diff-<hash>` anchor on the Files Changed view from
        the SHA256 digest of the file path. Returning the full digest keeps the
        anchor links working instead of navigating to the generic Files Changed
        view.
        """
        import hashlib
        return hashlib.sha256(filename.encode()).hexdigest()

    def write_job_summary(self, comment_body: str):
        """Write the report to the GitHub Actions job summary if available.

        This keeps the results visible even when the workflow cannot post a
        comment to the PR (for example when it runs with a read-only token).
        """
        summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
        if not summary_path:
            return

        try:
            with open(summary_path, 'a', encoding='utf-8') as summary_file:
                summary_file.write(comment_body + "\n")
            print("Wrote comparison report to the job summary")
        except OSError as e:
            print(f"Warning: failed to write job summary: {e}")

    def post_pr_comment(self, comment_body: str) -> bool:
        """Post (or update) a comment on the PR.

        Returns True when the comment was posted/updated successfully and
        False when the API rejected the request because the token is not
        permitted to write comments (this happens for pull requests opened
        from forks when the workflow runs with a read-only GITHUB_TOKEN).
        Any other failure is raised so it is surfaced to the caller.
        """
        url = f'{self.base_url}/issues/{self.pr_number}/comments'

        # Check if we already posted a comment. Paginate through all issue
        # comments so older bot comments are found and updated instead of
        # posting a duplicate.
        existing_comments_url = f'{self.base_url}/issues/{self.pr_number}/comments'
        comment_marker = "# Image and PDF Comparison Report"
        existing_comment_id = None
        page = 1

        while existing_comment_id is None:
            response = requests.get(
                existing_comments_url,
                headers=self.headers,
                params={'per_page': 100, 'page': page},
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code != 200:
                break

            batch = response.json()
            if not batch:
                break

            for comment in batch:
                if comment_marker in comment.get('body', ''):
                    existing_comment_id = comment['id']
                    break

            page += 1

        # Update existing comment or create new one
        if existing_comment_id:
            update_url = f'{self.base_url}/issues/comments/{existing_comment_id}'
            response = requests.patch(update_url,
                                     headers=self.headers,
                                     json={'body': comment_body},
                                     timeout=REQUEST_TIMEOUT)
        else:
            response = requests.post(url,
                                    headers=self.headers,
                                    json={'body': comment_body},
                                    timeout=REQUEST_TIMEOUT)

        if response.status_code in (401, 403):
            # The token is not allowed to write comments. This is expected for
            # pull requests from forks running with a read-only token, so treat
            # it as a non-fatal condition instead of failing the whole job.
            print(
                "Warning: not permitted to post a PR comment "
                f"({response.status_code} {response.text}). "
                "Skipping comment; see the job summary for the report."
            )
            return False

        if response.status_code not in (200, 201):
            raise Exception(f"Failed to post comment: {response.status_code} {response.text}")

        print("Successfully posted comment to PR")
        return True

    def run(self):
        """Main execution function"""
        print(f"Analyzing PR #{self.pr_number} in {self.repo}")

        # Get changed files
        files = self.get_pr_files()
        print(f"Found {len(files)} changed files")

        # Filter image and PDF files
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
        pdf_extension = '.pdf'

        image_files = []
        pdf_files = []

        for file_info in files:
            filename = file_info['filename'].lower()
            if any(filename.endswith(ext) for ext in image_extensions):
                image_files.append(file_info)
            elif filename.endswith(pdf_extension):
                pdf_files.append(file_info)

        print(f"Found {len(image_files)} image files and {len(pdf_files)} PDF files")

        # Compare images
        image_results = []
        for i, file_info in enumerate(image_files, 1):
            print(f"Comparing image {i}/{len(image_files)}: {file_info['filename']}")
            result = self.compare_images(file_info)
            image_results.append(result)

        # Compare PDFs
        pdf_results = []
        for i, file_info in enumerate(pdf_files, 1):
            print(f"Comparing PDF {i}/{len(pdf_files)}: {file_info['filename']}")
            result = self.compare_pdfs(file_info)
            pdf_results.append(result)

        # Generate report
        report = self.format_report(image_results, pdf_results)

        # Always make the report available in the job summary, then try to post
        # it as a PR comment. A missing comment permission must not fail the job.
        self.write_job_summary(report)
        self.post_pr_comment(report)

        print("\n" + "="*50)
        print("Comparison complete!")
        print("="*50)


def main():
    """Main entry point"""
    try:
        comparator = ImagePDFComparator()
        comparator.run()
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
