import pandas as pd


def load_data():
    """Load data from a CSV file."""
    print("Loading data from dataset.csv...")

    # Create sample data since we don't have the actual file
    data = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", None],
        "age": [25, None, 35, 40],
        "salary": [50000, 60000, None, 80000]
    })

    print(f"Loaded {len(data)} rows")
    return data
