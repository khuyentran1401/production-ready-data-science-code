# Testing marimo Notebooks

How marimo notebooks can be tested with pytest like regular Python modules.

## Files

- `test_example.py` - marimo notebook with testable functions

## Key Points

- marimo notebooks are plain Python scripts that can be tested with pytest
- Functions defined in cells can be tested independently

## How to Run

```bash
# Run the notebook interactively
uv run --group chapter14 marimo edit test_example.py

# Run tests with pytest
uv run --group chapter14 pytest test_example.py
```

## Expected Output

Pytest runs tests defined in the notebook cells, providing standard test output and CI/CD compatibility.

## Try This

1. **Interactive testing**: Run the notebook and see tests execute inline
2. **Command line testing**: Use `pytest test_example.py` to run tests from terminal
3. **Add new tests**: Create additional test functions following pytest conventions
4. **Break functions**: Modify functions to see how tests catch issues

## Learn More

← [Back to Chapter 14](../README.md) for more notebook patterns and the complete guide.