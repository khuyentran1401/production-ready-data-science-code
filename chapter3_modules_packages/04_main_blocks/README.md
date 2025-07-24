# Main Blocks: Controlling Code Execution

This section demonstrates the importance of **main blocks** (`if __name__ == "__main__":`) for controlling when code executes in Python modules.

## The Problem and Solution

Python modules can serve two purposes:
1. **Libraries** - Imported by other modules to use their functions/classes
2. **Scripts** - Executed directly to perform tasks

Without main blocks, it's impossible to write code that behaves differently in these two scenarios.

## Examples in This Directory

### 📁 [without_main/](without_main/) ❌
**Shows the problems of not using main blocks**

- Code executes immediately during import
- Unwanted side effects when importing
- Functions run multiple times unexpectedly
- Confusing and unpredictable behavior

**Run to see the problem:**
```bash
cd without_main
uv run main.py
```

**What happens:**
- `process_data.py` code runs during import
- `main.py` code runs when executed
- Result: Code executes twice!

### 📁 [with_main/](with_main/) ✅
**Shows the correct approach using main blocks**

- Code only runs when module is executed directly
- Clean imports with no side effects
- Modules can be both imported and executed
- Clear, predictable behavior

**Run to see the solution:**
```bash
cd with_main  
uv run main.py
```

**What happens:**
- Only `main.py` code runs
- Importing `process_data` has no side effects
- Result: Clean, controlled execution

## Key Concepts

### What is `__name__`?

`__name__` is a built-in Python variable that changes based on how the module is used:

- **When run directly:** `__name__ == "__main__"`
- **When imported:** `__name__ == "module_name"`

### How Main Blocks Work

```python
if __name__ == "__main__":
    # This code ONLY runs when the file is executed directly
    # It does NOT run when the file is imported
    main_function()
    run_tests()
    do_setup()
```

## Compare the Outputs

### Without Main Blocks:
```bash
$ uv run without_main/main.py
Process data from process_data    # ❌ Unintended execution
Processed result: [2, 3, 4]      # ❌ Unintended execution  
Process data from __main__        # ✅ Intended execution
Main result: [5, 6, 7]           # ✅ Intended execution
```

### With Main Blocks:
```bash
$ uv run with_main/main.py
Process data from __main__        # ✅ Only intended execution
Main result: [5, 6, 7]           # ✅ Clean, controlled output
```

## When to Use Main Blocks

### ✅ Always Use Main Blocks For:
- Script initialization code
- Test code and examples
- Command-line argument parsing
- Setting up logging or configuration
- Any code that should only run when script is executed

### ✅ Keep Outside Main Blocks:
- Function and class definitions
- Constants and configuration
- Import statements
- Any code that needs to be available when imported

## Best Practices

1. **Structure your modules like this:**
   ```python
   # Imports
   import os
   import sys
   
   # Constants
   DEFAULT_CONFIG = {...}
   
   # Functions and classes
   def my_function():
       pass
   
   class MyClass:
       pass
   
   # Main block
   if __name__ == "__main__":
       # Script-specific code here
       main()
   ```

2. **Make modules dual-purpose** - They should work both as libraries and scripts

3. **Test your imports** - Import your modules to ensure no unwanted side effects

4. **Use descriptive main functions** - Create a `main()` function and call it from the main block

## Benefits Summary

| Aspect | Without Main Blocks | With Main Blocks |
|--------|-------------------|------------------|
| **Import behavior** | ❌ Executes code | ✅ No side effects |
| **Testing** | ❌ Hard to isolate | ✅ Easy to test |
| **Reusability** | ❌ Poor | ✅ Excellent |
| **Predictability** | ❌ Confusing | ✅ Clear |
| **Performance** | ❌ Slow imports | ✅ Fast imports |

## Try It Yourself

1. **Run both examples** and compare the outputs
2. **Import the modules** in Python REPL and see the difference
3. **Modify the code** to add more functionality
4. **Create your own modules** following the main block pattern