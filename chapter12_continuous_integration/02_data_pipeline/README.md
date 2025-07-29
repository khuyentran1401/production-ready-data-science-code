# Data Pipeline Workflow

Automatic data pipeline execution when changes are made to the `data/` directory.

## Files

- `.github/workflows/data_pipeline.yaml` - GitHub Actions workflow for data pipeline
- `data/` directory - Where data files would be stored (triggers workflow)

## Key Points

- Workflow triggers on pushes to `data/**` files
- Integrates with DVC for data versioning and automated pipeline execution

## How to Run

```bash
# Test DVC pipeline locally
dvc repro

# Check pipeline status
dvc status
```

## Expected Output

Workflow automatically pulls latest data from DVC remote and executes the complete data pipeline when data files change.

## Try This

1. **Add data**: Push changes to files in the `data/` directory
2. **Watch automation**: See the workflow trigger and execute the full pipeline
3. **Check artifacts**: Review generated outputs from the automated pipeline run

## Learn More

← [Back to Chapter 12](../README.md)

---

← [Previous: 01_basic_ci](../01_basic_ci/README.md) | **Next:** [03_generate_report →](../03_generate_report/README.md)

*Example 2 of 4*