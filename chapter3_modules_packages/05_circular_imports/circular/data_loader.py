import pandas as pd

# PROBLEMATIC: Circular import
from data_processor import process_data


def load_data():
    """Load data from a CSV file and process it."""
    print("Loading data from dataset.csv...")

    # Create sample data since we don't have the actual file
    data = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", None],
        "age": [25, None, 35, 40],
        "salary": [50000, 60000, None, 80000]
    })

    print(f"Loaded {len(data)} rows")

    # This creates a circular dependency!
    # data_loader imports data_processor
    # data_processor imports data_loader (see data_processor.py)
    return process_data(data)
