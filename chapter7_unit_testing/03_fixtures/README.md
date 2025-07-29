# Fixtures for Shared Test Data

**Problem**: Data science tests often require expensive setup (loading datasets, training models, connecting to databases) that gets duplicated across multiple test functions, making tests slow and hard to maintain.

Use pytest fixtures to share test data and setup code across multiple tests, eliminating duplication.

**Why This Matters**: Fixtures eliminate duplicate setup code, speed up test execution, and ensure consistent test data across your data science test suite.

## Files

- `data_analyzer.py` - Functions that work with pandas DataFrames
- `test_data_analyzer.py` - Tests using local fixtures
- `test_advanced_analysis.py` - Tests using shared fixtures from conftest.py
- `conftest.py` - Shared fixtures available to all tests

## Key Points

- Fixtures eliminate duplicate setup code with automatic dependency injection
- conftest.py makes fixtures available across multiple test files

## How to Run

```bash
# Run all tests
uv run pytest -v

# See fixture setup/teardown in action
uv run pytest -v -s

# Show available fixtures
uv run pytest --fixtures test_data_analyzer.py
```

## Expected Output

```
test_data_analyzer.py::test_dataframe_shape PASSED
test_data_analyzer.py::test_column_statistics PASSED
test_data_analyzer.py::test_missing_values PASSED
test_advanced_analysis.py::test_sales_analysis PASSED
```

## Try This

1. **Modify fixtures**: Change the sample data in fixtures and see how tests adapt
2. **Add new fixtures**: Create fixtures for different types of test data
3. **Test fixture scopes**: Change fixture scopes and observe the behavior
4. **Break fixtures**: Introduce errors in fixture setup to see how tests fail
5. **Add teardown**: Use yield in fixtures to add cleanup code

## Learn More

← [Back to Chapter 7](../README.md) for more testing patterns and the complete testing guide.