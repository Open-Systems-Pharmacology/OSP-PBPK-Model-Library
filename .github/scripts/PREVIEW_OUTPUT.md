# Preview: Issues to Move from "No Status" to V12.3

This document shows the expected output when running the `github_projects_manager.py` script.

## How to Run

To see the actual preview and move issues, you need to:

1. **Set up authentication:**
   ```bash
   export GITHUB_TOKEN=your_personal_access_token
   ```

2. **Run the preview:**
   ```bash
   cd .github/scripts
   python3 github_projects_manager.py preview
   ```

3. **Move issues (after reviewing preview):**
   ```bash
   python3 github_projects_manager.py move
   ```

## Expected Preview Output

The script will query the GitHub Projects v2 API to:

1. **Find all organization projects**
2. **Locate the V12.3 project**
3. **Search all projects for issues with "No Status" status**
4. **Display a list of affected issues**

### Sample Output Format

```
GitHub Projects Manager - Preview Mode
============================================================
Fetching projects for organization: Open-Systems-Pharmacology

Found X projects:
  - [Project Name 1] (#1)
  - [Project Name 2] (#2)
  - V12.3 (#N)
  - [Project Name N] (#N)

✓ Found target project: V12.3
  URL: https://github.com/orgs/Open-Systems-Pharmacology/projects/N

============================================================
Searching for issues with 'No Status' across all projects...
============================================================

Checking project: [Project Name]
  Found X items in project

[For each project with items]

============================================================
PREVIEW: Found X issue(s) with 'No Status'
============================================================

Issue #NNN: [Issue Title]
  Current Project: [Current Project Name]
  State: [OPEN/CLOSED]
  URL: [GitHub Issue URL]

[Repeated for each issue]

============================================================
These issues would be moved to project: V12.3
============================================================
```

## What Happens When Moving

When you run the script in "move" mode:

1. Shows the preview (same as above)
2. Asks for confirmation: `Do you want to proceed with moving these issues? (yes/no):`
3. If confirmed, for each issue:
   - Gets the issue's GitHub global ID
   - Adds the issue to the V12.3 project
   - Reports success or failure
4. Shows a summary of moved and failed issues

## Notes

- Issues are **added** to V12.3 project (not removed from their current project)
- The "No Status" status will remain until manually changed
- Each issue move is independent - if one fails, others will still be processed
- The script handles pagination for projects with many items

## Safety

The script includes several safety features:

✓ Preview mode shows exactly what will happen before making changes
✓ Move mode requires explicit confirmation
✓ Each operation is wrapped in error handling
✓ Detailed logging shows progress and any issues

## Running Without Authentication

If you try to run without setting `GITHUB_TOKEN`, you'll see:

```
Error: GITHUB_TOKEN environment variable is not set

To run this script:
1. Create a GitHub Personal Access Token with 'repo' and 'project' scopes
2. Set the environment variable: export GITHUB_TOKEN=your_token_here
3. Run the script again
```

## Token Requirements

Your GitHub Personal Access Token needs:
- `repo` scope (full control of private repositories)
- `project` scope (read:project and write:project)

Create a token at: https://github.com/settings/tokens
