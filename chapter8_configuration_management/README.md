# Chapter 8: Configuration Management

Configuration management with Hydra for flexible parameter handling.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter8) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter8
```

## Examples

### [01_basic_hydra_config/](01_basic_hydra_config/) - Basic Hydra setup
```bash
cd 01_basic_hydra_config && uv run python process.py
```

### [02_interpolation/](02_interpolation/) - Config value interpolation
```bash
cd 02_interpolation && uv run python interpolation_demo.py
```

### [03_config_groups/](03_config_groups/) - Organized config groups
```bash
cd 03_config_groups && uv run python config_groups_demo.py
```

### [04_environment_configs/](04_environment_configs/) - Environment-specific configurations
```bash
cd 04_environment_configs && uv run --group chapter8 python environment_demo.py
# Or with Hydra integration:
cd 04_environment_configs && uv run --group chapter8 python hydra_environment_demo.py
```

## Quick Start

```bash
cd 01_basic_hydra_config
uv run python process.py
```

---

Each example is self-contained and ready to run.