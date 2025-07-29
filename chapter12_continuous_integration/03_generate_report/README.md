# Generate Report Workflow

Automatic report generation when changes are made to analysis scripts.

## Files

- `.github/workflows/generate_report.yaml` - GitHub Actions workflow
- `analysis/generate_report.py` - Python script that generates reports
- `requirements.txt` - Project dependencies

## Key Points

- Workflow triggers on pushes to `analysis/*.py` files
- Generates PDF reports with matplotlib and uploads as artifacts

## How to Run

```bash
# Test the report generation locally
python analysis/generate_report.py
```

## Expected Output

Workflow generates a PDF report and makes it available as a downloadable artifact when analysis scripts change.

## Try This

1. **Modify analysis**: Change the report generation script
2. **Push changes**: Trigger the workflow by committing to `analysis/` directory
3. **Download report**: Access the generated PDF from the workflow artifacts

## Learn More

← [Back to Chapter 12](../README.md)

---

← [Previous: 02_data_pipeline](../02_data_pipeline/README.md) | **Next:** [04_job_dependencies →](../04_job_dependencies/README.md)

*Example 3 of 4*