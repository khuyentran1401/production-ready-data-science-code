# Parametrization with pytest

Use `@pytest.mark.parametrize` to efficiently test multiple scenarios with the same test logic.

## Files

- `text_processor.py` - Text processing functions to test
- `test_text_processor.py` - Parametrized tests demonstrating different approaches
- `test_without_parametrization.py` - Repetitive approach without parametrization

## Key Points

- Parametrization eliminates duplicate test code
- pytest generates descriptive names for each parameter set

## How to Run

```bash
# Run all parametrized tests
uv run pytest -v

# Run specific parametrized test
uv run pytest test_text_processor.py::test_text_sentiment_parametrized -v
```

## Expected Output

```
test_text_processor.py::test_text_sentiment_parametrized[I love this-positive] PASSED
test_text_processor.py::test_text_sentiment_parametrized[I hate this-negative] PASSED
test_text_processor.py::test_text_sentiment_parametrized[This is okay-neutral] PASSED
test_text_processor.py::test_word_count_parametrized[hello world-2] PASSED
```

## Try This

1. **Add test cases**: Add new parameter sets to existing parametrized tests
2. **Combine parameters**: Create tests with multiple `@pytest.mark.parametrize` decorators
3. **Compare approaches**: Look at `test_without_parametrization.py` to see the difference
4. **Test edge cases**: Add boundary conditions and special cases to parameter lists

## Learn More

← [Back to Chapter 7](../README.md) for more testing patterns and the complete testing guide.