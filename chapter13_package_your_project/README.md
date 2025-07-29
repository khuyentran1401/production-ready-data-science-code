# Chapter 13: Package Your Project

## Problem

Data science code often stays trapped in individual notebooks or scripts, making it impossible for others to reuse valuable utilities and models. Without proper packaging, teams duplicate code, struggle with dependencies, and can't easily deploy models. Python packaging transforms reusable code into distributable libraries that teams can install and share.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter13
```

## Examples

- **[pandas_processors/](pandas_processors/)** - Complete package structure with tests
  ```bash
  uv run pytest tests/
  ```

- **[pyproject.toml](pyproject.toml)** - Modern Python packaging configuration
  ```bash
  cat pyproject.toml
  ```

- **[tests/](tests/)** - Test suite for package validation
  ```bash
  uv run pytest tests/ --cov=pandas_processors
  ```

## Project Structure

This package follows Python packaging best practices with a standardized directory layout:

```
pandas_processors/
├── pandas_processors/     # Source package directory
│   ├── __init__.py       # Package initialization and exports
│   ├── create.py         # DataFrame creation utilities
│   ├── impute.py         # Missing value imputation classes
│   └── normalize.py      # Data normalization classes
├── tests/                # Test suite with comprehensive coverage
│   ├── test_create.py    # Tests for DataFrame creation
│   ├── test_impute.py    # Tests for imputation functionality
│   └── test_normalize.py # Tests for normalization classes
├── docs/                 # Documentation generation directory
├── pyproject.toml        # Package metadata and build configuration
├── CHANGELOG.md          # Version history and changes
├── LICENSE               # Package licensing information
└── README.md             # This file
```

The source directory name (`pandas_processors/`) matches the package name, enabling direct imports like `import pandas_processors`.


## Complete Packaging Workflow

### Development and Testing

```bash
# Install development dependencies
uv sync --group chapter13

# Run tests with coverage
uv run python -m pytest tests/ --cov=pandas_processors

# Run tests in verbose mode
uv run python -m pytest tests/ -v
```

### Building the Package

```bash
# Build distribution files (.tar.gz and .whl)
uv build
```

This creates `dist/` directory with:
- `pandas_processors-0.1.0.tar.gz` (source distribution)
- `pandas_processors-0.1.0-py3-none-any.whl` (wheel distribution)

### Publishing to PyPI

```bash
# Publish to PyPI (requires PyPI account and authentication)
uv publish
```

### Installing the Package

Once published, users can install with:

```bash
# Install from PyPI
pip install pandas-processors

# Install specific version
pip install pandas-processors==0.1.0
```

### Documentation Generation

```bash
# Generate HTML documentation from docstrings
pdoc --html pandas_processors -o docs
```

This creates browsable API documentation in the `docs/` directory.

## Version Management

The package follows [semantic versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.2.3)
- Update version in `pyproject.toml` before building
- Create git tags for releases: `git tag -a v1.0.1 -m "Version 1.0.1"`

---

## Why This Matters

Packaging enables code reuse across projects, simplifies deployment, and allows data science teams to build on each other's work efficiently.