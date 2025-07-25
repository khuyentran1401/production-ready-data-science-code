import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    # Data processing functions that can be tested
    def calculate_average(numbers):
        """Calculate the average of a list of numbers."""
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    
    def filter_positive(numbers):
        """Filter out negative numbers from a list."""
        return [x for x in numbers if x > 0]
    
    return (calculate_average, filter_positive)


@app.cell
def _(calculate_average, filter_positive):
    # Example usage of the functions
    test_data = [-2, -1, 0, 1, 2, 3, 4, 5]
    
    positive_numbers = filter_positive(test_data)
    average = calculate_average(positive_numbers)
    
    print(f"Original data: {test_data}")
    print(f"Positive numbers: {positive_numbers}")
    print(f"Average of positive numbers: {average}")
    
    return (test_data, positive_numbers, average)


@app.cell
def _():
    # Test functions - these can be run with pytest
    def test_calculate_average():
        """Test the calculate_average function."""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([10]) == 10.0
        assert calculate_average([]) == 0
        assert calculate_average([-1, 0, 1]) == 0.0
    
    def test_filter_positive():
        """Test the filter_positive function."""
        assert filter_positive([1, 2, 3]) == [1, 2, 3]
        assert filter_positive([-1, 0, 1]) == [1]
        assert filter_positive([-5, -3, -1]) == []
        assert filter_positive([]) == []
    
    return (test_calculate_average, test_filter_positive)


@app.cell
def _(test_calculate_average, test_filter_positive):
    # Run tests within the notebook to verify they pass
    try:
        test_calculate_average()
        print("✓ test_calculate_average passed")
    except AssertionError as e:
        print(f"✗ test_calculate_average failed: {e}")
    
    try:
        test_filter_positive()
        print("✓ test_filter_positive passed")
    except AssertionError as e:
        print(f"✗ test_filter_positive failed: {e}")
    
    print("\nNote: This notebook can also be tested with: pytest test_example.py")
    return


if __name__ == "__main__":
    app.run()