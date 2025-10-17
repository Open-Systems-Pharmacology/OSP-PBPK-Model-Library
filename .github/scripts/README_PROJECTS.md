# GitHub Projects Issue Management

This directory contains a script for managing GitHub Projects v2 issues, specifically for moving issues from the "No Status" column to a target project.

## Purpose

This tool addresses the need to bulk move issues from the "No Status" status column to a specific project (V12.3) in the GitHub Projects interface.

## Prerequisites

1. **GitHub Personal Access Token** with the following scopes:
   - `repo` - Full control of private repositories
   - `project` - Full control of projects (read:project and write:project)

2. **Python 3.6+** with the `requests` library:
   ```bash
   pip install requests
   ```

## Creating a GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select the following scopes:
   - `repo` (all sub-scopes)
   - `project` (read:project, write:project)
4. Generate the token and copy it immediately (you won't be able to see it again)

## Usage

### Preview Mode (Recommended First Step)

Preview which issues would be affected without making any changes:

```bash
export GITHUB_TOKEN=your_token_here
python3 github_projects_manager.py preview
```

This will:
- List all organization projects
- Find the "V12.3" project
- Search all projects for issues with "No Status" status
- Display a list of issues that would be moved

### Move Mode

After reviewing the preview, move the issues:

```bash
export GITHUB_TOKEN=your_token_here
python3 github_projects_manager.py move
```

This will:
- Show the preview again
- Ask for confirmation
- Move the issues to the V12.3 project

## How It Works

The script uses the GitHub GraphQL API (Projects v2) to:

1. **Query Organization Projects**: Fetches all projects in the Open-Systems-Pharmacology organization
2. **Identify Target Project**: Locates the "V12.3" project
3. **Search for "No Status" Issues**: Iterates through all projects to find items with "No Status" status
4. **Move Issues**: Adds issues to the target project (V12.3)

## Example Output

### Preview Mode Output

```
GitHub Projects Manager - Preview Mode
============================================================
Fetching projects for organization: Open-Systems-Pharmacology

Found 5 projects:
  - Project A (#1)
  - Project B (#2)
  - V12.3 (#3)
  - Project D (#4)
  - Project E (#5)

✓ Found target project: V12.3
  URL: https://github.com/orgs/Open-Systems-Pharmacology/projects/3

============================================================
Searching for issues with 'No Status' across all projects...
============================================================

Checking project: Project A
  Found 10 items in project

Checking project: V12.3
  Found 5 items in project

============================================================
PREVIEW: Found 3 issue(s) with 'No Status'
============================================================

Issue #170: Use folder name in `create-reports.yml`
  Current Project: Project A
  State: OPEN
  URL: https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/issues/170

Issue #161: On pull_request workflows are not triggered
  Current Project: Project A
  State: OPEN
  URL: https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/issues/161

============================================================
These issues would be moved to project: V12.3
============================================================
```

## Troubleshooting

### "GITHUB_TOKEN environment variable is not set"

Make sure you've exported the token:
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

### "Error: HTTP 401" or "Error: HTTP 403"

Your token may not have the required permissions. Ensure your personal access token has:
- `repo` scope
- `project` scope (read:project and write:project)

### "Could not find project 'V12.3'"

The script looks for projects with "V12.3" in the title. Make sure:
- The project exists
- The project is accessible with your token
- The project name matches exactly (case-sensitive)

## Safety Features

- **Preview First**: The script always shows what will be moved before making changes
- **Confirmation Required**: In move mode, the script asks for confirmation before proceeding
- **Error Handling**: Each issue move is wrapped in error handling; failures won't stop other issues from being processed

## Limitations

- The script only adds issues to the target project; it does not remove them from the source project
- Issues must already exist in some project with "No Status" status
- The script processes up to 100 projects and 100 items per project (can be extended if needed)

## Repository Structure

```
.
├── github_projects_manager.py  # Main script
└── README_PROJECTS.md          # This file
```

## Technical Details

### GitHub Projects v2 API

The script uses the GitHub GraphQL API (Projects v2), which is the newer version of GitHub Projects. Key differences from Projects v1 (Classic):

- Uses GraphQL instead of REST API
- Different data model (fields, options, items)
- More flexible querying and filtering

### GraphQL Queries Used

1. **Get Organization Projects**: Fetches all projects for an organization
2. **Get Project Items**: Retrieves all items (issues, PRs) in a project with their field values
3. **Get Project Fields**: Gets field definitions (including Status field and its options)
4. **Add Item to Project**: Adds an issue to a project
5. **Update Item Field**: Updates a field value (like Status) for a project item

## Future Enhancements

Possible improvements:
- Add support for filtering by specific projects
- Support for updating status after moving (e.g., set to "In Progress")
- Batch processing with progress indicators
- Export to CSV for record-keeping
- Support for moving between specific status columns
