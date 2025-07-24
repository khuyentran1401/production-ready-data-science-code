def process_data(data):
    """Process the data by removing missing values."""
    print("Processing data (removing missing values)...")
    processed = data.dropna()
    print(f"Processed data: {len(processed)} rows remaining")
    return processed
