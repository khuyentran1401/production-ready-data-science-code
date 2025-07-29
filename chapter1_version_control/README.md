# Chapter 1: Version Control Your Code

## Problem

Data scientists often work on experiments that evolve rapidly—tweaking models, trying different datasets, collaborating with teammates. Without version control, it's easy to lose working code, accidentally break functionality, or struggle to reproduce results.

← [Back to Main README](../README.md)

## Prerequisites

- Git installed on your system
- GitHub account for remote repositories

## Example File

- `process.py` - Simple data processing script for demonstrations

## Quick Reference by Scenario

### Starting a New Project

Initialize repository and create first commit:

```bash
git init                              # Initialize Git repository
git add .                             # Stage all files
git commit -m "Initial commit"        # Create first commit
git remote add origin <repository-URL> # Connect to remote repository
git push -u origin main               # Push and set upstream
```

### Contributing to Existing Project

Clone and create feature branch:

```bash
git clone <repository-URL>            # Clone existing project
cd <project-name>                     # Navigate to project
git checkout -b feature/new-feature   # Create feature branch
# Make your changes to files
git add .                             # Stage changes
git commit -m "Add new feature"       # Commit changes
git push origin feature/new-feature   # Push feature branch
# Create pull request on GitHub
```

### Daily Workflow

Common commands for regular development:

```bash
git status                            # Check current status
git add process.py                    # Stage specific file
git add .                             # Stage all changes
git commit -m "Update data processing" # Commit with message
git pull                              # Get latest changes
git push                              # Share your changes
git log --oneline                     # View commit history
```

### Error Recovery

Fix mistakes and recover work:

```bash
# Temporarily save work
git stash                             # Save current changes
git stash pop                         # Restore saved changes

# Undo commits safely
git revert HEAD                       # Create new commit that undoes last commit
git reset --soft HEAD~1               # Undo last commit, keep changes staged
git reset --hard HEAD~1               # Undo last commit, discard changes (careful!)

# View and manage branches
git branch                            # List all branches
git branch -d feature-name            # Delete merged branch
git checkout main                     # Switch to main branch
```

### Remote Repository Management

Work with GitHub/remote repositories:

```bash
git remote -v                         # View remote repositories
git remote add origin <URL>           # Add remote repository
git push origin main                  # Push to main branch
git pull origin main                  # Pull from main branch
git fetch                             # Download remote changes (don't merge)
```

---

## Why This Matters

Version control transforms chaotic data science experiments into organized, reproducible workflows that enable collaboration and prevent costly mistakes.
