# Basic marimo Notebook

This example demonstrates the basic structure of a marimo notebook as shown in Chapter 14.

## Files
- `my_notebook.py`: Basic marimo notebook with cell dependencies

## Key Features Demonstrated
- marimo notebook structure with `@app.cell` decorators
- Cell dependencies (the second cell depends on `data` from the first cell)
- Clean Python script format for version control
- Automatic return statements for variable passing between cells

## Running the Notebook

```bash
# Install marimo
uv run --group chapter14 pip install marimo

# Run the notebook
uv run --group chapter14 marimo edit my_notebook.py
```

The notebook will open in your browser. You can:
- Modify the `data` variable in the first cell
- See how the second cell automatically updates when dependencies change
- Save the notebook - it remains a clean `.py` file

## Features Shown

1. **Cell Structure**: Each cell is a function decorated with `@app.cell`
2. **Dependency Tracking**: The second cell automatically runs when `data` changes
3. **Variable Passing**: Variables are returned as tuples and passed to dependent cells
4. **Clean Storage**: The notebook is stored as a readable Python script