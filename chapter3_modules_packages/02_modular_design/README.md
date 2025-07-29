# Modular Design

**Problem**: Data science scripts often grow into thousand-line files that mix data loading, preprocessing, modeling, and evaluation, making them impossible to debug, test, or reuse.

Compare monolithic vs modular code approaches to see why breaking large files into focused modules improves maintainability.

**Why This Matters**: Modular design makes data science code testable, debuggable, and enables teams to work on different pipeline components independently.

## Files

- `monolithic/main.py` - All functionality in one file (70+ lines)
- `modular/` - Same functionality split across focused modules
  - `process.py` - Data loading and preprocessing
  - `train_model.py` - Model training and evaluation
  - `main.py` - Workflow coordination

## Key Points

- Focused modules make code easier to navigate and test
- Modular design improves reusability and team collaboration

## How to Run

```bash
# Monolithic approach
cd monolithic && uv run main.py

# Modular approach  
cd modular && uv run main.py
```

## Expected Output

Both approaches produce the same results, but modular is easier to maintain.

## Try This

1. **Compare file sizes**: Notice how modular breaks down complexity
2. **Test individual modules**: Import functions from modular version
3. **Add new features**: See which approach is easier to extend

## Learn More

← [Back to Chapter 3](../README.md) for more modules and packages patterns and the complete guide.
