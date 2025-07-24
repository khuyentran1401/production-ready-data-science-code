# Circular Imports: Problem and Solution

This section demonstrates **circular import problems** and shows how to fix them using better code architecture. Circular imports are a common issue that can make your code fragile and hard to maintain.

## What Are Circular Imports?

Circular imports occur when two or more modules import each other, creating a dependency loop:

```
Module A → imports → Module B
    ↑                    ↓
    └─── imports ←───────┘
```

This creates problems because Python can't properly initialize modules that depend on each other.

## Examples in This Directory

### 📁 [circular/](circular/) ❌
**Demonstrates the circular import problem**

- `data_loader.py` imports from `data_processor.py`
- `data_processor.py` imports from `data_loader.py`
- Creates a circular dependency that can cause ImportError

**⚠️ Warning: May cause ImportError when run!**

**Try it (carefully):**
```bash
cd circular
uv run data_processor.py
```

### 📁 [fixed/](fixed/) ✅
**Shows the solution using coordinator pattern**

- `main.py` coordinates both modules
- `data_loader.py` and `data_processor.py` are independent
- Clean, linear dependencies with no cycles

**Run the working solution:**
```bash
cd fixed
uv run main.py
```

## The Problem in Detail

### Common Circular Import Scenarios

1. **Model-Service circular dependency:**
   ```python
   # models.py
   from services import UserService
   
   # services.py  
   from models import User
   ```

2. **Utility modules importing each other:**
   ```python
   # utils_a.py
   from utils_b import helper_function
   
   # utils_b.py
   from utils_a import another_helper
   ```

3. **Parent-child module dependencies:**
   ```python
   # parent.py
   from child import child_function
   
   # child.py
   from parent import parent_function
   ```

### Symptoms of Circular Imports

❌ **ImportError messages:**
```
ImportError: cannot import name 'function_name' from partially initialized module
```

❌ **AttributeError messages:**
```
AttributeError: partially initialized module has no attribute 'function_name'
```

❌ **Inconsistent behavior** - Code works sometimes, fails other times

❌ **Testing difficulties** - Can't import modules for testing

## The Solution: Coordinator Pattern

### Before (Circular):
```
data_loader.py ←→ data_processor.py
      ↑                ↓
      └── circular ────┘
```

### After (Fixed):
```
        main.py
       ↙        ↘
data_loader.py  data_processor.py
(independent)   (independent)
```

### Benefits of Coordinator Pattern

✅ **Eliminates circular dependencies** - Clean dependency tree

✅ **Single entry point** - Clear application structure

✅ **Easy testing** - Test each module independently

✅ **Better maintainability** - Changes don't cascade

✅ **Improved reusability** - Modules can be used elsewhere

## Alternative Solutions

### 1. Restructure Modules
**Move shared code to a separate module:**
```python
# common.py
def shared_function():
    pass

# module_a.py  
from common import shared_function

# module_b.py
from common import shared_function
```

### 2. Dependency Injection
**Pass dependencies as parameters:**
```python
# module_a.py
def process_data(data, processor_func):
    return processor_func(data)

# main.py
from module_a import process_data
from module_b import processor_function
result = process_data(data, processor_function)
```

### 3. Late Import
**Import inside functions (use sparingly):**
```python
def my_function():
    from other_module import needed_function  # Import when needed
    return needed_function()
```

### 4. Factory Pattern
**Create objects without direct imports:**
```python
# factory.py
def create_processor():
    from data_processor import DataProcessor
    return DataProcessor()
```

## Best Practices to Avoid Circular Imports

### ✅ Design Practices

1. **Plan your module hierarchy** - Draw dependency graphs
2. **Use single responsibility principle** - One purpose per module
3. **Prefer composition over inheritance** - Reduces tight coupling
4. **Create clear interfaces** - Define what modules expose

### ✅ Code Organization

1. **Keep utilities separate** - Don't mix business logic with utilities
2. **Use configuration modules** - Centralize settings
3. **Abstract common functionality** - Extract to base modules
4. **Minimize cross-imports** - Reduce module interdependencies

### ✅ Testing and Validation

1. **Test imports** - Run `python -c "import my_module"` for each module
2. **Use static analysis** - Tools like `import-linter` can detect cycles
3. **Review dependency graphs** - Visualize module relationships
4. **Refactor early** - Don't let circular dependencies accumulate

## Tools for Detection

### Find circular imports with Python:
```python
import importlib
import sys

def find_circular_imports():
    # Custom script to detect circular dependencies
    pass
```

### Use static analysis tools:
```bash
# Install import-linter
pip install import-linter

# Check for circular imports
lint-imports
```

## Key Takeaways

After working through these examples, you'll understand:

- ✅ **Why circular imports are problematic** and how they break Python's import system
- ✅ **How to identify circular import issues** from error messages and symptoms  
- ✅ **The coordinator pattern** as a robust solution for eliminating cycles
- ✅ **Alternative approaches** for different scenarios
- ✅ **Best practices** for designing modules to avoid circular dependencies
- ✅ **Tools and techniques** for detecting and preventing circular imports

## Next Steps

1. **Audit your current code** - Look for circular dependencies
2. **Refactor problem areas** - Apply the coordinator pattern
3. **Establish coding standards** - Prevent future circular imports
4. **Use static analysis tools** - Automate detection
5. **Plan module architecture** - Design dependencies upfront