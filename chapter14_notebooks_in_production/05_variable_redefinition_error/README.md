# Variable Redefinition Error Prevention

This example demonstrates marimo's powerful variable redefinition prevention feature, which eliminates a common source of bugs in traditional notebooks.

## The Problem

In Jupyter notebooks, you can accidentally reuse variable names across cells, leading to:

- **State tracking confusion**: You can't easily tell what format variables are in
- **Debugging complexity**: Tracking down errors becomes difficult 
- **Broken dependencies**: Other cells fail unexpectedly based on execution order

## Files

- `variable_redefinition_demo.py` - Interactive demonstration of variable redefinition prevention

## Key Features Demonstrated

### 1. Basic Redefinition Prevention
Shows how marimo prevents redefining the same variable (`data`) across multiple cells with the error message:
```
This cell redefines variables from other cells.
'data' was also defined by: cell-1
```

### 2. Real-World Data Transformation Scenario
Demonstrates the book's exact example where a `date` column undergoes multiple transformations:
- Initial: `pd.to_datetime(df['date'])` (datetime object)
- Step 2: `df['date'].dt.date` (date object) 
- Step 3: `df['date'].astype(str)` (string)

### 3. Solution Patterns
Shows two approaches to fix redefinition errors:

#### Unique Variable Names
```python
df_date_only = df.copy()
df_date_string = df_date_only.copy()
```

#### Private Variables
```python
_temp_df = df.copy()  # Private, not shared between cells
```

## How to Run

```bash
# Run the interactive notebook
uv run --group chapter14 marimo edit variable_redefinition_demo.py
```

## Expected Behavior

1. **Clean execution**: With commented redefinition lines, notebook runs smoothly
2. **Error demonstration**: Uncomment the redefinition lines to see marimo's error messages
3. **Solution showcase**: See how unique variable names and private variables solve the problem

## Interactive Experiments

### Trigger the Error
1. **Uncomment redefinition lines**: Remove `#` from lines that redefine `data` or `df`
2. **Observe error message**: See marimo's helpful error explanation
3. **Notice prevention**: Cell won't execute until you fix the naming conflict

### See the Solutions
1. **Unique names**: Notice how `df_date_only` and `df_date_string` work perfectly
2. **Private variables**: See how `_temp_df` can be reused across cells
3. **Clear dependencies**: Observe how each cell cleanly depends on the previous step

## Benefits Demonstrated

- **Clarity**: Always know what format your variables are in
- **Maintainability**: Descriptive names document your transformations  
- **Reliability**: No silent bugs from unexpected variable redefinition
- **Debugging**: Easy to track where transformations happen
- **Dependencies**: Clear cell-to-cell relationships

## Comparison with Jupyter

| Aspect | Jupyter Notebooks | marimo |
|--------|------------------|---------|
| Variable redefinition | Allowed (causes bugs) | Prevented (shows error) |
| State tracking | Difficult | Clear |
| Debugging | Complex | Straightforward |
| Dependencies | Hidden/broken | Explicit |

## Learn More

← [Back to Chapter 14](../README.md) for more notebook patterns and production-ready techniques.