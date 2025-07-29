# Main Blocks

**Problem**: Data science modules often execute expensive computations (model training, data processing) during import, slowing down testing and making modules unusable as libraries.

Use `if __name__ == "__main__":` to control when code executes in Python modules.

**Why This Matters**: Main blocks allow data science scripts to be both executable programs and importable libraries, enabling code reuse without unwanted side effects.

## Files

- `without_main/` - Shows problems without main blocks
  - `main.py` - Imports process_data module
  - `process_data.py` - Code runs during import (unintended)
- `with_main/` - Shows correct approach with main blocks
  - `main.py` - Imports process_data module  
  - `process_data.py` - Code only runs when executed directly

## Key Points

- Main blocks prevent code execution during import
- Modules can serve as both libraries and scripts

## How to Run

```bash
# See the problem
cd without_main && uv run main.py

# See the solution
cd ../with_main && uv run main.py
```

## Expected Output

Without main blocks: Code runs twice (during import + execution)
With main blocks: Code runs only when intended

## Try This

1. **Import both modules**: See which has side effects during import
2. **Add print statements**: Track when code executes
3. **Test in REPL**: Import modules interactively to see the difference
4. **Create dual-purpose modules**: Make files work as both library and script

## Learn More

← [Back to Chapter 3](../README.md) for more modules and packages patterns and the complete guide.