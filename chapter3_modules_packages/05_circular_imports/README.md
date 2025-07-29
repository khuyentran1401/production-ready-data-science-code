# Circular Imports

**Problem**: Data science pipelines with interdependent modules (data loader needs preprocessor, preprocessor needs data loader) create circular import errors that prevent code execution.

Demonstrates circular import problems and shows how to fix them using the coordinator pattern.

**Why This Matters**: Avoiding circular imports keeps data science pipelines modular and prevents mysterious ImportError crashes that are hard to debug.

## Files

- `circular/` - Shows the circular import problem
  - `data_loader.py` - Imports from data_processor.py
  - `data_processor.py` - Imports from data_loader.py (⚠️ causes ImportError)
- `fixed/` - Shows the coordinator pattern solution
  - `main.py` - Coordinates both modules independently
  - `data_loader.py` - Independent data loading
  - `data_processor.py` - Independent data processing

## Key Points

- Circular imports create dependency loops that can cause ImportError
- Use coordinator pattern to eliminate circular dependencies

## How to Run

```bash
# See the problem (may cause ImportError)
cd circular && uv run data_processor.py

# See the solution
cd ../fixed && uv run main.py
```

## Expected Output

Circular version may fail with ImportError. Fixed version runs cleanly with coordinator pattern.

## Try This

1. **Break the cycle**: Try importing the circular modules in Python REPL
2. **Add more complexity**: See how circular imports get worse with more modules
3. **Test independently**: Import fixed modules separately to verify independence
4. **Draw dependency graphs**: Visualize the before/after module relationships

## Learn More

← [Back to Chapter 3](../README.md) for more modules and packages patterns and the complete guide.