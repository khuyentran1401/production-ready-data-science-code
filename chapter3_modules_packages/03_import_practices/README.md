# Import Best Practices

This section demonstrates essential **import best practices** that make your Python code more maintainable, readable, and less error-prone.

## Why Import Practices Matter

Poor import practices can lead to:
- **Naming conflicts** and unexpected behavior
- **Unclear dependencies** and hard-to-debug code
- **Performance issues** from importing unnecessary modules
- **Maintenance nightmares** when refactoring code

## Examples in This Directory

### 📁 [wildcard_imports/](wildcard_imports/)
**Avoid wildcard imports and naming conflicts**

Shows the problems with `from module import *` and demonstrates why explicit imports are much better.

**Key lesson:** Wildcard imports can cause naming conflicts and make code unclear.

**Run the examples:**
```bash
# See the problem
cd wildcard_imports
uv run process_data_bad.py

# See the solution  
uv run process_data_good.py
```

### 📁 [import_grouping/](import_grouping/)
**Organize imports following PEP 8 standards**

Demonstrates proper import organization: standard library, third-party, and local imports grouped logically.

**Key lesson:** Well-organized imports make code more readable and maintainable.

**Run the example:**
```bash
cd import_grouping
uv run example.py
```

## Quick Reference: Import Best Practices

### ✅ DO: Use Explicit Imports
```python
from module import specific_function, SpecificClass
import module_name
```

### ❌ DON'T: Use Wildcard Imports
```python
from module import *  # Avoid this!
```

### ✅ DO: Group Imports Properly
```python
# Standard library imports
import os
import sys

# Third-party imports  
import pandas as pd
import numpy as np

# Local application imports
from myproject import mymodule
```

### ✅ DO: Use Aliases for Long Names
```python
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier as RFC
```

### ✅ DO: Sort Imports Alphabetically
```python
# Within each group, sort alphabetically
import json
import os
import sys
```

## Tools for Better Import Management

### isort - Automatic Import Sorting
```bash
pip install isort
isort your_file.py        # Sort imports in one file
isort .                   # Sort imports in all files
```

### flake8 - Import Linting
```bash
pip install flake8
flake8 your_file.py       # Check for import issues
```

## Common Import Anti-Patterns to Avoid

1. **Wildcard imports** - `from module import *`
2. **Circular imports** - Modules importing each other
3. **Unnecessary imports** - Importing modules you don't use
4. **Relative imports in applications** - Use absolute imports instead
5. **Imports inside functions** - Usually better at module level

## Key Takeaways

After working through these examples, you'll understand:

- ✅ Why explicit imports are clearer than wildcard imports
- ✅ How naming conflicts occur and how to avoid them
- ✅ The proper way to organize imports following PEP 8
- ✅ How good import practices improve code maintainability
- ✅ Tools that can help automate import organization

## Next Steps

Try applying these practices to your own code:
1. **Review your imports** - Look for wildcard imports to replace
2. **Organize existing imports** - Group and sort them properly  
3. **Use tools** like isort to automate the process
4. **Establish team standards** - Make sure everyone follows the same practices