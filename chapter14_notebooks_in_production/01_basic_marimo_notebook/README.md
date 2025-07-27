# Basic marimo Notebook

Basic structure of a marimo notebook with cell dependencies.

## Files

- `my_notebook.py` - Basic marimo notebook with cell dependencies

## Key Points

- Each cell is a function decorated with `@app.cell`
- Cells automatically update when dependencies change

## How to Run

```bash
# Install marimo
uv run --group chapter14 pip install marimo

# Run the notebook
uv run --group chapter14 marimo edit my_notebook.py
```

## Expected Output

Notebook opens in browser showing two cells where the second cell automatically updates when the first cell's `data` variable changes.

## Try This

1. **Modify data**: Change the `data` variable in the first cell
2. **Watch updates**: See how the second cell automatically updates when dependencies change
3. **Save changes**: Notice the notebook remains a clean `.py` file

## Learn More

← [Back to Chapter 14](../README.md) for more notebook patterns and the complete guide.