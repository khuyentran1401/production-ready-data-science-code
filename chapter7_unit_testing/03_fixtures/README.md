# Fixtures for Shared Test Data

This example demonstrates how to use pytest fixtures to share test data and setup code across multiple tests, eliminating duplication and improving maintainability.

## What This Example Shows

- **Basic fixtures**: Creating reusable test data with `@pytest.fixture`
- **Fixture scopes**: Function, module, and session-level fixtures
- **conftest.py**: Sharing fixtures across multiple test files
- **Setup and teardown**: Resource management with fixtures
- **Fixture dependencies**: Using fixtures that depend on other fixtures

## Files

- `data_analyzer.py` - Functions that work with pandas DataFrames
- `test_data_analyzer.py` - Tests using local fixtures
- `test_advanced_analysis.py` - Tests using shared fixtures from conftest.py
- `conftest.py` - Shared fixtures available to all tests

## Key Learning Points

1. **DRY Principle**: Fixtures eliminate duplicate setup code
2. **Automatic Cleanup**: Fixtures can handle resource cleanup automatically
3. **Dependency Injection**: pytest automatically provides fixtures to test functions
4. **Scope Management**: Control fixture lifecycle with scope parameters
5. **Shared Resources**: conftest.py makes fixtures available across test files

## How to Run

```bash
# Run all tests in this directory
uv run pytest -v

# See fixture setup/teardown in action
uv run pytest -v -s

# Run tests from specific file
uv run pytest test_data_analyzer.py -v

# Show fixture dependency graph (if pytest-dependency plugin installed)
uv run pytest --fixtures test_data_analyzer.py
```

## Expected Output

You'll see pytest automatically use fixtures:

```
test_data_analyzer.py::test_dataframe_shape PASSED
test_data_analyzer.py::test_column_statistics PASSED
test_data_analyzer.py::test_missing_values PASSED
test_advanced_analysis.py::test_sales_analysis PASSED
test_advanced_analysis.py::test_customer_segmentation PASSED
```

## Try This

1. **Modify fixtures**: Change the sample data in fixtures and see how tests adapt
2. **Add new fixtures**: Create fixtures for different types of test data
3. **Test fixture scopes**: Change fixture scopes and observe the behavior
4. **Break fixtures**: Introduce errors in fixture setup to see how tests fail
5. **Add teardown**: Use yield in fixtures to add cleanup code

## Key Concepts from Chapter 7

- **Fixtures centralize** test data preparation and reduce duplication
- **Setup and teardown** can be automated with fixture lifecycle management
- **Shared fixtures** in conftest.py make test data available across multiple files
- **Fixture scopes** control when fixtures are created and destroyed
- **Dependency injection** makes tests cleaner and more maintainable