# Chapter 7: Unit Testing

Testing patterns for data science code that work in production.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter7) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter7
```

## Examples

### [01_basic_testing/](01_basic_testing/) - Write your first tests
```bash
cd 01_basic_testing && uv run pytest
```

### [02_parametrization/](02_parametrization/) - Test multiple scenarios
```bash
cd 02_parametrization && uv run pytest -v
```

### [03_fixtures/](03_fixtures/) - Share test data
```bash
cd 03_fixtures && uv run pytest -v
```

### [04_edge_cases/](04_edge_cases/) - Handle boundary conditions
```bash
cd 04_edge_cases && uv run pytest -v
```

### [05_mocking/](05_mocking/) - Mock external dependencies
```bash
cd 05_mocking && uv run pytest -v
```

### [06_test_organization/](06_test_organization/) - Structure test suites
```bash
cd 06_test_organization && uv run pytest
```

## Quick Start

```bash
cd 01_basic_testing
uv run pytest -v
```

---

Each example is self-contained and ready to run.