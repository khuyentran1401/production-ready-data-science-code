# Chapter 12: Continuous Integration

GitHub Actions workflows for automating data science pipelines.

These examples are from [Production-Ready Data Science](https://codecut.ai/production-ready-data-science/?utm_source=github&utm_medium=production-ready-data-science-code&utm_campaign=chapter12) by Khuyen Tran.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter12
```

## Examples

### [01_basic_ci/](01_basic_ci/) - Automatic documentation generation
```bash
cd 01_basic_ci && cat .github/workflows/docs.yml
```

### [02_data_pipeline/](02_data_pipeline/) - Automated data pipeline workflow
```bash
cd 02_data_pipeline && cat .github/workflows/data-pipeline.yml
```

### [03_generate_report/](03_generate_report/) - Automatic report generation
```bash
cd 03_generate_report && python analysis/generate_report.py
```

### [04_job_dependencies/](04_job_dependencies/) - ML workflow with job ordering
```bash
cd 04_job_dependencies && cat .github/workflows/ml-pipeline.yml
```

## Quick Start

```bash
cd 01_basic_ci
cat .github/workflows/docs.yml
```

---

Each example is self-contained and ready to run.