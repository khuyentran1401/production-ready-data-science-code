# Basic Testing with pytest

Write your first pytest tests and see why structured testing beats print statements for debugging.

## Files

- `sentiment_analyzer.py` - Functions for sentiment analysis (code to test)
- `test_sentiment_analyzer.py` - pytest test functions
- `test_with_print.py` - Shows problems with print-based testing

## Key Points

- pytest automatically finds test files and functions
- Use `assert` statements to verify expected behavior

## How to Run

```bash
# Run all tests in this directory
uv run pytest -v

# Run a specific test file
uv run pytest test_sentiment_analyzer.py -v

# Run a specific test function
uv run pytest test_sentiment_analyzer.py::test_extract_sentiment_positive -v
```

## Expected Output

When running `uv run pytest -v`, you should see:

```
test_sentiment_analyzer.py::test_extract_sentiment_positive PASSED
test_sentiment_analyzer.py::test_extract_sentiment_negative PASSED
test_sentiment_analyzer.py::test_extract_sentiment_neutral PASSED
```

## Try This

1. **Modify a test**: Change an expected value in a test to see how pytest reports failures
2. **Add a test**: Create a new test function for additional edge cases
3. **Break the code**: Introduce a bug in `sentiment_analyzer.py` to see how tests catch it
4. **Compare approaches**: Run `test_with_print.py` to see why structured testing is better

## Learn More

← [Back to Chapter 7](../README.md) for more testing patterns and the complete testing guide.