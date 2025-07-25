# Parametrization with pytest

This example demonstrates how to use `@pytest.mark.parametrize` to efficiently test multiple scenarios with the same test logic.

## What This Example Shows

- **Parametrization basics**: Testing multiple inputs with one test function
- **Input-output pairs**: Testing expected results for different inputs
- **Multiple parameters**: Combining different parameter sets
- **Efficient testing**: Reducing code duplication in tests

## Files

- `text_processor.py` - Text processing functions to test
- `test_text_processor.py` - Parametrized tests demonstrating different approaches
- `test_without_parametrization.py` - Shows repetitive approach without parametrization

## Key Learning Points

1. **DRY Principle**: Parametrization eliminates duplicate test code
2. **Multiple Test Cases**: One test function can validate many scenarios
3. **Clear Test Names**: pytest generates descriptive names for each parameter set
4. **Easy Maintenance**: Adding new test cases requires minimal code changes

## How to Run

```bash
# Run all parametrized tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest test_text_processor.py -v

# Run just the parametrized sentiment tests
uv run pytest test_text_processor.py::test_text_sentiment_parametrized -v
```

## Expected Output

You'll see pytest generate separate test cases for each parameter:

```
test_text_processor.py::test_text_sentiment_parametrized[I love this-positive] PASSED
test_text_processor.py::test_text_sentiment_parametrized[I hate this-negative] PASSED
test_text_processor.py::test_text_sentiment_parametrized[This is okay-neutral] PASSED
test_text_processor.py::test_word_count_parametrized[hello world-2] PASSED
test_text_processor.py::test_word_count_parametrized[one-1] PASSED
test_text_processor.py::test_word_count_parametrized[-0] PASSED
```

## Try This

1. **Add test cases**: Add new parameter sets to existing parametrized tests
2. **Combine parameters**: Create tests with multiple `@pytest.mark.parametrize` decorators
3. **Compare approaches**: Look at `test_without_parametrization.py` to see the difference
4. **Test edge cases**: Add boundary conditions and special cases to parameter lists

## Key Concepts from Chapter 7

- **Parametrization** reduces test code duplication while improving coverage
- **Multiple scenarios** can be tested efficiently with single test functions
- **Test maintenance** becomes easier when adding new cases
- **Test readability** improves with descriptive parameter names