# MODULAR DESIGN: Functions organized in separate modules
from data_loader import load_data
from data_processor import clean_data, transform_data
from file_utils import save_results

if __name__ == "__main__":
    # Same functionality but organized in separate modules - easier to maintain and test
    raw_data = load_data()
    clean_data_result = clean_data(raw_data)
    transformed_data = transform_data(clean_data_result)
    save_results(transformed_data)
    
    print(f"Final result: {transformed_data}")
