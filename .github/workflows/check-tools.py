import csv
import os
import re
import sys
import requests

TOOLS_REPOS = {
    "ospsuite-R": "Open-Systems-Pharmacology/OSPSuite-R",
    "Reporting Engine": "Open-Systems-Pharmacology/OSPSuite.ReportingEngine",
    "RUtils": "Open-Systems-Pharmacology/OSPSuite.RUtils",
    "TLF": "Open-Systems-Pharmacology/TLF-Library",
    "rSharp": "Open-Systems-Pharmacology/rSharp",
    "Qualification Runner": "Open-Systems-Pharmacology/QualificationRunner",
    "Qualification Framework": "Open-Systems-Pharmacology/QualificationPlan",
    "PK-Sim": "Open-Systems-Pharmacology/PK-Sim",
}

GITHUB_API = "https://api.github.com"

def check_url(url):
    github_token = os.environ.get('GITHUB_TOKEN')
    headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        } if github_token else {}
    try:
        resp = requests.head(url, allow_redirects=True, timeout=10, headers=headers)
        if resp.status_code >= 400:
            return False, f"URL '{url}' returned HTTP status code {resp.status_code}"
        return True, ""
    except Exception as e:
        return False, f"URL '{url}' could not be reached: {e}"

def check_release(repo, version):
    tag = f"v{version}"
    url = f"{GITHUB_API}/repos/{repo}/releases/tags/{tag}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return True, ""
    else:
        return False, f"Release with tag '{tag}' not found in repository '{repo}'"

def check_branch(repo, branch):
    url = f"{GITHUB_API}/repos/{repo}/branches/{branch}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return True, ""
    else:
        return False, f"Branch '{branch}' not found in repository '{repo}'"

def is_version_tag(version):
    # Return True if version matches <major.minor> or <major.minor.patch> (numbers only)
    return re.match(r"^\d+\.\d+(\.\d+)?$", version) is not None

def main():
    errors = []
    file_path = "tools.csv"

    # Check empty lines
    with open(file_path, newline='', encoding="utf-8") as f:
        lines = f.readlines()
        for num, line in enumerate(lines, 1):
            if line.strip() == "":
                errors.append(f"tools.csv: Empty or blank line at line {num}")

    # Read CSV
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader, start=2):  # start=2: header is line 1
            tool = row["Tool"].strip()
            version = row["Version"].strip()
            url = row["URL"].strip()

            if tool not in TOOLS_REPOS:
                continue

            repo = TOOLS_REPOS[tool]

            if url and url != "NA":
                # 1) If URL is present, check it is valid
                ok, msg = check_url(url)
                if not ok:
                    errors.append(f"tools.csv: Row {i} (Tool: {tool}) URL check failed: {msg}")
            else:
                # 2) Check GitHub repo for release or branch
                if not version or version == "NA":
                    errors.append(f"tools.csv: Row {i} (Tool: {tool}) has neither a valid URL nor a Version.")
                    continue

                if is_version_tag(version):
                    ok, msg = check_release(repo, version)
                    if not ok:
                        errors.append(f"tools.csv: Row {i} (Tool: {tool}) release check failed: {msg}")
                else:
                    ok, msg = check_branch(repo, version)
                    if not ok:
                        errors.append(f"tools.csv: Row {i} (Tool: {tool}) branch check failed: {msg}")

    # Print errors and exit
    if errors:
        print("ERRORS FOUND in tools.csv checks:")
        for err in errors:
            print(err)
        sys.exit(1)
    else:
        print("All checks in tools.csv passed.")

if __name__ == "__main__":
    main()
