# Chapter 6: Classes

## Problem

Data science code often handles complex data structures and workflows using dictionaries, global variables, and loose functions. This approach becomes unwieldy as projects grow, making state management difficult and data validation error-prone. Classes provide structured ways to organize related data and behavior, especially with tools like Pydantic for automatic validation.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter6
```

## Examples

### [chapter6_classes.ipynb](chapter6_classes.ipynb) - Interactive examples
```bash
# Run the notebook
uv run jupyter notebook chapter6_classes.ipynb
```

## Quick Start

```bash
uv run jupyter notebook chapter6_classes.ipynb
```

---

## Why This Matters

Classes with proper validation prevent data errors, organize complex workflows, and create reusable components for production data science systems.