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

## Why This Matters

Packaging enables code reuse across projects, simplifies deployment, and allows data science teams to build on each other's work efficiently.