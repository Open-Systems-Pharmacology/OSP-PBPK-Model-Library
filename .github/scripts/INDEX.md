# GitHub Projects Issue Management - Index

Welcome! This directory contains everything you need to move issues from "No Status" to the V12.3 project.

## 🚀 Quick Start (3 Steps)

1. **Create a GitHub token**: https://github.com/settings/tokens (needs `repo` and `project` scopes)
2. **Set the token**: `export GITHUB_TOKEN=your_token_here`
3. **Run the script**: `./run.sh` and choose option 1 (Preview)

See **[CHECKLIST.md](CHECKLIST.md)** for detailed step-by-step instructions.

## 📚 Documentation Files

### For End Users

| File | Description | Start Here? |
|------|-------------|-------------|
| **[CHECKLIST.md](CHECKLIST.md)** | Step-by-step checklist with checkboxes | ⭐ **START HERE** |
| **[README.md](README.md)** | Complete usage guide with examples | ⭐ **MAIN DOCS** |
| **[PREVIEW_OUTPUT.md](PREVIEW_OUTPUT.md)** | What the output looks like | 👁️ Preview |
| **[SUMMARY.md](SUMMARY.md)** | Overview of everything created | 📋 Reference |

### For Technical Users

| File | Description | Best For |
|------|-------------|----------|
| **[README_PROJECTS.md](README_PROJECTS.md)** | Technical API details | Developers |
| **[WORKFLOW.md](WORKFLOW.md)** | Visual diagrams and flows | Understanding |

## 🛠️ Script Files

| File | Description | Executable |
|------|-------------|------------|
| **github_projects_manager.py** | Main Python script | ✅ Yes |
| **run.sh** | Interactive wrapper | ✅ Yes |
| **requirements.txt** | Python dependencies | No |

## 📖 How to Use This Documentation

### I just want to move issues NOW!
→ Go to **[CHECKLIST.md](CHECKLIST.md)** and follow the checkboxes

### I want to understand what will happen first
→ Read **[README.md](README.md)** sections:
- "What This Does"
- "Step-by-Step Guide"
- "Understanding the Output"

### I want to see example output
→ Open **[PREVIEW_OUTPUT.md](PREVIEW_OUTPUT.md)**

### I want to understand the technical details
→ Read **[README_PROJECTS.md](README_PROJECTS.md)** for:
- GitHub GraphQL API details
- How the script works
- Advanced usage

### I want to see the workflow visually
→ Check **[WORKFLOW.md](WORKFLOW.md)** for:
- ASCII flowcharts
- Data flow diagrams
- API interaction patterns

### I want a complete overview
→ See **[SUMMARY.md](SUMMARY.md)** for:
- All files created
- What each file does
- Validation results
- Technical specs

## 🎯 Common Tasks

### Preview which issues will be moved
```bash
export GITHUB_TOKEN=your_token
./run.sh
# Choose option 1
```

### Move issues to V12.3
```bash
export GITHUB_TOKEN=your_token
./run.sh
# Choose option 2
# Type 'yes' to confirm
```

### Direct command line usage
```bash
export GITHUB_TOKEN=your_token
python3 github_projects_manager.py preview    # Preview only
python3 github_projects_manager.py move       # Move with confirmation
```

## 🔍 File Details

```
.github/scripts/
├── INDEX.md                      ← You are here
├── CHECKLIST.md                  ← Quick start checklist (4.6 KB)
├── README.md                     ← Main documentation (7.6 KB)
├── SUMMARY.md                    ← Complete overview (7.8 KB)
├── PREVIEW_OUTPUT.md             ← Example outputs (3.5 KB)
├── README_PROJECTS.md            ← Technical docs (5.8 KB)
├── WORKFLOW.md                   ← Visual workflows (15 KB)
├── github_projects_manager.py    ← Main Python script (15 KB)
├── run.sh                        ← Interactive shell (2.4 KB)
└── requirements.txt              ← Dependencies (17 bytes)

Total: ~67 KB of code and documentation
```

## ✅ What You Get

1. **Preview Mode** - See what will happen before any changes
2. **Safety Features** - Confirmation required for moves
3. **Error Handling** - Graceful failures with detailed messages
4. **Comprehensive Docs** - Multiple guides for different needs
5. **Interactive Mode** - Easy-to-use menu system
6. **Direct CLI** - Power users can run commands directly

## 🛡️ Safety Features

- ✅ Preview mode makes NO changes
- ✅ Move mode requires explicit confirmation
- ✅ Each issue move is independent (failures don't stop others)
- ✅ Detailed logging shows exactly what's happening
- ✅ Issues stay in original projects (added to V12.3, not moved)

## 📊 Expected Results

When you run the preview, you'll see:
- Total number of issues with "No Status"
- Issue numbers, titles, and URLs
- Which project each issue is currently in
- Confirmation that V12.3 is the target project

When you run the move, you'll see:
- Progress for each issue being processed
- Success or failure status for each move
- Final summary: X moved successfully, Y failed

## 🔧 Requirements

- Python 3.6+
- requests library (auto-installed by run.sh)
- GitHub Personal Access Token with:
  - `repo` scope
  - `project` scope (read + write)

## ❓ Getting Help

1. **Quick answers**: Check the troubleshooting sections in:
   - [README.md](README.md#troubleshooting)
   - [CHECKLIST.md](CHECKLIST.md#troubleshooting)

2. **Understanding errors**: See detailed error explanations in:
   - [README_PROJECTS.md](README_PROJECTS.md#troubleshooting)

3. **Visual understanding**: Review the workflow diagrams in:
   - [WORKFLOW.md](WORKFLOW.md)

## 🎓 Learning Path

**Beginner**: 
1. Read [CHECKLIST.md](CHECKLIST.md)
2. Run preview mode
3. Review output
4. Run move mode if satisfied

**Intermediate**: 
1. Read [README.md](README.md)
2. Understand the workflow in [WORKFLOW.md](WORKFLOW.md)
3. Run commands directly

**Advanced**: 
1. Study [README_PROJECTS.md](README_PROJECTS.md)
2. Review the Python script source
3. Modify for your specific needs

## 📝 Quick Reference

| Want to... | Read... |
|-----------|---------|
| Move issues quickly | [CHECKLIST.md](CHECKLIST.md) |
| Understand the process | [README.md](README.md) |
| See example output | [PREVIEW_OUTPUT.md](PREVIEW_OUTPUT.md) |
| Learn technical details | [README_PROJECTS.md](README_PROJECTS.md) |
| Visualize the workflow | [WORKFLOW.md](WORKFLOW.md) |
| Get a complete overview | [SUMMARY.md](SUMMARY.md) |

## 🎉 You're Ready!

Follow the [CHECKLIST.md](CHECKLIST.md) to get started with moving your issues.

**Remember**: Always run preview first to see what will happen!

---

**Need immediate help?**
- Check [CHECKLIST.md](CHECKLIST.md) - Troubleshooting section
- Check [README.md](README.md) - Troubleshooting section
- Review [SUMMARY.md](SUMMARY.md) - Complete overview
