# Testing marimo Notebooks  

This example demonstrates how marimo notebooks can be tested with pytest, as shown in Chapter 14.

## Files
- `test_example.py`: marimo notebook with testable functions

## Key Features Demonstrated
- Functions defined within notebook cells
- Test functions that can be run with pytest
- Inline test execution within the notebook
- Standard Python testing workflow

## Running the Example

### Interactive Notebook
```bash
# Run the notebook interactively
uv run --group chapter14 marimo edit test_example.py
```

### Command Line Testing
```bash
# Run tests with pytest (as shown in the book)
uv run --group chapter14 pytest test_example.py
```

## What Makes This Possible

Unlike traditional Jupyter notebooks, marimo notebooks are:
- **Plain Python Scripts**: Can be imported and tested like any Python module
- **Function-Based**: Each cell is a function that can be tested independently  
- **No Hidden State**: Tests run predictably without notebook-specific quirks

## Testing Workflow

1. **Define Functions**: Create testable functions in notebook cells
2. **Write Tests**: Add test functions following pytest conventions
3. **Inline Verification**: Run tests within the notebook for immediate feedback
4. **CI Integration**: Use `pytest test_example.py` in CI pipelines

## Benefits for Production

- **CI/CD Compatible**: Standard pytest commands work seamlessly
- **Code Quality**: Functions can be tested just like regular Python code
- **Reproducible**: Tests run the same way in notebook and CI environments
- **No Special Tools**: Uses standard Python testing ecosystem