# Basic CI - Create Documentation

This example demonstrates automatic documentation generation when changes are made to the `src/` directory.

## Files
- `.github/workflows/create_documentation.yaml`: GitHub Actions workflow
- `src/example_module.py`: Example Python module with docstrings
- `requirements.txt`: Project dependencies

## How It Works

1. **Trigger**: Workflow runs when a pull request modifies files in `src/**`
2. **Environment**: Sets up Python 3.8 on Ubuntu
3. **Dependencies**: Installs project requirements and pdoc3
4. **Documentation**: Generates HTML docs from source code
5. **Artifact**: Uploads generated documentation as workflow artifact

## Key Features Demonstrated
- Path-based workflow triggering (`paths: - src/**`)
- Using pre-built actions (`actions/checkout@v2`, `actions/setup-python@v2`)
- Installing documentation tools (pdoc3)
- Creating and uploading artifacts
- Automatic documentation generation from docstrings

## Usage

This workflow would trigger automatically when:
- A pull request is created that modifies files in the `src/` directory
- The workflow generates HTML documentation and makes it available as a downloadable artifact