# Mocking External Dependencies

This example demonstrates how to use mocking to test functions that depend on external services like databases, APIs, or file systems without actually connecting to them.

## What This Example Shows

- **pytest-mock basics**: Using the `mocker` fixture for mocking
- **Mocking return values**: Controlling what mocked functions return
- **Mocking side effects**: Simulating errors and exceptions
- **Patching**: Replacing external dependencies in tests
- **Isolation**: Testing your code logic without external dependencies

## Files

- `data_fetcher.py` - Functions that depend on external services
- `test_data_fetcher.py` - Tests using mocking to isolate dependencies
- `test_mock_examples.py` - Various mocking techniques and patterns

## Key Learning Points

1. **Isolation**: Mocking isolates your code from external dependencies
2. **Reliability**: Tests run consistently without network/database issues
3. **Speed**: Mocked tests run much faster than real external calls
4. **Error Testing**: You can easily test error scenarios
5. **pytest-mock**: Provides convenient mocking utilities for pytest

## How to Run

```bash
# Run all mocking tests
uv run pytest -v

# Run with output to see mock calls
uv run pytest -v -s

# Run specific test file
uv run pytest test_data_fetcher.py -v

# Show mock call details
uv run pytest --tb=short -v
```

## Expected Output

You'll see tests passing without any actual external calls:

```
test_data_fetcher.py::test_fetch_user_data_success PASSED
test_data_fetcher.py::test_fetch_user_data_not_found PASSED
test_data_fetcher.py::test_database_connection_error PASSED
test_mock_examples.py::test_mock_return_value PASSED
```

## Try This

1. **Remove mocks**: Comment out mock setups to see how tests fail
2. **Add assertions**: Check that mocks were called with correct parameters
3. **Mock different layers**: Try mocking at different levels of the call stack
4. **Test error paths**: Use `side_effect` to test various error conditions
5. **Verify interactions**: Use `assert_called_with()` to verify mock usage

## Common Mocking Patterns

### Mock Return Values
```python
mocker.patch('module.function', return_value='mocked_result')
```

### Mock Side Effects (Errors)
```python
mocker.patch('module.function', side_effect=Exception('Test error'))
```

### Mock with Different Values
```python
mocker.patch('module.function', side_effect=[value1, value2, Exception()])
```

### Verify Mock Calls
```python
mock_func.assert_called_once_with(expected_args)
```

## Key Concepts from Chapter 7

- **Mocking** enables testing of code with external dependencies
- **Isolation** makes tests faster, more reliable, and deterministic
- **Error simulation** allows testing of failure scenarios
- **Mock verification** ensures your code interacts correctly with dependencies