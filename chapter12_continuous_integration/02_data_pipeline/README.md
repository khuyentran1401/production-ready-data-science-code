# Data Pipeline Workflow

This example demonstrates automatic data pipeline execution when changes are made to the `data/` directory.

## Files
- `.github/workflows/data_pipeline.yaml`: GitHub Actions workflow for data pipeline
- `data/` directory: Where data files would be stored (triggers workflow)

## How It Works

1. **Trigger**: Workflow runs when changes are pushed to files in `data/**`
2. **Environment**: Sets up Python 3.8 on Ubuntu
3. **DVC Setup**: Installs DVC (Data Version Control)
4. **AWS Config**: Configures credentials for S3 remote storage
5. **Data Sync**: Pulls latest data from DVC remote
6. **Pipeline**: Executes data pipeline using `dvc repro`

## Key Features Demonstrated
- Push-based workflow triggering (not pull request)
- Path filtering to respond only to data changes
- Integration with DVC for data versioning
- AWS credentials management using GitHub secrets
- Remote data storage configuration
- Automated pipeline execution

## Prerequisites

To use this workflow, you would need:
1. DVC initialized in your repository
2. AWS S3 bucket for data storage
3. GitHub repository secrets configured:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
4. DVC pipeline defined (dvc.yaml file)

## Usage

This workflow triggers automatically when:
- Changes are pushed to files in the `data/` directory
- The pipeline pulls the latest data and reproduces the entire data processing pipeline