# Chapter 12: Continuous Integration

## Problem

Data science teams often rely on manual processes to validate code, run tests, and generate reports, leading to inconsistent results and human errors. Without automation, teams forget to run tests before merging, documentation becomes outdated, and data pipelines break silently when dependencies change.

## Examples

- [01_basic_ci/](01_basic_ci/) - Automatic documentation generation
- [02_data_pipeline/](02_data_pipeline/) - Automated data pipeline workflow
- [03_generate_report/](03_generate_report/) - Automatic report generation
- [04_job_dependencies/](04_job_dependencies/) - ML workflow with job ordering

## Setup

```bash
uv sync --group chapter12
```

---

## Why This Matters

Automated CI/CD pipelines ensure consistent validation, catch errors early, and enable reliable deployment of data science workflows to production.

---

← [Back to Main README](../README.md) | **Next:** [Chapter 13: Package Your Project →](../chapter13_package_your_project/README.md)