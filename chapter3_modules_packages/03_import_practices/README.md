# Import Best Practices

**Problem**: Data science projects often use wildcard imports (`from pandas import *`) that create mysterious bugs when function names collide, and disorganized imports make dependencies unclear.

Essential import practices that make Python code more maintainable and avoid naming conflicts.

**Why This Matters**: Clean import practices prevent hard-to-debug naming conflicts and make data science code dependencies explicit and maintainable.

## Files

- `wildcard_imports/` - Shows problems with `from module import *`
  - `process_data_bad.py` - Demonstrates naming conflicts
  - `process_data_good.py` - Shows explicit import solution
- `import_grouping/example.py` - Proper import organization following PEP 8

## Key Points

- Use explicit imports instead of wildcard imports
- Group imports: standard library, third-party, then local imports

## How to Run

```bash
# See the problem with wildcard imports
uv run wildcard_imports/process_data_bad.py

# See the solution with explicit imports  
uv run wildcard_imports/process_data_good.py

# See proper import grouping
uv run import_grouping/example.py
```

## Expected Output

Both approaches work, but explicit imports prevent naming conflicts and improve code clarity.

## Try This

1. **Break the imports**: Add conflicting function names to see wildcard problems
2. **Reorganize imports**: Practice grouping imports by type
3. **Use tools**: Try `isort` and `flake8` for automated import management

## Learn More

← [Back to Chapter 3](../README.md)

---

← [Previous: 02_modular_design](../02_modular_design/README.md) | **Next:** [04_main_blocks →](../04_main_blocks/README.md)

*Example 3 of 6*