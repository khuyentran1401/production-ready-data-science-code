# Chapter 1: Version Control Your Code - Examples

## Problem

Data scientists often work on experiments that evolve rapidly—tweaking models, trying different datasets, collaborating with teammates. Without version control, it's easy to lose working code, accidentally break functionality, or struggle to reproduce results. Git provides the foundation for tracking changes, collaborating safely, and maintaining reproducible data science workflows.

← [Back to Main README](../README.md)

## Prerequisites

- Git installed on your system
- Dependencies: `uv sync --group chapter1`
- GitHub account for remote examples

## Example Script

- `process.py` - Simple data processing script for Git demonstrations

## Git Command Examples

### Basic Git Commands

```bash
git init
```

Output:

```
Initialized empty Git repository in /path/to/chapter1_version_control/.git/
```

```bash
git status
```

Output:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        process.py

nothing added to commit but untracked files present (use "git add" to track)
```

Output:

```bash
git add .
```

```bash
git commit -m "Initial commit: Add data science project files"
```

Output:

```
[main (root-commit) abc1234] Initial commit: Add data science project files
 3 files changed, 50 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 process.py
```

```bash
git log --oneline
```

Output:

```
abc1234 (HEAD -> main) Initial commit: Add data science project files
```

### Remote Repository Commands

```bash
git remote add origin https://github.com/USERNAME/repo-name.git
```

```bash
git remote -v
```

Output:

```
origin  https://github.com/USERNAME/repo-name.git (fetch)
origin  https://github.com/USERNAME/repo-name.git (push)
```

```bash
git push -u origin main
```

Output:

```
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 2.1 KiB | 2.1 MiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/USERNAME/repo-name.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

```bash
git pull origin main
```

Output:

```
From https://github.com/USERNAME/repo-name
 * branch            main       -> FETCH_HEAD
Already up to date.
```

### Branching Commands

```bash
git checkout -b feature/improve-model
```

Output:

```
Switched to a new branch 'feature/improve-model'
```

```bash
git branch
```

Output:

```
* feature/improve-model
  main
```

```bash
git checkout main
```

Output:

```
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

```bash
git merge feature/improve-model
```

Output:

```
Updating abc1234..def5678
Fast-forward
 process.py | 3 +++
 1 file changed, 3 insertions(+)
```

```bash
git branch -d feature/improve-model
```

Output:

```
Deleted branch feature/improve-model (was def5678).
```

### Error Recovery Commands

```bash
git stash
```

```
Saved working directory and index state WIP on main: abc1234 Initial commit
```

```bash
git stash pop
```

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   process.py

no changes added to commit (use "git add" or "git commit -a")
Dropped refs/stash@{0} (ghi9012)
```

```bash
git revert HEAD
```

Output:

```
[main jkl3456] Revert "Add problematic feature"
 1 file changed, 1 deletion(-)
```

```bash
git reset --soft HEAD~1
```

## Why This Matters

Version control transforms chaotic data science experiments into organized, reproducible workflows that enable collaboration and prevent costly mistakes.
