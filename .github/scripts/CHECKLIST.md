# Quick Start Checklist

Follow these steps to move issues from "No Status" to V12.3 project.

## Prerequisites

- [ ] Python 3.6 or later installed
- [ ] GitHub account with access to Open-Systems-Pharmacology organization
- [ ] Permission to manage GitHub Projects

## Step 1: Create GitHub Token

- [ ] Go to https://github.com/settings/tokens
- [ ] Click "Generate new token (classic)"
- [ ] Give it a name: "Projects Manager" (or similar)
- [ ] Select scopes:
  - [ ] ✅ `repo` (all sub-scopes)
  - [ ] ✅ `project` → `read:project`
  - [ ] ✅ `project` → `write:project`
- [ ] Click "Generate token"
- [ ] Copy the token (you won't see it again!)

## Step 2: Set Up Environment

```bash
# Navigate to the scripts directory
cd .github/scripts

# Set your GitHub token
export GITHUB_TOKEN=paste_your_token_here

# Verify token is set
echo $GITHUB_TOKEN
```

## Step 3: Install Dependencies (Optional)

The `run.sh` script will do this automatically, but you can do it manually:

```bash
pip3 install -r requirements.txt
```

## Step 4: Run Preview (IMPORTANT!)

- [ ] Run the preview to see what will be moved:

```bash
./run.sh
# Choose option 1: Preview
```

OR directly:

```bash
python3 github_projects_manager.py preview
```

- [ ] Review the output carefully
- [ ] Verify the correct issues are listed
- [ ] Confirm V12.3 is the target project
- [ ] Check that issue details look correct

## Step 5: Review Preview Output

Verify the preview shows:
- [ ] Total count of issues with "No Status"
- [ ] Issue numbers and titles
- [ ] Current project for each issue
- [ ] Issue state (OPEN/CLOSED)
- [ ] GitHub URLs for each issue
- [ ] Target project name (V12.3)

## Step 6: Execute Move (If Preview Looks Good)

- [ ] Run the move command:

```bash
./run.sh
# Choose option 2: Move
```

OR directly:

```bash
python3 github_projects_manager.py move
```

- [ ] Review the preview shown again
- [ ] Type `yes` when prompted to confirm
- [ ] Wait for the script to process all issues
- [ ] Review the summary (successfully moved vs failed)

## Step 7: Verify in GitHub

- [ ] Go to the V12.3 project in GitHub
- [ ] Verify issues were added
- [ ] Manually update issue statuses if needed (they'll still show "No Status")

## Troubleshooting

### If preview shows no issues:
✅ Great! No issues have "No Status" - nothing to move

### If you see "GITHUB_TOKEN not set":
```bash
export GITHUB_TOKEN=your_token_here
echo $GITHUB_TOKEN  # verify it's set
```

### If you see "HTTP 401" or "HTTP 403":
- Your token may not have the right permissions
- Create a new token with `repo` and `project` scopes

### If you see "Could not find project 'V12.3'":
- Check the project name in the preview output
- The project might be named differently
- You might not have access to the project

### If some issues fail to move:
- Check the error message for each failed issue
- Issues might already be in V12.3
- There might be API rate limiting (wait and try again)

## Expected Timeline

- Preview: 10-30 seconds (depending on number of projects)
- Move: 2-5 seconds per issue

## Safety Notes

✅ **Preview mode makes NO changes** - always safe to run
✅ **Move mode requires confirmation** - you'll be asked before any changes
✅ **Issues stay in original projects** - they're added to V12.3, not removed from current
✅ **Status doesn't change** - you'll need to manually update from "No Status"
✅ **Each issue independent** - if one fails, others still process

## Quick Reference

| Command | Purpose |
|---------|---------|
| `./run.sh` | Interactive menu |
| `python3 github_projects_manager.py preview` | Preview only |
| `python3 github_projects_manager.py move` | Move with confirmation |
| `export GITHUB_TOKEN=...` | Set authentication |

## Need Help?

See the detailed documentation:
- `README.md` - Main documentation with examples
- `README_PROJECTS.md` - Technical API details
- `WORKFLOW.md` - Visual diagrams and flow
- `PREVIEW_OUTPUT.md` - Example outputs
- `SUMMARY.md` - Complete overview

## Success Criteria

You're done when:
- [ ] Preview ran successfully and showed the expected issues
- [ ] Move operation completed successfully
- [ ] Summary shows all issues moved (0 failed)
- [ ] Issues appear in V12.3 project in GitHub UI
- [ ] (Optional) Issue statuses updated manually if needed

## Post-Move Actions

After moving issues to V12.3:
1. Go to the V12.3 project in GitHub
2. For each moved issue, update its status from "No Status" to appropriate value
3. Consider adding labels or assignees
4. Update issue descriptions if needed

---

**Remember**: Always run preview first! It shows exactly what will happen with no risk.
