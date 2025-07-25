# Chapter 7: Unit Testing

This directory contains complete, runnable code examples from Chapter 7 of "Production-Ready Data Science: From Prototyping to Production with Python".

## Overview

Unit testing is essential for ensuring your code works as intended, identifying edge cases, and enabling safe refactoring. This chapter demonstrates:

- **Basic pytest usage** and test structure
- **Parametrization** for testing multiple scenarios efficiently
- **Fixtures** for sharing test data and setup code
- **Edge case testing** for boundary conditions
- **Mocking** external dependencies like databases and APIs
- **Test organization** with proper directory structure

## Examples Structure

Each example directory contains complete, functional code that you can run and modify to understand the concepts better.

### 📁 [01_basic_testing/](01_basic_testing/)
**pytest fundamentals and test structure**
- Writing basic test functions with assertions
- Understanding test discovery and naming conventions
- Testing sentiment analysis functions
- **Run:** `uv sync --group chapter7 && cd 01_basic_testing && uv run pytest`

### 📁 [02_parametrization/](02_parametrization/)
**Testing multiple scenarios with parametrization**
- Using `@pytest.mark.parametrize` for efficient testing
- Testing with lists of input-output pairs
- Combining multiple parameters
- **Run:** `cd 02_parametrization && uv run pytest -v`

### 📁 [03_fixtures/](03_fixtures/)
**Shared test data and setup methods**
- Creating reusable test fixtures
- Using `conftest.py` for shared fixtures
- Setup and teardown with fixtures
- **Run:** `cd 03_fixtures && uv run pytest -v`

### 📁 [04_edge_cases/](04_edge_cases/)
**Testing boundary conditions and error handling**
- Testing empty inputs, null values, and extreme cases
- Verifying error handling with `pytest.raises`
- Testing data validation functions
- **Run:** `cd 04_edge_cases && uv run pytest -v`

### 📁 [05_mocking/](05_mocking/)
**Mocking external dependencies**
- Using `pytest-mock` to mock database connections
- Mocking API calls and file operations
- Testing error scenarios with mocked failures
- **Run:** `cd 05_mocking && uv run pytest -v`

### 📁 [06_test_organization/](06_test_organization/)
**Proper test directory structure**
- Organizing tests in separate directories
- Using `conftest.py` for project-wide fixtures
- Configuring pytest with `pytest.ini`
- **Run:** `cd 06_test_organization && uv run pytest`

## Getting Started

1. **Install dependencies:**
   ```bash
   uv sync --group chapter7
   ```

2. **Navigate to any example directory and run the tests:**
   ```bash
   cd 01_basic_testing
   uv run pytest -v
   ```

3. **Run all tests in the chapter:**
   ```bash
   uv run pytest chapter7_unit_testing/ -v
   ```

## Key Takeaways

After working through these examples, you'll understand:

- ✅ How to write effective unit tests with pytest
- ✅ When and how to use parametrization for comprehensive testing
- ✅ How to organize test data with fixtures
- ✅ How to test edge cases and error conditions
- ✅ How to mock external dependencies for isolated testing
- ✅ How to structure tests for maintainability and scalability

## Next Steps

Try modifying the examples to:
- Add new test cases to existing functions
- Create tests for your own data science functions
- Experiment with different fixture scopes and combinations
- Practice mocking different types of external dependencies
- Set up continuous integration to run these tests automatically

---

💡 **Tip:** Each subdirectory contains its own README with specific instructions and explanations for that testing concept.