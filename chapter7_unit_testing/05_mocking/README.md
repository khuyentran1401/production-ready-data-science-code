# Mocking External Dependencies

**Problem**: Data science tests often depend on external services (APIs, databases, file systems) that are slow, unreliable, or unavailable during testing, making tests fragile and slow.

Use mocking to test functions that depend on external services without actually connecting to them.

**Why This Matters**: Mocking enables fast, reliable data science tests by simulating external dependencies, allowing you to test your logic without waiting for databases or API calls.

## Files

- `data_fetcher.py` - Functions that depend on external services
- `test_data_fetcher.py` - Tests using mocking to isolate dependencies
- `test_mock_examples.py` - Various mocking techniques and patterns

## Key Points

- Mocking isolates your code from external dependencies
- Tests run faster and more reliably without external calls

## How to Run

```bash
# Run all mocking tests
uv run pytest -v

# Run with output to see mock calls
uv run pytest -v -s
```

## Expected Output

```
test_data_fetcher.py::test_fetch_user_data_success PASSED
test_data_fetcher.py::test_fetch_user_data_not_found PASSED
test_data_fetcher.py::test_database_connection_error PASSED
test_mock_examples.py::test_mock_return_value PASSED
```

Tests pass without any actual external calls.

## Try This

1. **Remove mocks**: Comment out mock setups to see how tests fail
2. **Add assertions**: Check that mocks were called with correct parameters
3. **Mock different layers**: Try mocking at different levels of the call stack
4. **Test error paths**: Use `side_effect` to test various error conditions
5. **Verify interactions**: Use `assert_called_with()` to verify mock usage

## Learn More

← [Back to Chapter 7](../README.md) for more testing patterns and the complete testing guide.