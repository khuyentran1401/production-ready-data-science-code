# Project Structure: Standardized Data Science Template

This example shows a **standardized project structure** for data science projects that follows Python packaging best practices and industry conventions.

## Why Standard Structure Matters

A well-organized project structure:
- **Improves navigation** - Team members can quickly find files
- **Enables proper packaging** - Code can be installed and imported correctly  
- **Supports testing** - Clear separation between source code and tests
- **Facilitates deployment** - Easy to containerize and deploy
- **Follows conventions** - Familiar to other Python developers

## Project Template Structure

```
06_project_structure/
├── README.md                 # This file
├── pyproject.toml           # Modern Python project configuration
├── src/                     # Source code package
│   └── data_pipeline/       # Main package
│       ├── __init__.py      # Package initialization
│       ├── config.py        # Configuration management
│       ├── data/            # Data processing subpackage
│       │   ├── __init__.py
│       │   ├── loader.py    # Data loading functions
│       │   └── processor.py # Data processing functions
│       ├── models/          # ML models subpackage
│       │   ├── __init__.py
│       │   ├── trainer.py   # Model training
│       │   └── predictor.py # Model prediction
│       └── utils/           # Utility functions
│           ├── __init__.py
│           └── helpers.py   # Helper functions
├── tests/                   # Test files
│   ├── __init__.py
│   ├── test_data/          # Test data processing
│   │   ├── test_loader.py
│   │   └── test_processor.py
│   ├── test_models/        # Test ML models
│   │   ├── test_trainer.py
│   │   └── test_predictor.py
│   └── test_utils/         # Test utilities
│       └── test_helpers.py
├── data/                   # Data files (not in src/)
│   ├── raw/               # Raw data
│   └── processed/         # Processed data
├── notebooks/             # Jupyter notebooks
│   └── exploration.ipynb  # Data exploration
├── scripts/               # Standalone scripts
│   └── run_pipeline.py    # Pipeline execution script
└── docs/                  # Documentation
    └── api.md            # API documentation
```

## Key Benefits of This Structure

### ✅ **`src/` Layout**
- Prevents accidental imports of uninstalled code
- Forces proper package installation for testing
- Industry standard for Python packages

### ✅ **Subpackages for Organization** 
- `data/` - All data-related functionality
- `models/` - ML model training and prediction
- `utils/` - Shared utility functions

### ✅ **Separate Test Directory**
- Mirrors the `src/` structure in `tests/`
- Easy to run all tests: `uv run pytest tests/`
- Clear separation of concerns

### ✅ **Modern Configuration**
- `pyproject.toml` instead of setup.py
- UV-compatible dependency groups
- Proper build system configuration

## How to Use This Template

1. **Copy the structure** to your new project
2. **Update pyproject.toml** with your project name and dependencies
3. **Install in development mode**: `uv sync`
4. **Add your code** to the appropriate subpackages
5. **Write tests** that mirror your source structure
6. **Run tests**: `uv run pytest`

## Installation and Usage

```bash
# Install the package in development mode
uv sync

# Run the main pipeline script
uv run scripts/run_pipeline.py

# Run all tests
uv run pytest tests/

# Import the package in code
python -c "from data_pipeline.data.loader import load_data; print('✅ Package installed correctly')"
```

This structure scales from small projects to large enterprise applications while maintaining clarity and following Python best practices.