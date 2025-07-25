"""
Tests for the normalize module.
"""

import pytest
import pandas as pd
import numpy as np
from pandas_processors.normalize import MinMaxNormalizer, StandardNormalizer


class TestMinMaxNormalizer:
    """Test the MinMaxNormalizer class."""
    
    def test_minmax_normalizer_init_default(self):
        """Test MinMaxNormalizer with default range."""
        normalizer = MinMaxNormalizer()
        assert normalizer.feature_range == (0, 1)
        assert normalizer.data_min_ == {}
        assert normalizer.data_max_ == {}
    
    def test_minmax_normalizer_init_custom_range(self):
        """Test MinMaxNormalizer with custom range."""
        normalizer = MinMaxNormalizer(feature_range=(-1, 1))
        assert normalizer.feature_range == (-1, 1)
    
    def test_minmax_normalizer_fit_transform(self):
        """Test MinMaxNormalizer fit and transform."""
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["a", "b", "c", "d", "e"]  # Non-numeric
        })
        
        normalizer = MinMaxNormalizer()
        result = normalizer.fit_transform(df)
        
        # Check that A is normalized to [0, 1]
        expected_a = [0.0, 0.25, 0.5, 0.75, 1.0]
        np.testing.assert_array_almost_equal(result["A"], expected_a)
        
        # Check that B is normalized to [0, 1]
        expected_b = [0.0, 0.25, 0.5, 0.75, 1.0]
        np.testing.assert_array_almost_equal(result["B"], expected_b)
        
        # Check that non-numeric column is unchanged
        assert result["C"].equals(df["C"])
    
    def test_minmax_normalizer_custom_range(self):
        """Test MinMaxNormalizer with custom range."""
        df = pd.DataFrame({"A": [0, 5, 10]})
        
        normalizer = MinMaxNormalizer(feature_range=(-1, 1))
        result = normalizer.fit_transform(df)
        
        expected = [-1.0, 0.0, 1.0]
        np.testing.assert_array_almost_equal(result["A"], expected)
    
    def test_minmax_normalizer_constant_column(self):
        """Test MinMaxNormalizer with constant values."""
        df = pd.DataFrame({"A": [5, 5, 5, 5]})
        
        normalizer = MinMaxNormalizer()
        result = normalizer.fit_transform(df)
        
        # All values should be min value of range when data has no variance
        expected = [0.0, 0.0, 0.0, 0.0]
        np.testing.assert_array_almost_equal(result["A"], expected)
    
    def test_minmax_normalizer_specific_columns(self):
        """Test MinMaxNormalizer with specific columns."""
        df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [10, 20, 30],
            "C": [100, 200, 300]
        })
        
        normalizer = MinMaxNormalizer()
        result = normalizer.fit_transform(df, columns=["A", "C"])
        
        # A and C should be normalized
        np.testing.assert_array_almost_equal(result["A"], [0.0, 0.5, 1.0])
        np.testing.assert_array_almost_equal(result["C"], [0.0, 0.5, 1.0])
        
        # B should be unchanged
        assert result["B"].equals(df["B"])
    
    def test_transform_without_fit_raises_error(self):
        """Test that transform without fit raises ValueError."""
        df = pd.DataFrame({"A": [1, 2, 3]})
        normalizer = MinMaxNormalizer()
        
        with pytest.raises(ValueError, match="Normalizer has not been fit yet"):
            normalizer.transform(df)


class TestStandardNormalizer:
    """Test the StandardNormalizer class."""
    
    def test_standard_normalizer_init(self):
        """Test StandardNormalizer initialization."""
        normalizer = StandardNormalizer()
        assert normalizer.mean_ == {}
        assert normalizer.std_ == {}
    
    def test_standard_normalizer_fit_transform(self):
        """Test StandardNormalizer fit and transform."""
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["a", "b", "c", "d", "e"]  # Non-numeric
        })
        
        normalizer = StandardNormalizer()
        result = normalizer.fit_transform(df)
        
        # Check that A is standardized (mean≈0, std≈1)
        assert abs(result["A"].mean()) < 1e-10
        assert abs(result["A"].std() - 1.0) < 1e-10
        
        # Check that B is standardized (mean≈0, std≈1)
        assert abs(result["B"].mean()) < 1e-10
        assert abs(result["B"].std() - 1.0) < 1e-10
        
        # Check that non-numeric column is unchanged
        assert result["C"].equals(df["C"])
    
    def test_standard_normalizer_constant_column(self):
        """Test StandardNormalizer with constant values."""
        df = pd.DataFrame({"A": [5, 5, 5, 5]})
        
        normalizer = StandardNormalizer()
        result = normalizer.fit_transform(df)
        
        # All values should be 0 when data has no variance
        expected = [0.0, 0.0, 0.0, 0.0]
        np.testing.assert_array_almost_equal(result["A"], expected)
    
    def test_standard_normalizer_specific_columns(self):
        """Test StandardNormalizer with specific columns."""
        df = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": [100, 200, 300, 400, 500]
        })
        
        normalizer = StandardNormalizer()
        result = normalizer.fit_transform(df, columns=["A", "C"])
        
        # A and C should be standardized
        assert abs(result["A"].mean()) < 1e-10
        assert abs(result["A"].std() - 1.0) < 1e-10
        assert abs(result["C"].mean()) < 1e-10
        assert abs(result["C"].std() - 1.0) < 1e-10
        
        # B should be unchanged
        assert result["B"].equals(df["B"])
    
    def test_transform_without_fit_raises_error(self):
        """Test that transform without fit raises ValueError."""
        df = pd.DataFrame({"A": [1, 2, 3]})
        normalizer = StandardNormalizer()
        
        with pytest.raises(ValueError, match="Normalizer has not been fit yet"):
            normalizer.transform(df)