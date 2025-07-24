from data_loader import load_data
from data_processor import process_data


def main():
    """Main function that coordinates data loading and processing."""
    print("Starting data processing pipeline...")

    # Load data using data_loader module
    raw_data = load_data()

    # Process data using data_processor module
    processed_data = process_data(raw_data)

    print("\nFinal processed data:")
    print(processed_data)
    print(f"\nProcessing complete! Final dataset has {len(processed_data)} rows.")

    return processed_data


if __name__ == "__main__":
    main()
