# Wildcard Imports: Good vs Bad Practices

This example demonstrates the problems with **wildcard imports** (`from module import *`) and shows why **explicit imports** are much better for maintainable code.

## The Problem: Wildcard Imports

Using `from module import *` can cause:
- **Naming conflicts** when multiple modules have functions/classes with the same name
- **Unclear code** - it's not obvious where functions come from
- **Debugging difficulties** - hard to trace the source of functions
- **IDE issues** - poor autocomplete and error detection

## Files in This Example

### `processors.py`
Contains our custom processing classes and functions:
- `SimpleImputer` - Custom imputation class (different from sklearn's)
- `custom_scaler()` - Custom scaling function

### `process_data_bad.py` ❌
**Demonstrates problems with wildcard imports:**
```python
from processors import *        # Imports everything from processors
from sklearn.impute import *    # Imports everything from sklearn.impute
```

**Problems this causes:**
- Both modules have a `SimpleImputer` class
- Python uses the **last imported** version (sklearn's, not ours)
- It's unclear which version is being used
- This can lead to unexpected behavior

### `process_data_good.py` ✅  
**Shows the correct approach with explicit imports:**
```python
from processors import SimpleImputer    # Our custom SimpleImputer
from sklearn.impute import KNNImputer   # sklearn's KNNImputer
```

**Benefits:**
- Clear which `SimpleImputer` we're using (our custom one)
- No naming conflicts
- Code is self-documenting
- Easy to debug and maintain

## How to Run

### Run the bad example:
```bash
uv run process_data_bad.py
```

**Observe:** The output shows we're using sklearn's SimpleImputer instead of our custom one!

### Run the good example:
```bash
uv run process_data_good.py
```

**Observe:** Clear indication of which SimpleImputer is being used, and both imputers work as expected.

## Key Learning Points

### ❌ Problems with Wildcard Imports
- **Naming conflicts** - Later imports override earlier ones
- **Unclear origins** - Can't tell where functions come from
- **Debugging nightmares** - Hard to trace issues
- **Poor IDE support** - Less helpful autocomplete

### ✅ Benefits of Explicit Imports  
- **Clear intentions** - Obvious which module provides what
- **No conflicts** - Each import is explicitly named
- **Better debugging** - Easy to trace function sources
- **IDE friendly** - Better autocomplete and error detection
- **Self-documenting** - Code shows its dependencies clearly

## Best Practices

1. **Always use explicit imports:**
   ```python
   from module import specific_function, SpecificClass
   ```

2. **Use aliases for long names:**
   ```python
   from very_long_module_name import function as short_name
   ```

3. **Group imports logically** (see the import_grouping example)

4. **Avoid `import *` except in very specific cases** (like in `__init__.py` files for package exports)

## Try It Yourself

1. **Modify `processors.py`** - Add more functions and see how they interact
2. **Create your own conflict** - Make both modules have a function with the same name
3. **Practice explicit imports** - Import only what you need from each module