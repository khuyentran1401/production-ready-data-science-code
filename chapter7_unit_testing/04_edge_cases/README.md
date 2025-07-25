# Testing Edge Cases and Error Conditions

This example demonstrates how to test boundary conditions, edge cases, and error handling to ensure your code behaves correctly in unexpected situations.

## What This Example Shows

- **Boundary testing**: Testing with empty inputs, null values, and extreme values
- **Error handling**: Using `pytest.raises` to test exceptions
- **Input validation**: Testing type checking and data validation
- **Edge case identification**: Common edge cases in data science functions

## Files

- `calculator.py` - Mathematical and data processing functions with edge cases
- `test_calculator.py` - Comprehensive edge case tests
- `test_error_scenarios.py` - Tests focused on error conditions and exception handling

## Key Learning Points

1. **Edge Cases Matter**: Real-world data often contains unexpected values
2. **Defensive Programming**: Functions should handle invalid inputs gracefully
3. **pytest.raises**: Essential tool for testing exception handling
4. **Boundary Values**: Test minimum, maximum, and boundary conditions
5. **Type Safety**: Verify functions handle incorrect data types appropriately

## How to Run

```bash
# Run all edge case tests
uv run pytest -v

# Run tests with detailed output for failures
uv run pytest -v --tb=long

# Run only error handling tests
uv run pytest test_error_scenarios.py -v

# Run tests and show which edge cases are covered
uv run pytest --tb=short -v
```

## Expected Output

You'll see tests covering various edge cases:

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

## Common Edge Cases in Data Science

### Numerical Data
- Empty datasets
- Single data points
- All identical values
- Extreme outliers
- Missing values (NaN, None)
- Infinite values
- Zero and negative values

### Text Data
- Empty strings
- Very long strings
- Special characters
- Unicode characters
- Whitespace-only strings

### DataFrames
- Empty DataFrames
- Single-row/single-column DataFrames
- Missing entire columns
- Mixed data types
- Memory constraints

## Key Concepts from Chapter 7

- **Edge case testing** prevents bugs that only appear with unusual inputs
- **Exception testing** ensures errors are handled gracefully
- **Boundary value analysis** identifies critical test points
- **Input validation testing** protects against invalid data