# Chapter 2: Dependency Management

Practice the key dependency management concepts from the book with simple, runnable examples.

← [Back to Main README](../README.md)


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