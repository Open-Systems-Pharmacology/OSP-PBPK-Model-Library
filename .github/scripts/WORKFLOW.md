# GitHub Projects Issue Migration Workflow

## Visual Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Start: User Request                       │
│       "Move all issues from 'No Status' to V12.3"          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 1: Authentication Setup                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 1. Create GitHub Personal Access Token              │   │
│  │    - Go to GitHub Settings → Tokens                 │   │
│  │    - Scopes: repo, project                          │   │
│  │ 2. Export token: export GITHUB_TOKEN=...            │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 2: Run Preview Mode                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ./run.sh  OR  python3 github_projects_manager.py    │   │
│  │                preview                               │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                    │
│         Queries GitHub GraphQL API                          │
│                         │                                    │
│     ┌───────────────────┴───────────────────┐              │
│     ▼                   ▼                   ▼              │
│  Get Org         Get All Items        Find Issues          │
│  Projects        in Each Project      with "No Status"     │
│                                                             │
│  Output:                                                    │
│  ┌────────────────────────────────────────────────────┐   │
│  │ Issue #170: Use folder name in create-reports.yml  │   │
│  │   Current Project: Project A                       │   │
│  │   State: OPEN                                      │   │
│  │   URL: https://github.com/...                      │   │
│  │                                                    │   │
│  │ Issue #161: On pull_request workflows...          │   │
│  │   Current Project: Project A                       │   │
│  │   State: OPEN                                      │   │
│  │   URL: https://github.com/...                      │   │
│  │                                                    │   │
│  │ These issues would be moved to project: V12.3      │   │
│  └────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 3: Review Preview                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ User reviews the list of issues that will be moved  │   │
│  │                                                      │   │
│  │ Decision Point:                                      │   │
│  │   ✅ Looks good → Proceed to Step 4                │   │
│  │   ❌ Not ready → Stop, no changes made             │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              Step 4: Execute Move                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ python3 github_projects_manager.py move              │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                    │
│            Shows preview again                               │
│                         │                                    │
│                         ▼                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Confirmation: Do you want to proceed? (yes/no)       │   │
│  └─────────────────────────────────────────────────────┘   │
│            │                        │                        │
│            │ yes                    │ no                     │
│            ▼                        ▼                        │
│  ┌────────────────┐      ┌────────────────┐               │
│  │ Process Issues  │      │ Cancel & Exit   │               │
│  └────────────────┘      └────────────────┘               │
│            │                                                 │
│            ▼                                                 │
│  For each issue:                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 1. Get issue global ID                              │   │
│  │ 2. Add to V12.3 project                             │   │
│  │ 3. Report success/failure                           │   │
│  └─────────────────────────────────────────────────────┘   │
│                         │                                    │
│                         ▼                                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Summary:                                            │   │
│  │   Successfully moved: 2                             │   │
│  │   Failed: 0                                         │   │
│  └─────────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  Step 5: Verification                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Verify in GitHub UI:                                │   │
│  │ 1. Go to V12.3 project                              │   │
│  │ 2. Check that issues were added                     │   │
│  │ 3. Manually update status if needed                 │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## API Interactions

```
Python Script                GitHub GraphQL API
    │                              │
    │   Query: Get Projects        │
    ├─────────────────────────────>│
    │                              │
    │   Response: List of Projects │
    │<─────────────────────────────┤
    │                              │
    │   Query: Get Project Items   │
    ├─────────────────────────────>│
    │                              │
    │   Response: Items + Status   │
    │<─────────────────────────────┤
    │                              │
    │   Filter: Status="No Status" │
    │                              │
    │   (Preview shown to user)    │
    │                              │
    │   User confirms: yes         │
    │                              │
    │   Mutation: Add Item         │
    ├─────────────────────────────>│
    │                              │
    │   Response: Success          │
    │<─────────────────────────────┤
    │                              │
```

## Data Flow

```
Organization Projects
        │
        ├── Project A
        │   └── Issue #170 (Status: "No Status") ───┐
        │   └── Issue #161 (Status: "No Status") ───┤
        │                                            │
        ├── Project B                                │
        │   └── Issue #122 (Status: "In Progress")  │
        │                                            │
        ├── V12.3 (Target)                          │
        │   └── Issue #156 (Status: "Todo")         │
        │                                            │
        └── Project D                                │
                                                     │
                                                     │
                          Script identifies ────────┘
                          issues with "No Status"
                                   │
                                   │
                                   ▼
                          Add to V12.3 Project
                                   │
                                   │
                                   ▼
Organization Projects (After)
        │
        ├── Project A
        │   └── Issue #170 (Status: "No Status") ───┐ Still in Project A
        │   └── Issue #161 (Status: "No Status") ───┤
        │                                            │
        ├── Project B                                │
        │   └── Issue #122 (Status: "In Progress")  │
        │                                            │
        ├── V12.3 (Target)                          │ Also added here
        │   └── Issue #156 (Status: "Todo")         │
        │   └── Issue #170 (Status: "No Status") <──┘
        │   └── Issue #161 (Status: "No Status") <──┐
        │                                            │
        └── Project D
```

## File Structure

```
.github/scripts/
├── README.md                      ← Main documentation (start here)
├── README_PROJECTS.md             ← Detailed technical docs
├── PREVIEW_OUTPUT.md              ← Example outputs
├── WORKFLOW.md                    ← This file (visual workflow)
├── github_projects_manager.py     ← Main script
├── run.sh                         ← Interactive wrapper
└── requirements.txt               ← Python dependencies
```

## Quick Reference

| Command | Purpose |
|---------|---------|
| `./run.sh` | Interactive mode with menu |
| `python3 github_projects_manager.py preview` | Show what would be moved |
| `python3 github_projects_manager.py move` | Move issues (with confirmation) |
| `export GITHUB_TOKEN=...` | Set authentication token |
| `pip3 install -r requirements.txt` | Install dependencies |
