# Circular Imports - The Solution

This example shows how to **fix circular import problems** by restructuring code to eliminate circular dependencies. The solution uses a **coordinator pattern** where a main module orchestrates the interaction between independent modules.

## The Solution: Coordinator Pattern

Instead of modules importing each other, we use a coordinator (`main.py`) that:
- Imports functions from both modules
- Orchestrates their interaction
- Eliminates circular dependencies

## Fixed Architecture

```
main.py
├── imports → data_loader.py
└── imports → data_processor.py

data_loader.py (no imports to data_processor)
data_processor.py (no imports to data_loader)
```

## Files in This Example

### `data_loader.py` ✅
**Independent module focused on data loading:**
```python
import pandas as pd

def load_data():
    # ... load data logic ...
    return data  # Returns data without processing it
```

**Key points:**
- No imports from other project modules
- Single responsibility: loading data
- Returns raw data for others to process

### `data_processor.py` ✅  
**Independent module focused on data processing:**
```python
def process_data(data):
    # ... process data logic ...
    return processed_data
```

**Key points:**
- No imports from other project modules
- Single responsibility: processing data
- Accepts data as parameter instead of loading it

### `main.py` ✅
**Coordinator that orchestrates the workflow:**
```python
from data_loader import load_data
from data_processor import process_data

def main():
    raw_data = load_data()        # Get data from data_loader
    processed_data = process_data(raw_data)  # Process with data_processor
    return processed_data
```

**Key points:**
- Imports from both modules (but they don't import each other)
- Coordinates the workflow
- Passes data between modules explicitly

## How to Run

```bash
uv run main.py
```

## Expected Output

```
Starting data processing pipeline...
Loading data from dataset.csv...
Loaded 4 rows
Processing data (removing missing values)...
Processed data: 2 rows remaining

Final processed data:
     name  age   salary
0   Alice   25  50000.0
2  Charlie   35      NaN

Processing complete! Final dataset has 2 rows.
```

## Benefits of This Approach

✅ **No circular dependencies** - Clean, linear dependency flow

✅ **Clear separation of concerns** - Each module has one responsibility

✅ **Easy to test** - Test each module independently

✅ **Maintainable** - Changes to one module don't break others

✅ **Reusable** - Modules can be used in other projects

✅ **Predictable** - Clear execution flow and dependencies

## Comparison with Circular Version

| Aspect | Circular (Bad) | Fixed (Good) |
|--------|----------------|--------------|
| **Dependencies** | A↔B circular | main→A, main→B linear |
| **Testing** | Hard to isolate | Easy to test each module |
| **Errors** | ImportError risk | No import issues |
| **Reusability** | Tightly coupled | Loosely coupled |
| **Maintainability** | Fragile | Robust |

## Design Principles Applied

1. **Single Responsibility** - Each module does one thing well
2. **Dependency Inversion** - High-level module (main) depends on low-level modules
3. **Loose Coupling** - Modules don't directly depend on each other
4. **Explicit Dependencies** - Data flow is clear and explicit

## When to Use This Pattern

✅ **Use coordinator pattern when:**
- You have modules that need to work together
- The workflow has a clear sequence of steps
- You want to avoid tight coupling between modules
- You need a clear entry point for your application

## Alternative Solutions

If the coordinator pattern doesn't fit your use case, consider:

1. **Dependency injection** - Pass dependencies as parameters
2. **Factory pattern** - Create objects without direct imports
3. **Observer pattern** - Use events instead of direct calls
4. **Restructuring** - Merge modules or extract common functionality

## Key Takeaways

- **Circular imports indicate design problems** - Fix the design, not just the imports
- **Use coordinators** to orchestrate independent modules
- **Keep modules focused** - Single responsibility principle
- **Make dependencies explicit** - Pass data between modules clearly
- **Test the pattern** - Each module should be testable in isolation