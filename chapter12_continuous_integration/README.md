# Chapter 12: Continuous Integration Examples

This directory contains examples for continuous integration using GitHub Actions as demonstrated in Chapter 12 of the book.

## Examples Overview

### 1. Basic CI - Create Documentation (`01_basic_ci/`)
- Automatic documentation generation from source code
- Triggered by changes in `src/` directory
- Uses pdoc3 to generate HTML documentation
- Creates downloadable artifacts

### 2. Data Pipeline Workflow (`02_data_pipeline/`)
- Automated data pipeline execution
- Triggered by changes in `data/` directory
- Integrates with DVC for data versioning
- Uses AWS S3 for remote data storage

### 3. Generate Report Workflow (`03_generate_report/`)
- Automatic report generation
- Triggered by changes in `analysis/` scripts
- Creates PDF reports with matplotlib
- Uploads reports as artifacts

### 4. Job Dependencies - ML Workflow (`04_job_dependencies/`)
- Complete ML pipeline with proper job ordering
- Demonstrates sequential and parallel job execution
- Shows dependency management with `needs` keyword

## Key Concepts Covered

### 1. **Why Continuous Integration?**
- **Early Bug Detection**: Catch issues before they affect the team
- **Improved Code Quality**: Automated quality checks on every PR
- **Documentation Maintenance**: Keep docs synchronized with code changes

### 2. **GitHub Actions Components**
- **Workflows**: Automated rules triggered by repository events
- **Events**: Activities that trigger workflows (push, pull_request, etc.)
- **Jobs**: Sets of tasks that execute in response to events
- **Steps**: Sequential tasks within a job
- **Actions**: Reusable components from GitHub Marketplace

### 3. **Common Triggers**
- **Pull Request**: `on: pull_request`
- **Push to Branch**: `on: push: branches: [main]`
- **Path Filtering**: `paths: [src/**, data/**, analysis/**]`

### 4. **Job Management**
- **Parallel Execution**: Jobs run simultaneously by default
- **Dependencies**: Use `needs` keyword to control execution order  
- **Conditional Execution**: Failed jobs prevent dependent jobs from running

## GitHub Actions Workflow Structure

```yaml
name: Workflow Name
on:
  # Event triggers
  pull_request:
    paths:
      - src/**

jobs:
  job_name:
    name: Human-readable name
    runs-on: ubuntu-latest
    needs: [dependency_job]  # Optional dependencies
    steps:
      - name: Step name
        uses: actions/checkout@v2  # Use pre-built action
      - name: Another step
        run: echo "Custom command"    # Run custom command
```

## Best Practices Demonstrated

1. **Event Specificity**: Use path filters to trigger workflows only when relevant files change
2. **Reusable Actions**: Leverage pre-built actions for common tasks (checkout, setup-python)
3. **Artifact Management**: Store and share generated files (documentation, reports)
4. **Secret Management**: Use GitHub secrets for sensitive data (API keys, credentials)
5. **Job Dependencies**: Ensure proper execution order while maximizing parallelism
6. **Environment Consistency**: Use specific versions (Python 3.8, action versions)

## Common Data Science Workflows

These examples demonstrate three essential CI patterns for data science:

1. **Documentation Automation**: Keeps API docs synchronized with code
2. **Data Pipeline Automation**: Processes data changes automatically  
3. **Report Generation**: Creates stakeholder deliverables on analysis updates
4. **ML Pipeline Orchestration**: Manages complex multi-step workflows

## Usage Notes

- All workflows use Ubuntu runners (`runs-on: ubuntu-latest`)
- Python 3.8 is used consistently across examples
- Workflows create artifacts that can be downloaded from GitHub Actions tab
- Path filters ensure workflows only run when relevant files change
- Dependencies and requirements are handled automatically in each workflow