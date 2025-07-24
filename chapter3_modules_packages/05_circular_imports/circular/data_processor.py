# PROBLEMATIC: Circular import
from data_loader import load_data


def process_data(data):
    """Process the data by removing missing values."""
    print("Processing data (removing missing values)...")
    processed = data.dropna()
    print(f"Processed data: {len(processed)} rows remaining")
    return processed


def main():
    """Main function that tries to load and process data."""
    print("Starting data processing pipeline...")

    # This creates a circular dependency!
    # data_processor imports data_loader
    # data_loader imports data_processor
    # This can lead to ImportError or unexpected behavior
    data = load_data()

    print("Final processed data:")
    print(data)
    return data


if __name__ == "__main__":
    main()
