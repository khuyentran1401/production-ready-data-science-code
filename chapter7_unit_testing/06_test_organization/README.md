# Test Organization and Structure

This example demonstrates how to organize tests in a scalable, maintainable structure with proper directory layout, shared fixtures, and configuration files.

## What This Example Shows

- **Test directory structure**: Organizing tests to mirror your source code
- **conftest.py usage**: Sharing fixtures and configuration across test modules
- **pytest.ini configuration**: Configuring pytest behavior and options
- **Test discovery**: How pytest finds and runs tests automatically
- **Shared test utilities**: Creating reusable test helpers

## Files and Structure

```
06_test_organization/
├── README.md
├── pytest.ini                 # pytest configuration
├── src/                       # Source code
│   ├── __init__.py
│   ├── data_processor.py      # Data processing functions
│   └── model.py              # Machine learning model functions
├── tests/                     # Test directory
│   ├── __init__.py
│   ├── conftest.py           # Shared fixtures for all tests
│   ├── test_data_processor.py # Tests for data_processor.py
│   ├── test_model.py         # Tests for model.py
│   └── utils/                # Test utilities
│       ├── __init__.py
│       └── test_helpers.py   # Reusable test helper functions
```

## Key Learning Points

1. **Mirror Structure**: Test directory structure should mirror source code structure
2. **Shared Resources**: Use conftest.py for fixtures used across multiple test files
3. **Configuration**: pytest.ini centralizes test configuration and options
4. **Test Discovery**: Follow naming conventions for automatic test discovery
5. **Modularity**: Organize tests into logical modules and packages

## How to Run

```bash
# Run all tests in the project
uv run pytest

# Run tests with verbose output
uv run pytest -v

# Run specific test modules
uv run pytest tests/test_data_processor.py

# Run tests matching a pattern
uv run pytest -k "test_data"

# Run tests in a specific directory
uv run pytest tests/

# Show test coverage (if pytest-cov is installed)
uv run pytest --cov=src
```

## Expected Output

You'll see organized test execution:

```
tests/test_data_processor.py::test_clean_data PASSED
tests/test_data_processor.py::test_validate_data PASSED
tests/test_model.py::test_train_model PASSED
tests/test_model.py::test_predict PASSED
```

## Try This

1. **Add new modules**: Create new source files and corresponding test files
2. **Reorganize**: Move tests around and see how pytest still finds them
3. **Modify config**: Change pytest.ini settings and observe the effects
4. **Add test utilities**: Create more helper functions in the utils module
5. **Test collections**: Run tests for specific modules or patterns

## pytest.ini Configuration Options

Key configuration options demonstrated:

- `testpaths`: Specify where to look for tests
- `python_files`: Patterns for test file names  
- `python_classes`: Patterns for test class names
- `python_functions`: Patterns for test function names
- `addopts`: Default command-line options
- `markers`: Define custom test markers

## Key Concepts from Chapter 7

- **Scalable organization** makes tests easier to find and maintain
- **Shared fixtures** reduce duplication across test modules
- **Configuration files** standardize testing behavior across the team
- **Test discovery** works best with consistent naming conventions
- **Modular design** allows for targeted test execution