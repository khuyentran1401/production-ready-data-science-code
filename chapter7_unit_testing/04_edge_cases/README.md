# Testing Edge Cases and Error Conditions

**Problem**: Data science functions often work on sample data but fail in production with edge cases like empty datasets, missing values, or unexpected data types that weren't considered during development.

Test boundary conditions, edge cases, and error handling to ensure code behaves correctly in unexpected situations.

**Why This Matters**: Edge case testing prevents production failures by ensuring data science functions handle real-world data anomalies gracefully.

## Files

- `calculator.py` - Mathematical and data processing functions with edge cases
- `test_calculator.py` - Comprehensive edge case tests
- `test_error_scenarios.py` - Tests focused on error conditions and exception handling

## Key Points

- Edge cases reveal bugs that only appear with unusual inputs
- Use `pytest.raises` to test exception handling

## How to Run

```bash
# Run all edge case tests
uv run pytest -v

# Run only error handling tests
uv run pytest test_error_scenarios.py -v
```

## Expected Output

```
test_calculator.py::test_divide_by_zero PASSED
test_calculator.py::test_empty_list_average PASSED
test_calculator.py::test_negative_numbers PASSED
test_calculator.py::test_very_large_numbers PASSED
test_error_scenarios.py::test_invalid_input_types PASSED
```

## Try This

1. **Add edge cases**: Think of additional boundary conditions to test
2. **Break the functions**: Remove error handling to see how tests catch issues
3. **Test with real data**: Use actual messy data to find more edge cases
4. **Performance edges**: Test with very large or very small datasets
5. **Precision issues**: Test floating-point calculations for accuracy

## Learn More

← [Back to Chapter 7](../README.md) for more testing patterns and the complete testing guide.