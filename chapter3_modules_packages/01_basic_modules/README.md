# Basic Modules Example

This example demonstrates the fundamental concept of Python modules - creating reusable code in separate `.py` files and importing them into other modules.

## What This Example Shows

- **Creating a utility module** (`utils.py`) with shared configuration and functions
- **Importing specific items** from a module using `from module import item`
- **Using imported variables and functions** in another module
- **Basic file organization** for better code structure

## Files in This Example

### `utils.py`
Contains shared resources used across the project:
- `config`: A dictionary with common configuration settings
- `save_to_csv()`: A reusable function for saving DataFrames to CSV files

### `process_data.py`  
Demonstrates importing and using items from the utils module:
- Imports `save_to_csv` function and `config` dictionary from utils
- Creates sample data using pandas
- Uses the imported configuration to create directories
- Uses the imported function to save data

## How to Run

1. **Run the example:**
   ```bash
   uv run process_data.py
   ```

2. **Expected output:**
   ```
   Data is saved to data/mydata.csv
   ```

3. **Check the results:**
   - A `data/` directory will be created
   - The file `data/mydata.csv` will contain the sample data

## Key Learning Points

✅ **Modules are just `.py` files** - Any Python file can be imported as a module

✅ **Explicit imports are clear** - `from utils import save_to_csv, config` clearly shows what we're using

✅ **Shared configuration** - The `config` dictionary can be used across multiple modules

✅ **Code reusability** - The `save_to_csv` function can be used anywhere we need to save data

## Try It Yourself

1. **Modify the config:** Change the `data_path` in `utils.py` and see how it affects the output

2. **Add a new function:** Add a `load_from_csv()` function to `utils.py` and use it in `process_data.py`

3. **Create more data:** Modify `process_data.py` to create and save different datasets

4. **Add more configuration:** Extend the `config` dictionary with additional settings like file formats or column names