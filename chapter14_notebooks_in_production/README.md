# Chapter 14: Notebooks in Production Examples

This directory contains examples for using marimo notebooks in production as demonstrated in Chapter 14 of the book.

## Examples Overview

### 1. Basic marimo Notebook (`01_basic_marimo_notebook/`)
- Introduction to marimo notebook structure
- Cell dependencies and variable passing
- Clean Python script storage format

### 2. Dependency Tracking (`02_dependency_tracking/`)
- Automatic cell re-execution when dependencies change
- Chain of dependent cells
- Interactive parameter adjustment

### 3. Data Analysis Workflow (`03_data_analysis_workflow/`)
- Complete data science workflow
- Data exploration, visualization, and analysis
- Real-time updates throughout the pipeline

### 4. Testing Notebook (`04_testing_notebook/`)
- Testable functions within notebooks
- pytest integration for CI/CD
- Inline test execution and verification

## Prerequisites

Install dependencies using:
```bash
uv sync --group chapter14
pip install marimo  # marimo is not in uv yet, install with pip
```

## Key Concepts Covered

### 1. **Problems with Traditional Jupyter Notebooks**
- **Hidden State**: Variables can be modified in any order
- **Out-of-Order Execution**: Cells can run in wrong sequence
- **Version Control Issues**: JSON format is hard to diff and merge
- **Testing Challenges**: Difficult to integrate with standard testing tools

### 2. **marimo Solutions**
- **Automatic Dependency Tracking**: Cells re-run automatically when dependencies change
- **Top-to-Bottom Execution**: Enforces reproducible execution order
- **Plain Python Scripts**: Stored as `.py` files for clean version control
- **Variable Isolation**: Prevents accidental variable redefinition
- **Standard Testing**: Works with pytest and CI/CD pipelines

### 3. **marimo Notebook Structure**
```python
import marimo
app = marimo.App()

@app.cell
def cell_1():
    # Cell logic here
    variable = "value"
    return (variable,)  # Return variables for other cells

@app.cell  
def cell_2(variable):  # Automatically receives dependencies
    # Uses variable from cell_1
    result = process(variable)
    return (result,)

if __name__ == "__main__":
    app.run()
```

### 4. **Export Formats**
marimo notebooks can be exported to multiple formats:
```bash
marimo export html my_notebook.py           # Static HTML report
marimo export html-wasm my_notebook.py      # Interactive web app
marimo export ipynb my_notebook.py          # Jupyter notebook
marimo export md my_notebook.py             # Markdown document  
marimo export script my_notebook.py         # Pure Python script
```

## Running the Examples

### Interactive Mode
```bash
# Navigate to any example directory
cd 01_basic_marimo_notebook/

# Open the notebook in browser
marimo edit my_notebook.py
```

### Testing Mode  
```bash
# Run tests on notebook files
pytest 04_testing_notebook/test_example.py
```

### Export Examples
```bash
# Export as HTML report
marimo export html 03_data_analysis_workflow/data_analysis.py

# Export as interactive web app
marimo export html-wasm 03_data_analysis_workflow/data_analysis.py
```

## Benefits for Production

### 1. **Reproducibility**
- **Deterministic Execution**: Always runs cells in the correct order
- **No Hidden State**: Clear variable dependencies prevent bugs
- **Consistent Results**: Same output every time

### 2. **Version Control**
- **Clean Diffs**: Python script format shows meaningful changes
- **Easy Merging**: Standard text file conflicts resolution
- **Code Reviews**: Reviewable like any Python code

### 3. **Testing & CI/CD**
- **Standard Testing**: Use pytest directly on notebook files  
- **CI Integration**: Standard Python testing workflows work
- **Quality Assurance**: Automated testing in deployment pipelines

### 4. **Collaboration**
- **Team-Friendly**: No JSON merge conflicts
- **Code Standards**: Follows Python conventions and formatting
- **Sharing**: Easy to share as scripts or interactive apps

## Best Practices Demonstrated

1. **Cell Design**: Keep cells focused and return relevant variables
2. **Dependency Management**: Design clear variable flows between cells
3. **Function Definition**: Create testable functions within cells
4. **Documentation**: Use docstrings and comments for clarity
5. **Testing**: Include test functions for critical logic
6. **Export Strategy**: Choose appropriate export format for use case

## Migration from Jupyter

For teams moving from Jupyter to marimo:
1. **Convert Existing Notebooks**: Use marimo's conversion tools
2. **Refactor Cell Dependencies**: Clean up variable flows
3. **Add Tests**: Include test functions for critical analysis
4. **Update CI/CD**: Use standard pytest commands
5. **Train Team**: marimo enforces good practices automatically