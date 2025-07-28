# Chapter 2: Dependency Management

Practice the key dependency management concepts from the book with simple, runnable examples.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter2) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# Check Python version first
python check_python.py
```

## Examples

### [01_virtual_environments/](01_virtual_environments/) - Experience pandas conflicts
```bash
cd 01_virtual_environments && python -m venv legacy_env && source legacy_env/bin/activate
```

### [02_version_ranges/](02_version_ranges/) - Compare version pinning strategies  
```bash
cd 02_version_ranges && python -m venv exact_env && source exact_env/bin/activate
```

### [03_dev_prod_separation/](03_dev_prod_separation/) - Separate dev/prod dependencies
```bash
cd 03_dev_prod_separation && python -m venv prod_env && source prod_env/bin/activate
```

### [04_uv_basics/](04_uv_basics/) - Modern dependency management with uv
```bash
cd 04_uv_basics && uv init
```

## Quick Start

```bash
cd 01_virtual_environments
python check_python.py
python -m venv legacy_env
source legacy_env/bin/activate  # Windows: legacy_env\Scripts\activate
pip install -r requirements-legacy.txt
python legacy_project.py
```

## Prerequisites

**Python 3.10.11 recommended** for full compatibility with all examples.

### Install Python 3.10.11
**Option 1: pyenv (recommended)**
```bash
# Install pyenv first: https://github.com/pyenv/pyenv#installation
pyenv install 3.10.11
pyenv local 3.10.11  # Use Python 3.10.11 for this project
```

**Option 2: uv (modern alternative)**  
```bash
# Install uv first: https://docs.astral.sh/uv/getting-started/installation/
uv python install 3.10.11
uv python pin 3.10.11
```

### Time Required
- 15 minutes per example
- Additional 5 minutes for Python setup (first time only)

---

Each example demonstrates a specific problem and solution from the book.
