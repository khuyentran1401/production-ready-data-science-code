"""
Data Analysis Functions

Functions for analyzing pandas DataFrames that demonstrate
the need for shared test data through fixtures.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any


def get_dataframe_info(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Get basic information about a DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with shape, columns, and data types
    """
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.to_dict(),
        "memory_usage": df.memory_usage(deep=True).sum()
    }


def calculate_column_stats(df: pd.DataFrame, column: str) -> Dict[str, float]:
    """
    Calculate statistics for a numeric column.
    
    Args:
        df: Input DataFrame
        column: Column name to analyze
        
    Returns:
        Dictionary with mean, median, std, min, max
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' is not numeric")
    
    series = df[column].dropna()
    
    return {
        "mean": float(series.mean()),
        "median": float(series.median()),
        "std": float(series.std()),
        "min": float(series.min()),
        "max": float(series.max()),
        "count": len(series)
    }


def find_missing_values(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze missing values in a DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary with missing value information
    """
    missing_counts = df.isnull().sum()
    missing_percentages = (missing_counts / len(df)) * 100
    
    return {
        "missing_counts": missing_counts.to_dict(),
        "missing_percentages": missing_percentages.to_dict(),
        "total_missing": int(missing_counts.sum()),
        "columns_with_missing": list(missing_counts[missing_counts > 0].index)
    }


def filter_dataframe(df: pd.DataFrame, column: str, threshold: float, operation: str = "greater") -> pd.DataFrame:
    """
    Filter DataFrame based on column values.
    
    Args:
        df: Input DataFrame
        column: Column to filter on
        threshold: Threshold value
        operation: "greater", "less", "equal"
        
    Returns:
        Filtered DataFrame
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found")
    
    if operation == "greater":
        return df[df[column] > threshold].copy()
    elif operation == "less":
        return df[df[column] < threshold].copy()
    elif operation == "equal":
        return df[df[column] == threshold].copy()
    else:
        raise ValueError("Operation must be 'greater', 'less', or 'equal'")


def calculate_correlation_matrix(df: pd.DataFrame, numeric_only: bool = True) -> pd.DataFrame:
    """
    Calculate correlation matrix for DataFrame.
    
    Args:
        df: Input DataFrame
        numeric_only: Whether to include only numeric columns
        
    Returns:
        Correlation matrix as DataFrame
    """
    if numeric_only:
        numeric_df = df.select_dtypes(include=[np.number])
        if numeric_df.empty:
            raise ValueError("No numeric columns found")
        return numeric_df.corr()
    else:
        return df.corr()


def group_and_aggregate(df: pd.DataFrame, group_by: str, agg_column: str, agg_func: str = "mean") -> pd.DataFrame:
    """
    Group DataFrame and calculate aggregation.
    
    Args:
        df: Input DataFrame
        group_by: Column to group by
        agg_column: Column to aggregate
        agg_func: Aggregation function ("mean", "sum", "count", "max", "min")
        
    Returns:
        Grouped and aggregated DataFrame
    """
    if group_by not in df.columns:
        raise ValueError(f"Group column '{group_by}' not found")
    
    if agg_column not in df.columns:
        raise ValueError(f"Aggregation column '{agg_column}' not found")
    
    agg_functions = {
        "mean": "mean",
        "sum": "sum", 
        "count": "count",
        "max": "max",
        "min": "min"
    }
    
    if agg_func not in agg_functions:
        raise ValueError(f"Aggregation function must be one of: {list(agg_functions.keys())}")
    
    return df.groupby(group_by)[agg_column].agg(agg_functions[agg_func]).reset_index()