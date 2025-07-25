# Dependency Tracking Example

This example demonstrates marimo's automatic dependency tracking as shown in Chapter 14.

## Files
- `filtering_example.py`: Notebook showing automatic cell updates when dependencies change

## Key Features Demonstrated
- Automatic dependency detection and re-execution
- Chain of dependent cells (Cell 1 → Cell 2 → Cell 3)
- Real-time updates when threshold value changes

## Running the Example

```bash
# Run the notebook
uv run --group chapter14 marimo edit filtering_example.py
```

## Interactive Demo

1. **Initial State**: 
   - `threshold = 30`
   - Filtered data shows values > 30: [40, 50, 60, 70, 80, 90]

2. **Change Threshold**: 
   - Modify `threshold` to `50` in Cell 1
   - marimo **automatically** reruns Cell 2 and Cell 3
   - Filtered data updates to show values > 50: [60, 70, 80, 90]
   - Statistics recalculate automatically

3. **Observe Dependency Chain**:
   - Cell 1 (threshold) → Cell 2 (filtering) → Cell 3 (statistics)
   - All dependent cells update in correct order automatically

## Benefits Shown
- **No Manual Re-execution**: marimo handles cell dependencies automatically  
- **Correct Order**: Cells always run in the right sequence
- **No Hidden State**: Clear dependency relationships prevent bugs
- **Interactive Analysis**: Change parameters and see immediate results