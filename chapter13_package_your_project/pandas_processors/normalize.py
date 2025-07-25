"""
Data normalization utilities.

This module provides classes for normalizing pandas DataFrames.
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Dict


class MinMaxNormalizer:
    """
    Normalizer that scales features to a given range (default 0-1).
    
    Attributes:
        feature_range: Tuple of (min, max) for the target range
        data_min_: Dictionary storing minimum values for each column
        data_max_: Dictionary storing maximum values for each column
    """
    
    def __init__(self, feature_range: tuple = (0, 1)):
        """
        Initialize the normalizer.
        
        Args:
            feature_range: Desired range of transformed data as (min, max)
        """
        self.feature_range = feature_range
        self.data_min_ = {}
        self.data_max_ = {}
    
    def fit(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> "MinMaxNormalizer":
        """
        Learn the min and max values from the data.
        
        Args:
            df: DataFrame to learn from
            columns: List of columns to normalize. If None, uses all numeric columns.
            
        Returns:
            Self for method chaining
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns.tolist()
        
        self.data_min_ = {}
        self.data_max_ = {}
        
        for col in columns:
            if col in df.columns:
                self.data_min_[col] = df[col].min()
                self.data_max_[col] = df[col].max()
        
        return self
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply min-max normalization to the DataFrame.
        
        Args:
            df: DataFrame to normalize
            
        Returns:
            DataFrame with normalized values
            
        Raises:
            ValueError: If normalizer has not been fit yet
        """
        if not self.data_min_ or not self.data_max_:
            raise ValueError("Normalizer has not been fit yet. Call fit() first.")
        
        df_normalized = df.copy()
        min_val, max_val = self.feature_range
        
        for col in self.data_min_.keys():
            if col in df_normalized.columns:
                data_range = self.data_max_[col] - self.data_min_[col]
                if data_range == 0:
                    # Handle case where all values are the same
                    df_normalized[col] = min_val
                else:
                    # Apply min-max scaling formula
                    df_normalized[col] = (
                        (df_normalized[col] - self.data_min_[col]) / data_range
                    ) * (max_val - min_val) + min_val
        
        return df_normalized
    
    def fit_transform(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fit the normalizer and transform the data in one step.
        
        Args:
            df: DataFrame to fit and transform
            columns: List of columns to normalize
            
        Returns:
            DataFrame with normalized values
        """
        return self.fit(df, columns).transform(df)


class StandardNormalizer:
    """
    Normalizer that standardizes features by removing mean and scaling to unit variance.
    
    Also known as Z-score normalization.
    
    Attributes:
        mean_: Dictionary storing mean values for each column
        std_: Dictionary storing standard deviation values for each column
    """
    
    def __init__(self):
        """Initialize the normalizer."""
        self.mean_ = {}
        self.std_ = {}
    
    def fit(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> "StandardNormalizer":
        """
        Learn the mean and standard deviation from the data.
        
        Args:
            df: DataFrame to learn from
            columns: List of columns to normalize. If None, uses all numeric columns.
            
        Returns:
            Self for method chaining
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns.tolist()
        
        self.mean_ = {}
        self.std_ = {}
        
        for col in columns:
            if col in df.columns:
                self.mean_[col] = df[col].mean()
                self.std_[col] = df[col].std()
        
        return self
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply standard normalization to the DataFrame.
        
        Args:
            df: DataFrame to normalize
            
        Returns:
            DataFrame with standardized values
            
        Raises:
            ValueError: If normalizer has not been fit yet
        """
        if not self.mean_ or not self.std_:
            raise ValueError("Normalizer has not been fit yet. Call fit() first.")
        
        df_normalized = df.copy()
        
        for col in self.mean_.keys():
            if col in df_normalized.columns:
                if self.std_[col] == 0:
                    # Handle case where standard deviation is 0
                    df_normalized[col] = 0
                else:
                    # Apply z-score normalization
                    df_normalized[col] = (
                        df_normalized[col] - self.mean_[col]
                    ) / self.std_[col]
        
        return df_normalized
    
    def fit_transform(self, df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        Fit the normalizer and transform the data in one step.
        
        Args:
            df: DataFrame to fit and transform
            columns: List of columns to normalize
            
        Returns:
            DataFrame with standardized values
        """
        return self.fit(df, columns).transform(df)