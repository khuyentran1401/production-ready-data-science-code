# Test Organization and Structure

**Problem**: Data science projects often have scattered test files with unclear naming conventions, making it difficult to find relevant tests, run specific test suites, or maintain test coverage as projects grow.

Organize tests in a scalable, maintainable structure with proper directory layout and shared fixtures.

**Why This Matters**: Well-organized tests enable efficient development workflows, make it easy to run targeted test suites, and ensure comprehensive coverage of data science functionality.

## Files

- `pytest.ini` - pytest configuration and options
- `src/` - Source code modules
  - `data_processor.py` - Data processing functions
  - `model.py` - Machine learning model functions
- `tests/` - Test directory mirroring src/ structure
  - `conftest.py` - Shared fixtures for all tests
  - `test_data_processor.py` - Tests for data_processor.py
  - `test_model.py` - Tests for model.py
  - `utils/test_helpers.py` - Reusable test helper functions

## Key Points

- Test directory structure should mirror source code structure
- conftest.py centralizes shared fixtures and configuration

## How to Run

```bash
# Run all tests
uv run pytest -v

# Run specific test modules
uv run pytest tests/test_data_processor.py

# Run tests matching a pattern
uv run pytest -k "test_data"

# Show test coverage
uv run pytest --cov=src
```

## Expected Output

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

## Learn More

← [Back to Chapter 7](../README.md)

---

← [Previous: 05_mocking](../05_mocking/README.md)

*Example 6 of 6*