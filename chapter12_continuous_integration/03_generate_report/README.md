# Generate Report Workflow

This example demonstrates automatic report generation when changes are made to analysis scripts.

## Files
- `.github/workflows/generate_report.yaml`: GitHub Actions workflow
- `analysis/generate_report.py`: Python script that generates reports
- `requirements.txt`: Project dependencies

## How It Works

1. **Trigger**: Workflow runs when changes are pushed to `analysis/*.py` files
2. **Environment**: Sets up Python 3.8 on Ubuntu
3. **Dependencies**: Installs project requirements
4. **Report Generation**: Runs the report generation script
5. **Artifact**: Uploads the generated PDF report

## Key Features Demonstrated
- Path filtering with wildcards (`analysis/*.py`)
- Automated script execution
- Report generation with matplotlib
- PDF artifact creation and upload
- Stakeholder-ready deliverable generation

## Usage

```bash
# Test the report generation locally
python analysis/generate_report.py
```

This workflow triggers automatically when:
- Changes are pushed to Python files in the `analysis/` directory
- The generated report (PDF) becomes available as a downloadable artifact
- Stakeholders can access the latest analysis results without manual intervention