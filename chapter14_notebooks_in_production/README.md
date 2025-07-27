# Chapter 14: Notebooks in Production

Production-ready notebooks using marimo for reproducible data science workflows.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter14) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter14
pip install marimo
```

## Examples

### [01_basic_marimo_notebook/](01_basic_marimo_notebook/) - Introduction to marimo structure
```bash
cd 01_basic_marimo_notebook && marimo edit my_notebook.py
```

### [02_dependency_tracking/](02_dependency_tracking/) - Automatic cell re-execution
```bash
cd 02_dependency_tracking && marimo edit filtering_example.py
```

### [03_data_analysis_workflow/](03_data_analysis_workflow/) - Complete data science workflow
```bash
cd 03_data_analysis_workflow && marimo edit data_analysis.py
```

### [04_testing_notebook/](04_testing_notebook/) - Testable notebook functions
```bash
cd 04_testing_notebook && pytest test_example.py
```

### [05_variable_redefinition_error/](05_variable_redefinition_error/) - Variable redefinition prevention
```bash
cd 05_variable_redefinition_error && marimo edit variable_redefinition_demo.py
```

## Quick Start

```bash
cd 01_basic_marimo_notebook
marimo edit my_notebook.py
```

---

Each example is self-contained and ready to run.