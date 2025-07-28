# Chapter 1: Version Control Your Code - Examples

Practical examples for Chapter 1 of the book. Read Chapter 1 for complete explanations of Git concepts and workflows.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter1) by Khuyen Tran.

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

```
Initialized empty Git repository in /path/to/chapter1_version_control/.git/
```

```bash
git status
```

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

```bash
git add .
```

```bash
git commit -m "Initial commit: Add data science project files"
```

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

```
origin  https://github.com/USERNAME/repo-name.git (fetch)
origin  https://github.com/USERNAME/repo-name.git (push)
```

```bash
git push -u origin main
```

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

```
From https://github.com/USERNAME/repo-name
 * branch            main       -> FETCH_HEAD
Already up to date.
```

### Branching Commands

```bash
git checkout -b feature/improve-model
```

```
Switched to a new branch 'feature/improve-model'
```

```bash
git branch
```

```
* feature/improve-model
  main
```

```bash
git checkout main
```

```
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

```bash
git merge feature/improve-model
```

```
Updating abc1234..def5678
Fast-forward
 process.py | 3 +++
 1 file changed, 3 insertions(+)
```

```bash
git branch -d feature/improve-model
```

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

```
[main jkl3456] Revert "Add problematic feature"
 1 file changed, 1 deletion(-)
```

```bash
git reset --soft HEAD~1
```


