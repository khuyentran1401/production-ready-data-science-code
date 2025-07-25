# Basic Testing with pytest

This example demonstrates the fundamentals of unit testing with pytest, comparing the benefits of structured testing vs simple print statements.

## What This Example Shows

- **pytest basics**: Writing test functions, assertions, and test discovery
- **Test structure**: Organizing tests with descriptive names
- **Comparison**: Benefits of testing over print statements for debugging
- **Practical example**: Testing sentiment analysis functions

## Files

- `sentiment_analyzer.py` - Functions for sentiment analysis (code to test)
- `test_sentiment_analyzer.py` - pytest test functions
- `test_with_print.py` - Shows problems with print-based testing

## Key Learning Points

1. **Test Discovery**: pytest automatically finds files starting with `test_` and functions starting with `test_`
2. **Assertions**: Use `assert` statements to verify expected behavior
3. **Test Isolation**: Each test function runs independently
4. **Clear Feedback**: pytest provides detailed failure information

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

## Key Concepts from Chapter 7

- Tests provide **automated verification** that code works as intended
- Tests help **identify edge cases** that manual testing might miss
- Tests enable **safe refactoring** by catching regressions
- Tests serve as **living documentation** showing how functions should behave