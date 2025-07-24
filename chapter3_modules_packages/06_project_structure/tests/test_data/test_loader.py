"""Tests for data loading functionality."""

import pytest
import pandas as pd
from data_pipeline.data.loader import load_data, save_data
from data_pipeline.config import RAW_DATA_DIR
import tempfile
from pathlib import Path


def test_load_data_creates_sample_when_missing():
    """Test that load_data creates sample data when file doesn't exist."""
    # Use a unique filename that doesn't exist
    test_filename = "test_nonexistent.csv"
    
    # Clean up any existing test file
    test_path = RAW_DATA_DIR / test_filename
    if test_path.exists():
        test_path.unlink()
    
    # Load data (should create sample)
    data = load_data(test_filename)
    
    # Verify sample data structure
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 5
    assert "feature1" in data.columns
    assert "feature2" in data.columns
    assert "target" in data.columns
    
    # Clean up
    if test_path.exists():
        test_path.unlink()


def test_save_data():
    """Test data saving functionality."""
    # Create test data
    test_data = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })
    
    # Use temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        filename = "test_save.csv"
        
        # Save data
        save_data(test_data, filename, temp_path)
        
        # Verify file was created and has correct content
        saved_path = temp_path / filename
        assert saved_path.exists()
        
        loaded_data = pd.read_csv(saved_path)
        pd.testing.assert_frame_equal(test_data, loaded_data)