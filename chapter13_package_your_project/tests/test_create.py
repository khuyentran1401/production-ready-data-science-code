"""
Tests for the create module.
"""

import pytest
import pandas as pd
import numpy as np
from pandas_processors.create import create_dataframe, create_sample_data


class TestCreateDataFrame:
    """Test the create_dataframe function."""
    
    def test_create_basic_dataframe(self):
        """Test creating a basic DataFrame."""
        data = {"name": ["Alice", "Bob"], "age": [25, 30]}
        df = create_dataframe(data)
        
        assert isinstance(df, pd.DataFrame)
        assert list(df.columns) == ["name", "age"]
        assert len(df) == 2
        assert df.loc[0, "name"] == "Alice"
        assert df.loc[1, "age"] == 30
    
    def test_create_dataframe_with_index(self):
        """Test creating DataFrame with custom index."""
        data = {"value": [1, 2, 3]}
        index = ["a", "b", "c"]
        df = create_dataframe(data, index=index)
        
        assert list(df.index) == index
        assert df.loc["a", "value"] == 1
        assert df.loc["c", "value"] == 3
    
    def test_create_empty_dataframe(self):
        """Test creating empty DataFrame."""
        data = {"col1": [], "col2": []}
        df = create_dataframe(data)
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 0
        assert list(df.columns) == ["col1", "col2"]


class TestCreateSampleData:
    """Test the create_sample_data function."""
    
    def test_create_sample_data_default(self):
        """Test creating sample data with default parameters."""
        df = create_sample_data()
        
        assert isinstance(df, pd.DataFrame)
        assert df.shape == (100, 5)
        assert all(col.startswith("feature_") for col in df.columns)
    
    def test_create_sample_data_custom_size(self):
        """Test creating sample data with custom dimensions."""
        df = create_sample_data(n_rows=50, n_cols=3)
        
        assert df.shape == (50, 3)
        assert list(df.columns) == ["feature_1", "feature_2", "feature_3"]
    
    def test_create_sample_data_no_missing(self):
        """Test creating sample data without missing values."""
        df = create_sample_data(n_rows=20, n_cols=2, missing_rate=0.0)
        
        assert df.shape == (20, 2)
        assert not df.isnull().any().any()
    
    def test_create_sample_data_with_missing(self):
        """Test creating sample data with missing values."""
        df = create_sample_data(n_rows=100, n_cols=2, missing_rate=0.1)
        
        assert df.shape == (100, 2)
        # Should have some missing values (approximately 10% of 200 values)
        missing_count = df.isnull().sum().sum()
        assert missing_count > 0
        assert missing_count < 200  # Less than total values
    
    def test_create_sample_data_reproducible(self):
        """Test that sample data is reproducible with same random state."""
        df1 = create_sample_data(n_rows=10, n_cols=2, random_state=42)
        df2 = create_sample_data(n_rows=10, n_cols=2, random_state=42)
        
        pd.testing.assert_frame_equal(df1, df2)