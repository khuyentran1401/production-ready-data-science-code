# Basic Modules

Create reusable code in separate `.py` files and import them into other modules.

## Files

- `utils.py` - Shared configuration and CSV saving function
- `process_data.py` - Imports and uses utilities from utils module

## Key Points

- Modules are just `.py` files that can be imported
- Use explicit imports to clearly show dependencies

## How to Run

```bash
uv run process_data.py
```

## Expected Output

```
Data is saved to data/mydata.csv
```

A `data/` directory will be created with the CSV file.

## Learn More

← [Back to Chapter 3](../README.md) for more modules and packages patterns and the complete guide.
