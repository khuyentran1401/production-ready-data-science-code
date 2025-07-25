"""
Data imputation utilities.

This module provides classes for handling missing values in pandas DataFrames.
"""

import pandas as pd
import numpy as np
from typing import Union, List, Optional


class MeanMedianImputer:
    """
    Imputer that fills missing values with mean or median.
    
    This is the class mentioned in the book that users can import:
    from pandas_processors.impute import MeanMedianImputer
    
    Attributes:
        strategy: Either "mean" or "median"
        fill_values_: Dictionary storing computed fill values for each column
    """
    
    def __init__(self, strategy: str = "mean"):
        """
        Initialize the imputer.
        
        Args:
            strategy: Strategy for imputation, either "mean" or "median"
            
        Raises:
            ValueError: If strategy is not "mean" or "median"
        """
        if strategy not in ["mean", "median"]:
            raise ValueError("Strategy must be either 'mean' or 'median'")
        
        self.strategy = strategy
        self.fill_values_ = {}
    
    def fit(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> "MeanMedianImputer":
        """
        Learn the fill values from the data.
        
        Args:
            df: DataFrame to learn from
            columns: List of columns to impute. If None, uses all numeric columns.
            
        Returns:
            Self for method chaining
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns.tolist()
        
        self.fill_values_ = {}
        
        for col in columns:
            if col in df.columns:
                if self.strategy == "mean":
                    self.fill_values_[col] = df[col].mean()
                else:  # median
                    self.fill_values_[col] = df[col].median()
        
        return self
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply the imputation to the DataFrame.
        
        Args:
            df: DataFrame to impute
            
        Returns:
            DataFrame with missing values filled
            
        Raises:
            ValueError: If imputer has not been fit yet
        """
        if not self.fill_values_:
            raise ValueError("Imputer has not been fit yet. Call fit() first.")
        
        df_imputed = df.copy()
        
        for col, fill_value in self.fill_values_.items():
            if col in df_imputed.columns:
                df_imputed[col] = df_imputed[col].fillna(fill_value)
        
        return df_imputed
    
    def fit_transform(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fit the imputer and transform the data in one step.
        
        Args:
            df: DataFrame to fit and transform
            columns: List of columns to impute
            
        Returns:
            DataFrame with missing values filled
        """
        return self.fit(df, columns).transform(df)


class SimpleImputer:
    """
    Simple imputer that fills missing values with a constant value.
    
    Attributes:
        fill_value: Value to use for filling missing values
    """
    
    def __init__(self, fill_value: Union[int, float, str] = 0):
        """
        Initialize the imputer.
        
        Args:
            fill_value: Value to use for filling missing values
        """
        self.fill_value = fill_value
    
    def transform(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fill missing values with the specified fill value.
        
        Args:
            df: DataFrame to impute
            columns: List of columns to impute. If None, uses all columns.
            
        Returns:
            DataFrame with missing values filled
        """
        df_imputed = df.copy()
        
        if columns is None:
            columns = df.columns.tolist()
        
        for col in columns:
            if col in df_imputed.columns:
                df_imputed[col] = df_imputed[col].fillna(self.fill_value)
        
        return df_imputed