# Dependency Tracking Example

marimo's automatic dependency tracking with chain of dependent cells.

## Files

- `filtering_example.py` - Notebook showing automatic cell updates when dependencies change

## Key Points

- Chain of dependent cells (Cell 1 → Cell 2 → Cell 3)
- Real-time updates when threshold value changes

## How to Run

```bash
# Run the notebook
uv run --group chapter14 marimo edit filtering_example.py
```

## Expected Output

Notebook displays filtering example where changing the threshold in Cell 1 automatically updates filtering in Cell 2 and statistics in Cell 3.

## Try This

1. **Change threshold**: Modify `threshold` from `30` to `50` in Cell 1
2. **Watch cascade**: See marimo automatically rerun Cell 2 and Cell 3
3. **Observe order**: Notice all dependent cells update in correct sequence
4. **Test interactivity**: Try different threshold values and see immediate results

## Learn More

← [Back to Chapter 14](../README.md)

---

← [Previous: 01_basic_marimo_notebook](../01_basic_marimo_notebook/README.md) | **Next:** [03_data_analysis_workflow →](../03_data_analysis_workflow/README.md)

*Example 2 of 5*