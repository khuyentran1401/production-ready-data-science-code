"""
DataFrame creation utilities.

This module provides functions for creating pandas DataFrames with various data patterns.
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional


def create_dataframe(data: Dict[str, List[Any]], index: Optional[List] = None) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a dictionary of column data.
    
    Args:
        data: Dictionary where keys are column names and values are lists of data
        index: Optional list of index values
        
    Returns:
        pandas DataFrame created from the input data
        
    Example:
        >>> data = {"name": ["Alice", "Bob"], "age": [25, 30]}
        >>> df = create_dataframe(data)
        >>> print(df)
           name  age
        0  Alice   25
        1    Bob   30
    """
    return pd.DataFrame(data, index=index)


def create_sample_data(n_rows: int = 100, n_cols: int = 5, 
                      missing_rate: float = 0.1, random_state: int = 42) -> pd.DataFrame:
    """
    Create sample DataFrame with numeric data and optional missing values.
    
    Args:
        n_rows: Number of rows to generate
        n_cols: Number of columns to generate  
        missing_rate: Proportion of values to make missing (0.0 to 1.0)
        random_state: Random seed for reproducibility
        
    Returns:
        pandas DataFrame with sample numeric data
        
    Example:
        >>> df = create_sample_data(n_rows=10, n_cols=3, missing_rate=0.2)
        >>> print(df.shape)
        (10, 3)
    """
    np.random.seed(random_state)
    
    # Generate random numeric data
    data = np.random.randn(n_rows, n_cols)
    
    # Create column names
    columns = [f"feature_{i+1}" for i in range(n_cols)]
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)
    
    # Add missing values
    if missing_rate > 0:
        n_missing = int(n_rows * n_cols * missing_rate)
        missing_indices = np.random.choice(
            df.size, size=n_missing, replace=False
        )
        
        # Convert flat indices to row, col indices
        row_indices = missing_indices // n_cols
        col_indices = missing_indices % n_cols
        
        for row, col in zip(row_indices, col_indices):
            df.iloc[row, col] = np.nan
    
    return df