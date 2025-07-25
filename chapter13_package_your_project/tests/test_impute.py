"""
Tests for the impute module.
"""

import pytest
import pandas as pd
import numpy as np
from pandas_processors.impute import MeanMedianImputer, SimpleImputer


class TestMeanMedianImputer:
    """Test the MeanMedianImputer class."""
    
    def test_mean_imputer_init(self):
        """Test initializing mean imputer."""
        imputer = MeanMedianImputer(strategy="mean")
        assert imputer.strategy == "mean"
        assert imputer.fill_values_ == {}
    
    def test_median_imputer_init(self):
        """Test initializing median imputer."""
        imputer = MeanMedianImputer(strategy="median")
        assert imputer.strategy == "median"
    
    def test_invalid_strategy(self):
        """Test that invalid strategy raises ValueError."""
        with pytest.raises(ValueError, match="Strategy must be either 'mean' or 'median'"):
            MeanMedianImputer(strategy="invalid")
    
    def test_mean_imputer_fit_transform(self):
        """Test mean imputer fit and transform."""
        df = pd.DataFrame({
            "A": [1, 2, np.nan, 4],
            "B": [np.nan, 2, 3, 4],
            "C": ["a", "b", "c", "d"]  # Non-numeric column
        })
        
        imputer = MeanMedianImputer(strategy="mean")
        result = imputer.fit_transform(df)
        
        # Check that numeric columns are imputed
        assert not result["A"].isnull().any()
        assert not result["B"].isnull().any()
        assert result.loc[2, "A"] == 2.33333333  # Mean of [1, 2, 4] is 2.333...
        assert result.loc[0, "B"] == 3.0  # Mean of [2, 3, 4] is 3.0
        
        # Check that non-numeric column is unchanged
        assert result["C"].equals(df["C"])
    
    def test_median_imputer_fit_transform(self):
        """Test median imputer fit and transform."""
        df = pd.DataFrame({
            "A": [1, 2, np.nan, 4, 5],
            "B": [np.nan, 1, 2, 3, 10]
        })
        
        imputer = MeanMedianImputer(strategy="median")
        result = imputer.fit_transform(df)
        
        # Check that values are filled with median
        assert result.loc[2, "A"] == 2.5  # Median of [1, 2, 4, 5] is 2.5
        assert result.loc[0, "B"] == 2.5   # Median of [1, 2, 3, 10] is 2.5
    
    def test_fit_transform_with_columns(self):
        """Test imputer with specific columns."""
        df = pd.DataFrame({
            "A": [1, np.nan, 3],
            "B": [np.nan, 2, 3],
            "C": [1, 2, np.nan]
        })
        
        imputer = MeanMedianImputer(strategy="mean")
        result = imputer.fit_transform(df, columns=["A", "B"])
        
        # A and B should be imputed
        assert not result["A"].isnull().any()
        assert not result["B"].isnull().any()
        
        # C should still have missing value
        assert result["C"].isnull().any()
    
    def test_transform_without_fit_raises_error(self):
        """Test that transform without fit raises ValueError."""
        df = pd.DataFrame({"A": [1, np.nan, 3]})
        imputer = MeanMedianImputer()
        
        with pytest.raises(ValueError, match="Imputer has not been fit yet"):
            imputer.transform(df)


class TestSimpleImputer:
    """Test the SimpleImputer class."""
    
    def test_simple_imputer_init_default(self):
        """Test SimpleImputer initialization with default value."""
        imputer = SimpleImputer()
        assert imputer.fill_value == 0
    
    def test_simple_imputer_init_custom(self):
        """Test SimpleImputer initialization with custom value."""
        imputer = SimpleImputer(fill_value=-999)
        assert imputer.fill_value == -999
    
    def test_simple_imputer_transform(self):
        """Test SimpleImputer transform method."""
        df = pd.DataFrame({
            "A": [1, np.nan, 3],
            "B": [np.nan, 2, 3],
            "C": ["x", np.nan, "z"]
        })
        
        imputer = SimpleImputer(fill_value=-1)
        result = imputer.transform(df)
        
        assert not result["A"].isnull().any()
        assert not result["B"].isnull().any()
        assert not result["C"].isnull().any()
        assert result.loc[1, "A"] == -1
        assert result.loc[0, "B"] == -1
        assert result.loc[1, "C"] == -1
    
    def test_simple_imputer_with_columns(self):
        """Test SimpleImputer with specific columns."""
        df = pd.DataFrame({
            "A": [1, np.nan, 3],
            "B": [np.nan, 2, 3],
            "C": [1, np.nan, 3]
        })
        
        imputer = SimpleImputer(fill_value=999)
        result = imputer.transform(df, columns=["A", "C"])
        
        # A and C should be imputed
        assert not result["A"].isnull().any()
        assert not result["C"].isnull().any()
        assert result.loc[1, "A"] == 999
        assert result.loc[1, "C"] == 999
        
        # B should still have missing value
        assert result["B"].isnull().any()