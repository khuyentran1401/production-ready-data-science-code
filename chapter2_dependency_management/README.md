# Chapter 2: Dependency Management

## Problem

Data science projects often break when shared between team members or deployed to production due to missing packages, version conflicts, or environment differences. "It works on my machine" becomes a constant frustration when pandas 1.5 works locally but production has 1.3, or when a colleague can't run your notebook because of missing dependencies.

Practice the key dependency management concepts from the book with simple, runnable examples.


## Examples

- [01_virtual_environments/](01_virtual_environments/) - Experience pandas conflicts
- [02_version_ranges/](02_version_ranges/) - Compare version pinning strategies
- [03_dev_prod_separation/](03_dev_prod_separation/) - Separate dev/prod dependencies
- [04_uv_basics/](04_uv_basics/) - Modern dependency management with uv


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

---

## Why This Matters

Proper dependency management eliminates "works on my machine" problems, ensures reproducible results across environments, and prevents production failures caused by package version conflicts.

---

← [Back to Main README](../README.md) | **Next:** [Chapter 3: Modules & Packages →](../chapter3_modules_packages/README.md)