# Chapter 3: Modules and Packages

Organize Python code into reusable, maintainable components.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter3
```

## Examples

### [01_basic_modules/](01_basic_modules/) - Create and import modules
```bash
cd 01_basic_modules && uv run process_data.py
```

### [02_modular_design/](02_modular_design/) - Break monolithic code into modules
```bash
cd 02_modular_design/modular && uv run main.py
```

### [03_import_practices/](03_import_practices/) - Import best practices
```bash
cd 03_import_practices/wildcard_imports && uv run process_data_good.py
```

### [04_main_blocks/](04_main_blocks/) - Control code execution
```bash
cd 04_main_blocks/with_main && uv run main.py
```

### [05_circular_imports/](05_circular_imports/) - Avoid circular dependencies
```bash
cd 05_circular_imports/fixed && uv run main.py
```

### [06_project_structure/](06_project_structure/) - Standardized project layout
```bash
cd 06_project_structure && uv sync && uv run scripts/run_pipeline.py
```

## Quick Start

```bash
cd 01_basic_modules
uv run process_data.py
```

---

Each example is self-contained and ready to run.