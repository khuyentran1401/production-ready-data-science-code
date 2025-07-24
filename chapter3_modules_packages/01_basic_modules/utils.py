# Configuration dictionary
config = {"data_path": "data", "model_path": "model"}

# CSV saving function
def save_to_csv(file_name, result):
    result.to_csv(file_name, index=False)
    print(f"Data is saved to {file_name}")
