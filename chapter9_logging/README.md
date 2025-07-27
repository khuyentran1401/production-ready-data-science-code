# Chapter 9: Logging

Structured logging with Loguru for production-ready applications.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter9) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter9
```

## Examples

### [01_basic_logging/](01_basic_logging/) - Basic Loguru usage
```bash
cd 01_basic_logging && uv run python basic_loguru.py
```

### [02_custom_formatting/](02_custom_formatting/) - Custom log formats
```bash
cd 02_custom_formatting && uv run python custom_format.py
```

### [03_file_logging/](03_file_logging/) - File and terminal logging
```bash
cd 03_file_logging && uv run python file_logging.py
```

### [04_rotation_retention/](04_rotation_retention/) - Log rotation strategies
```bash
cd 04_rotation_retention && uv run python rotation_example.py
```

### [05_filtering/](05_filtering/) - Message filtering
```bash
cd 05_filtering && uv run python filtering_example.py
```

### [06_exception_handling/](06_exception_handling/) - Exception logging
```bash
cd 06_exception_handling && uv run python exception_logging.py
```

### [07_colorized_logs/](07_colorized_logs/) - Color schemes
```bash
cd 07_colorized_logs && uv run python colorized_logging.py
```

## Quick Start

```bash
cd 01_basic_logging
uv run python basic_loguru.py
```

---

Each example is self-contained and ready to run.