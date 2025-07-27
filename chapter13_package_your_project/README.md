# Chapter 13: Package Your Project

Complete Python packaging example using modern tooling with uv and hatchling.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter13) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter13
```

## Examples

### [pandas_processors/](pandas_processors/) - Complete package structure with tests
```bash
cd pandas_processors && pytest
```

### [pyproject.toml](pyproject.toml) - Modern Python packaging configuration
```bash
cat pyproject.toml
```

### [tests/](tests/) - Test suite for package validation
```bash
pytest --cov=pandas_processors
```

## Quick Start

```bash
cd pandas_processors
pytest -v
```

---

Each example is self-contained and ready to run.