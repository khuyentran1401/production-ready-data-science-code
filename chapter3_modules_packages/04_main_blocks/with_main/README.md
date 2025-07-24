# With Main Block - The Solution

This example demonstrates the **correct approach** using main blocks (`if __name__ == "__main__":`) to control when code executes. This solves the problems shown in the "without_main" example.

## The Solution: Main Blocks

Main blocks ensure that code only runs when a module is executed directly, not when it's imported by another module.

## Files in This Example

### `process_data.py`  
Contains a function and **properly controlled code** using a main block:
```python
def process_data(data: list):
    return [num + 1 for num in data]

if __name__ == "__main__":
    # This code ONLY runs when process_data.py is executed directly
    print(f"Process data from {__name__}")
    result = process_data([1, 2, 3])
    print(f"Processed result: {result}")
```

### `main.py`
Imports from `process_data.py` and uses its own main block:
```python
from process_data import process_data

if __name__ == "__main__":
    # This code ONLY runs when main.py is executed directly
    print(f"Process data from {__name__}")
    result = process_data([4, 5, 6])
    print(f"Main result: {result}")
```

## How to Run

### Run main.py:
```bash
uv run main.py
```

**Output:**
```
Process data from __main__
Main result: [5, 6, 7]
```

### Run process_data.py directly:  
```bash
uv run process_data.py
```

**Output:**
```
Process data from __main__
Processed result: [2, 3, 4]
```

## What's Different?

1. **Clean imports** - Importing `process_data` no longer triggers unwanted code execution
2. **Controlled execution** - Code only runs when you explicitly execute the file
3. **Dual purpose modules** - Each module can be both imported and run directly
4. **Clear behavior** - It's obvious when and why code executes

## Benefits of Main Blocks

✅ **Prevents unwanted execution** - Code doesn't run during import

✅ **Clean imports** - Import functions without side effects

✅ **Better testing** - Import and test functions in isolation  

✅ **Dual-purpose modules** - Files can be both libraries and scripts

✅ **Clear intent** - Obvious what code runs when

✅ **Performance** - No unexpected computations during import

## How Main Blocks Work

```python
if __name__ == "__main__":
    # This condition is True only when:
    # 1. The file is run directly (python myfile.py)
    # 
    # This condition is False when:
    # 1. The file is imported (from myfile import function)
```

- `__name__` is a built-in variable
- When a file is run directly: `__name__ == "__main__"`  
- When a file is imported: `__name__ == "module_name"`

## Compare with the Problem

Run the **`../without_main/main.py`** example to see the difference:
- **Without main blocks**: Code runs during import (problematic)
- **With main blocks**: Code only runs when intended (correct)

## Best Practices

1. **Always use main blocks** for script-specific code
2. **Keep functions outside** the main block so they can be imported
3. **Put initialization code** inside the main block
4. **Make modules dual-purpose** - importable and executable
5. **Test by importing** your modules to ensure no side effects

## Try It Yourself

1. **Import the module** in Python REPL: `from process_data import process_data`
2. **Notice no output** - the main block code doesn't run
3. **Call the function** directly: `process_data([7, 8, 9])`
4. **Compare** with the "without_main" version