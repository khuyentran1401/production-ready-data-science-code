# Project Structure

**Problem**: Data science projects often lack standardized organization, making it difficult for team members to navigate code, find specific functionality, or package projects for deployment.

Standardized data science project template following Python packaging best practices.

**Why This Matters**: Consistent project structure accelerates team onboarding, makes code discoverable, and enables smooth transition from research to production deployment.

## Files

- `pyproject.toml` - Modern Python project configuration with UV support
- `src/data_pipeline/` - Main package with subpackages:
  - `data/` - Data loading and processing (loader.py, processor.py)
  - `models/` - ML training and prediction (trainer.py, predictor.py)
  - `utils/` - Shared utilities (helpers.py)
- `tests/` - Test directory mirroring src/ structure
- `scripts/run_pipeline.py` - Standalone pipeline execution script

## Key Points

- src/ layout prevents accidental imports of uninstalled code
- Subpackages organize functionality by domain

## How to Run

```bash
# Install in development mode
uv sync

# Run the pipeline
uv run scripts/run_pipeline.py

# Run tests
uv run pytest tests/

# Verify package installation
python -c "from data_pipeline.data.loader import load_data; print('✅ Package installed correctly')"
```

## Expected Output

Pipeline executes data loading, processing, and model training steps. All tests pass.

## Try This

1. **Copy the structure**: Use this template for your next data science project
2. **Add new modules**: Create additional subpackages and corresponding tests
3. **Test the organization**: See how easy it is to find and import specific functionality
4. **Scale up**: Add more complex package hierarchies following this pattern

## Learn More

← [Back to Chapter 3](../README.md)

---

← [Previous: 05_circular_imports](../05_circular_imports/README.md)

*Example 6 of 6*