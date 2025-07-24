# Without Main Block - The Problem

This example demonstrates what happens when you **don't use main blocks** in your Python modules. Code executes immediately during import, leading to unintended behavior.

## The Problem

Without main blocks (`if __name__ == "__main__":`), any code at the module level executes immediately when the module is imported, not just when it's run directly.

## Files in This Example

### `process_data.py`
Contains a function and **problematic code** that runs immediately:
```python
def process_data(data: list):
    return [num + 1 for num in data]

# PROBLEM: This code runs immediately when imported!
print(f"Process data from {__name__}")
result = process_data([1, 2, 3])
print(f"Processed result: {result}")
```

### `main.py`  
Imports from `process_data.py` and also calls the function:
```python
from process_data import process_data

print(f"Process data from {__name__}")
result = process_data([4, 5, 6])
print(f"Main result: {result}")
```

## How to Run and See the Problem

```bash
uv run main.py
```

## Expected Output (Problematic!)

```
Process data from process_data
Processed result: [2, 3, 4]
Process data from __main__
Main result: [5, 6, 7]
```

## What's Happening?

1. **Import triggers execution** - When `main.py` imports `process_data`, the module-level code in `process_data.py` runs immediately
2. **Function runs twice** - Once during import, once in main
3. **Unintended behavior** - We didn't mean for `process_data([1, 2, 3])` to run during import
4. **Confusing output** - It's unclear when and why code is executing

## Problems This Causes

❌ **Unintended execution** - Code runs when you just want to import functions

❌ **Performance issues** - Heavy computations happen during import

❌ **Hard to test** - Can't import functions without triggering side effects

❌ **Confusing behavior** - Unclear when code will execute

❌ **Import side effects** - Importing a module changes program state

## The Solution

Check out the **`../with_main/`** example to see how main blocks solve these problems by controlling when code executes.

## Key Learning Points

- **Module-level code runs immediately** when a module is imported
- **This can cause unintended side effects** and confusing behavior  
- **Main blocks control execution** and separate importable code from script behavior
- **Always use main blocks** for code that should only run when the script is executed directly