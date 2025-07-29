# Basic CI - Create Documentation

Automatic documentation generation when changes are made to source code.

## Files

- `.github/workflows/create_documentation.yaml` - GitHub Actions workflow
- `src/example_module.py` - Python module with docstrings
- `requirements.txt` - Project dependencies

## Key Points

- Workflow triggers on pull requests that modify `src/**` files
- Generates HTML documentation using pdoc3 and uploads as artifact

## How to Run

```bash
# Test documentation generation locally
pip install pdoc3
pdoc3 --html src/example_module.py
```

## Expected Output

Workflow creates downloadable HTML documentation artifact when PR modifies source files.

## Learn More

← [Back to Chapter 12](../README.md)

---

**Next:** [02_data_pipeline →](../02_data_pipeline/README.md)

*Example 1 of 4*