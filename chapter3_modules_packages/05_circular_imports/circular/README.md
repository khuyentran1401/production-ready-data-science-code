# Circular Imports - The Problem

This example demonstrates **circular imports** - a problematic pattern where two or more modules import each other, creating a dependency loop that can cause your program to fail.

## What Are Circular Imports?

Circular imports occur when:
- Module A imports from Module B
- Module B imports from Module A  
- This creates a dependency loop: A → B → A

## The Problem in This Example

### `data_loader.py`
```python
from data_processor import process_data  # Imports from data_processor

def load_data():
    # ... load data ...
    return process_data(data)  # Uses data_processor function
```

### `data_processor.py`  
```python
from data_loader import load_data  # Imports from data_loader

def main():
    data = load_data()  # Uses data_loader function
```

## Circular Dependency Chain

```
data_loader.py → imports → data_processor.py
      ↑                           ↓
      └─────────── imports ←──────┘
```

## How to See the Problem

**⚠️ Warning: This example may cause an ImportError!**

Try running:
```bash
uv run data_processor.py
```

## Possible Outcomes

Depending on your Python version and execution order, you might see:

### 1. ImportError
```
ImportError: cannot import name 'process_data' from partially initialized module 'data_processor'
```

### 2. AttributeError  
```
AttributeError: partially initialized module 'data_processor' has no attribute 'process_data'
```

### 3. Unexpected Behavior
- Functions may not be available when expected
- Modules may be partially initialized
- Code may work sometimes but fail other times

## Why This Happens

1. **Python imports modules once** and caches them
2. **During import**, Python starts executing the module
3. **If module A imports B**, Python starts loading B
4. **If B then imports A**, Python tries to use a partially loaded A
5. **This can cause errors** or unpredictable behavior

## Problems with Circular Imports

❌ **ImportError or AttributeError** - Modules fail to load properly

❌ **Unpredictable behavior** - Code may work sometimes, fail other times

❌ **Hard to debug** - Error messages are confusing

❌ **Testing issues** - Difficult to test modules in isolation

❌ **Maintenance nightmare** - Changes can break imports unexpectedly

❌ **Poor design** - Usually indicates tightly coupled, poorly structured code

## Signs You Have Circular Imports

- Import errors mentioning "partially initialized module"
- Code that works when run directly but fails when imported
- Mysterious AttributeErrors for functions that clearly exist
- Different behavior depending on which module you run first

## The Solution

Check out the **`../fixed/`** example to see how to restructure this code to eliminate circular dependencies using a coordinator pattern.

## Key Learning Points

- **Circular imports are bad design** - They indicate tightly coupled modules
- **Python can't handle true circular dependencies** - Will cause errors or unpredictable behavior
- **Good module design avoids this problem** - Each module should have a clear, single purpose
- **Use coordinator modules** to orchestrate interactions between independent modules
- **Plan your module dependencies** - Draw dependency graphs to avoid cycles