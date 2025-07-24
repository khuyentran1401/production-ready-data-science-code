"""Tests for utility helper functions."""

import pandas as pd

from data_pipeline.utils.helpers import create_summary, format_results, validate_data


def test_format_results():
    """Test results formatting function."""
    accuracy = 0.85
    feature_importance = pd.Series([0.3, 0.7], index=["feature1", "feature2"])

    result = format_results(accuracy, feature_importance)

    assert "Accuracy: 0.850" in result
    assert "feature2: 0.700" in result
    assert "feature1: 0.300" in result


def test_create_summary():
    """Test data summary creation."""
    test_data = pd.DataFrame({
        "col1": [1, 2, None],
        "col2": ["a", "b", "c"]
    })

    summary = create_summary(test_data)

    assert summary["shape"] == (3, 2)
    assert "col1" in summary["columns"]
    assert "col2" in summary["columns"]
    assert summary["missing_values"]["col1"] == 1
    assert summary["missing_values"]["col2"] == 0


def test_validate_data_success():
    """Test successful data validation."""
    data = pd.DataFrame({
        "required1": [1, 2, 3],
        "required2": [4, 5, 6],
        "optional": [7, 8, 9]
    })

    assert validate_data(data, ["required1", "required2"]) is True


def test_validate_data_failure():
    """Test failed data validation."""
    data = pd.DataFrame({
        "col1": [1, 2, 3],
        "col2": [4, 5, 6]
    })

    # Missing required column
    assert validate_data(data, ["col1", "col2", "missing_col"]) is False
