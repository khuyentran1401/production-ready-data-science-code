def process_data(data: list):
    """Process a list of numbers by adding 1 to each."""
    return [num + 1 for num in data]

if __name__ == "__main__":
    # This code only runs when process_data.py is executed directly
    print(f"Process data from {__name__}")
    result = process_data([1, 2, 3])
    print(f"Processed result: {result}")
