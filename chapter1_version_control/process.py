"""
Simple data processing script for Git demonstration
"""

def process_data():
    """Process sample data"""
    data = [1, 2, 3, 4, 5]
    processed = [x * 2 for x in data]
    return processed

def main():
    """Main processing function"""
    print("Processing data...")
    result = process_data()
    print(f"Result: {result}")

if __name__ == "__main__":
    main()