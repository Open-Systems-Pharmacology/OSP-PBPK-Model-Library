# Moving Issues from "No Status" to V12.3 Project

## Quick Start

The fastest way to preview and move issues:

```bash
cd .github/scripts

# Set your GitHub token
export GITHUB_TOKEN=your_personal_access_token_here

# Run the interactive script
./run.sh
```

## What This Does

This tool helps you manage GitHub Projects v2 by:

1. **Finding all issues** with "No Status" status across all organization projects
2. **Previewing** which issues would be affected
3. **Moving issues** to the V12.3 project (with confirmation)

## Files Included

- **`github_projects_manager.py`** - Main Python script using GitHub GraphQL API
- **`run.sh`** - Interactive shell script for easy execution
- **`requirements.txt`** - Python dependencies
- **`README_PROJECTS.md`** - Detailed documentation
- **`PREVIEW_OUTPUT.md`** - Expected output format

## Step-by-Step Guide

### 1. Create a GitHub Personal Access Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Projects Manager")
4. Select scopes:
   - ✅ `repo` (all sub-scopes)
   - ✅ `project` (read:project, write:project)
5. Click "Generate token"
6. Copy the token immediately (you won't see it again!)

### 2. Set the Token

```bash
export GITHUB_TOKEN=ghp_your_token_here
```

> **Tip:** Add this to your `~/.bashrc` or `~/.zshrc` if you'll use it frequently

### 3. Run the Preview (Recommended First)

```bash
cd .github/scripts
python3 github_projects_manager.py preview
```

This will show you:
- All organization projects
- The V12.3 target project
- All issues currently marked as "No Status"
- Which project each issue is currently in

**Example output:**
```
Found 3 issue(s) with 'No Status'

Issue #170: Use folder name in `create-reports.yml`
  Current Project: Project A
  State: OPEN
  URL: https://github.com/...

These issues would be moved to project: V12.3
```

### 4. Move the Issues

After reviewing the preview:

```bash
python3 github_projects_manager.py move
```

The script will:
1. Show the preview again
2. Ask for confirmation: `Do you want to proceed with moving these issues? (yes/no):`
3. Move each issue to V12.3
4. Show a summary of successes and failures

### 5. Alternative: Use the Interactive Script

```bash
./run.sh
```

This will:
- Check prerequisites (Python, pip, requirements)
- Verify your GitHub token is set
- Present a menu to choose preview or move mode

## Understanding the Output

### Preview Mode

```
GitHub Projects Manager - Preview Mode
============================================================
Fetching projects for organization: Open-Systems-Pharmacology

Found 5 projects:
  - Project A (#1)
  - V12.3 (#3)
  - Project C (#5)

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
PREVIEW: Found 2 issue(s) with 'No Status'
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

### Move Mode

```
Moving 2 issues to project: V12.3
============================================================

Processing Issue #170: Use folder name in `create-reports.yml`
  ✓ Added to project V12.3

Processing Issue #161: On pull_request workflows are not triggered
  ✓ Added to project V12.3

============================================================
Summary:
  Successfully moved: 2
  Failed: 0
============================================================
```

## Important Notes

### What Happens

✅ **Issues ARE added to V12.3 project**
❌ **Issues are NOT removed from their current project** (GitHub allows issues to be in multiple projects)
❌ **Status does NOT change automatically** (issues will still show "No Status" until manually updated)

### Safety Features

- **Preview first**: Always see what will happen before making changes
- **Confirmation required**: Move mode asks for explicit confirmation
- **Independent operations**: If one issue fails, others continue processing
- **Detailed logging**: See exactly what's happening at each step

### Limitations

- Processes up to 100 projects (can be increased if needed)
- Processes up to 100 items per project per page (handles pagination)
- Only adds issues to V12.3, doesn't remove from source projects
- Requires manual status updates after moving

## Troubleshooting

### "GITHUB_TOKEN environment variable is not set"

```bash
export GITHUB_TOKEN=your_token_here
```

Make sure you've created and set a Personal Access Token.

### "Error: HTTP 401" or "Error: HTTP 403"

Your token doesn't have the required permissions. Create a new token with:
- `repo` scope (full control)
- `project` scope (read and write)

### "Could not find project 'V12.3'"

The project might:
- Not exist yet
- Have a different name (check the projects list in the output)
- Not be accessible with your token

### Script Hangs or Times Out

- You might be rate-limited by GitHub API
- Check your network connection
- Try again in a few minutes

### No Issues Found with "No Status"

This is good news! Either:
- All issues have been assigned a status
- Issues haven't been added to any projects yet
- The "Status" field might be named differently

## For Developers

### Script Architecture

The script uses:
- **GitHub GraphQL API v4** for Projects v2
- **Python 3.6+** with `requests` library
- **Paginated queries** to handle large datasets
- **Error handling** for resilience

### Key Functions

- `get_organization_projects()` - Fetches all org projects
- `get_project_items()` - Gets all items in a project with pagination
- `get_project_fields()` - Retrieves field definitions
- `add_item_to_project()` - Adds an issue to a project
- `preview_issues_to_move()` - Shows what would be moved
- `move_issues_to_project()` - Performs the actual move

### Extending the Script

To modify the script:

1. **Change target project**: Edit the project name in the search logic
2. **Filter by status**: Modify the status check in `get_project_items()`
3. **Update status after moving**: Add a call to `update_item_field()` after moving
4. **Export results**: Add CSV export functionality

## Additional Resources

- [GitHub Projects v2 API Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects)
- [GitHub GraphQL API Explorer](https://docs.github.com/en/graphql/overview/explorer)
- [Creating GitHub Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review the detailed documentation in `README_PROJECTS.md`
3. Check the example output in `PREVIEW_OUTPUT.md`
4. Open an issue in the repository

## License

This script is part of the OSP-PBPK-Model-Library repository.
