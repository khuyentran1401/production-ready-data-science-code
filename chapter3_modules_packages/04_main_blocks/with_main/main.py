from process_data import process_data

if __name__ == "__main__":
    # This code only runs when main.py is executed directly
    print(f"Process data from {__name__}")
    result = process_data([4, 5, 6])
    print(f"Main result: {result}")
