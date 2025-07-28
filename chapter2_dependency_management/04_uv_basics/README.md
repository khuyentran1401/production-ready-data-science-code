# uv Basics

Follow the book's uv examples to experience modern dependency management.

## Key Points

- uv replaces pip, virtualenv, and Poetry in one tool
- Creates `pyproject.toml` and `uv.lock` files automatically
- Much faster than traditional tools

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