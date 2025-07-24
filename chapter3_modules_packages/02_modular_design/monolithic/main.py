# MONOLITHIC DESIGN: All functions in one file

def load_data():
    """Load raw data."""
    data = [1, 2, 3, 4, 5, None, 7, 8, 9, 10]
    print("Data loaded")
    return data


def clean_data(data):
    """Clean the data by removing None values."""
    cleaned = [x for x in data if x is not None]
    print("Data cleaned")
    return cleaned


def transform_data(data):
    """Transform data by multiplying each value by 2."""
    transformed = [x * 2 for x in data]
    print("Data transformed")
    return transformed


def save_results(data):
    """Save results to a file."""
    with open("results.txt", "w") as f:
        f.write(str(data))
    print("Results saved")


if __name__ == "__main__":
    # All processing steps in one file - harder to maintain and test
    raw_data = load_data()
    clean_data_result = clean_data(raw_data)
    transformed_data = transform_data(clean_data_result)
    save_results(transformed_data)
    
    print(f"Final result: {transformed_data}")
