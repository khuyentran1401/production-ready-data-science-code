# Chapter 3: Python Modules and Packages

This directory contains complete, runnable code examples from Chapter 3 of "Production-Ready Data Science: From Prototyping to Production with Python".

## Overview

Python modules and packages are essential for organizing code into reusable components. This chapter demonstrates:

- **What modules and packages are** and how they work
- **Project organization best practices** for maintainable code
- **Import best practices** to avoid common pitfalls
- **Code execution control** using main blocks
- **How to avoid circular dependencies**

## Examples Structure

Each example directory contains complete, functional code that you can run and modify to understand the concepts better.

### 📁 [01_basic_modules/](01_basic_modules/)
**Basic module usage and imports**
- Creating and using simple modules
- Importing functions and variables between modules
- **Run:** `cd 01_basic_modules && uv run process_data.py`

### 📁 [02_modular_design/](02_modular_design/)
**Breaking monolithic code into modules**
- Compare monolithic vs modular design
- Learn how to organize code by responsibility
- **Run monolithic:** `cd 02_modular_design/monolithic && uv run main.py`
- **Run modular:** `cd 02_modular_design/modular && uv run main.py`

### 📁 [03_import_practices/](03_import_practices/)
**Import best practices and pitfalls**
- Avoid wildcard imports and naming conflicts
- Proper import organization and grouping
- **Run bad example:** `cd 03_import_practices/wildcard_imports && uv run process_data_bad.py`
- **Run good example:** `cd 03_import_practices/wildcard_imports && uv run process_data_good.py`

### 📁 [04_main_blocks/](04_main_blocks/)
**Using main blocks for execution control**
- Compare code with and without main blocks
- Understand when and why code executes during import
- **Run without main:** `cd 04_main_blocks/without_main && uv run main.py`
- **Run with main:** `cd 04_main_blocks/with_main && uv run main.py`

### 📁 [05_circular_imports/](05_circular_imports/)
**Avoiding circular import problems**
- See how circular imports break your code
- Learn how to restructure to fix the problem
- **Run fixed version:** `cd 05_circular_imports/fixed && uv run main.py`

### 📁 [06_project_structure/](06_project_structure/)
**Standardized project structure template**
- Example of well-organized data science project structure
- Includes proper directory organization and configuration files
- **Run:** `cd 06_project_structure && uv sync && uv run scripts/run_pipeline.py`

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Navigate to any example directory and run the code:**
   ```bash
   cd 01_basic_modules
   uv run process_data.py
   ```

3. **Compare different approaches:** Many examples show both problematic and improved versions side-by-side.

## Key Takeaways

After working through these examples, you'll understand:

- ✅ How to create and use Python modules effectively
- ✅ Why breaking large files into smaller modules improves maintainability
- ✅ How to organize imports properly and avoid common pitfalls
- ✅ When and how to use main blocks for execution control
- ✅ How to structure data science projects for scalability
- ✅ How to avoid circular dependencies in your codebase

## Next Steps

Try modifying the examples to:
- Add new functions to existing modules
- Reorganize the project structures
- Practice importing from different module hierarchies
- Create your own modules following these patterns

---

💡 **Tip:** Each subdirectory contains its own README with specific instructions and explanations for that concept.