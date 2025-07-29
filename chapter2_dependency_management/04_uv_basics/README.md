# uv Basics

## Problem

Traditional Python dependency management involves juggling multiple tools: pip for installation, virtualenv for environments, pip-tools for locking versions, and manual pyproject.toml editing. This creates complexity and inconsistency. uv consolidates these workflows into a single, fast tool written in Rust.

## Key Points

- uv replaces pip, virtualenv, pip-tools, and Poetry in one tool (10-20x faster installs)
- Creates `pyproject.toml` and `uv.lock` files automatically with proper version locking
- Handles project initialization, dependency management, and environment reproduction seamlessly

## How to Run

Start with an empty directory and run these commands:

**Initialize project:**
```bash
uv init
cat pyproject.toml  # See the generated project file
```

**Add dependencies:**
```bash
uv add pandas scikit-learn
cat pyproject.toml  # See dependencies added automatically
ls -la  # Notice uv.lock file created
```

**Run script:**
```bash
uv run main.py  # Runs the auto-generated main.py
```

**Add development dependencies:**
```bash
uv add pytest black --dev
cat pyproject.toml  # See dev dependencies in [dependency-groups]
```

**Show dependency tree:**
```bash
uv tree  # See all packages and their dependencies
```

**Sync environment:**
```bash
uv sync  # Install all dependencies from lock file
uv sync --no-dev  # Install only production dependencies
```

## Expected Output

- `pyproject.toml` gets updated automatically with each `uv add`
- `uv.lock` contains exact versions for reproducibility
- Commands run much faster than equivalent pip operations

Try timing `uv add pandas` vs `pip install pandas`!

## Why This Matters

Faster dependency resolution and unified tooling reduces project setup time from minutes to seconds, improving developer productivity.

← [Back to Chapter 2](../README.md)

---

← [Previous: 03_dev_prod_separation](../03_dev_prod_separation/README.md)

*Example 4 of 4*