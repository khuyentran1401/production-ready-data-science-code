import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Variable Redefinition Error Demonstration
        
        This notebook demonstrates marimo's variable redefinition prevention feature. 
        marimo prevents you from accidentally redefining variables across different cells, 
        which eliminates bugs caused by naming collisions and makes notebook logic more predictable.
        
        ## The Problem in Traditional Notebooks
        
        In Jupyter notebooks, you can accidentally reuse variable names across cells, 
        leading to confusion about what data format you're working with and making 
        debugging more difficult.
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Example 1: Basic Variable Redefinition Error
        
        Let's start with the example from the book. Try to define the same variable `data` 
        in multiple cells and see how marimo prevents this error.
        """
    )
    return


@app.cell
def _():
    # Cell 1: Initial data definition
    data = [1, 2, 3]
    print(f"Original data: {data}")
    return (data,)


@app.cell
def _():
    # Cell 2: This cell will show an error because it tries to redefine 'data'
    # Uncomment the line below to see the error:
    # data = [4, 5, 6]
    
    # marimo will show: "This cell redefines variables from other cells"
    # 'data' was also defined by: cell-1
    
    print("This cell would cause a redefinition error if we uncommented the data assignment")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Example 2: Real-World Data Transformation Scenario
        
        This example shows a common scenario where you might accidentally redefine 
        variables during data preprocessing - exactly like the book's example with 
        date transformations.
        """
    )
    return


@app.cell
def _(pd):
    # Cell 1: Initial data loading with date column
    df = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'value': [100, 200, 300]
    })
    df['date'] = pd.to_datetime(df['date'])  # datetime object
    print("Initial data with datetime:")
    print(df.dtypes)
    print(f"Date type: {type(df['date'].iloc[0])}")
    return (df,)


@app.cell
def _():
    # Cell 2: This would cause a redefinition error
    # Uncomment the lines below to see the error:
    
    # df['date'] = df['date'].dt.date  # date object
    # print("After converting to date only:")
    # print(f"Date type: {type(df['date'].iloc[0])}")
    
    print("This cell would redefine 'df' if uncommented, causing marimo error")
    return


@app.cell
def _():
    # Cell 3: This would also cause a redefinition error
    # Uncomment the lines below to see the error:
    
    # df['date'] = df['date'].astype(str)  # string
    # print("After converting to string:")
    # print(f"Date type: {type(df['date'].iloc[0])}")
    
    print("This cell would also redefine 'df' if uncommented, causing marimo error")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Solution: Use Unique Variable Names
        
        The correct approach is to use descriptive, unique variable names for each 
        transformation step. This makes your code more readable and prevents 
        redefinition errors.
        """
    )
    return


@app.cell
def _(df):
    # Solution Cell 1: Convert to date only with new variable name
    df_date_only = df.copy()
    df_date_only['date'] = df_date_only['date'].dt.date
    print("Data with date only (using df_date_only):")
    print(f"Date type: {type(df_date_only['date'].iloc[0])}")
    return (df_date_only,)


@app.cell
def _(df_date_only):
    # Solution Cell 2: Convert to string with another new variable name
    df_date_string = df_date_only.copy()
    df_date_string['date'] = df_date_string['date'].astype(str)
    print("Data with date as string (using df_date_string):")
    print(f"Date type: {type(df_date_string['date'].iloc[0])}")
    print(df_date_string.head())
    return (df_date_string,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Alternative Solution: Private Variables
        
        You can also use private variables (prefixed with underscore) that stay 
        local to each cell. These variables are not shared between cells, so 
        redefinition is allowed.
        """
    )
    return


@app.cell
def _(df):
    # Private variable example - Cell 1
    _temp_df = df.copy()
    _temp_df['date'] = _temp_df['date'].dt.date
    
    # Create a new public variable for sharing
    processed_data_v1 = _temp_df
    print("Using private variable _temp_df (not shared)")
    print(f"Date type: {type(processed_data_v1['date'].iloc[0])}")
    return (processed_data_v1,)


@app.cell
def _(processed_data_v1):
    # Private variable example - Cell 2
    # We can reuse _temp_df here because it's private to this cell
    _temp_df = processed_data_v1.copy()
    _temp_df['date'] = _temp_df['date'].astype(str)
    
    # Create another new public variable for sharing
    processed_data_v2 = _temp_df
    print("Reusing private variable _temp_df (allowed)")
    print(f"Date type: {type(processed_data_v2['date'].iloc[0])}")
    return (processed_data_v2,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Benefits of marimo's Variable Redefinition Prevention
        
        1. **State tracking clarity**: You always know what format your variables are in
        2. **Easier debugging**: Clear variable names make it easy to track where errors occur
        3. **No broken dependencies**: Other cells won't fail unexpectedly due to variable format assumptions
        4. **Better code readability**: Descriptive variable names document your data transformations
        5. **Prevents silent bugs**: Catches redefinition errors before they cause problems downstream
        
        ## Summary
        
        marimo's variable redefinition prevention transforms a common source of bugs 
        into a helpful constraint that leads to better, more maintainable code.
        """
    )
    return


if __name__ == "__main__":
    app.run()