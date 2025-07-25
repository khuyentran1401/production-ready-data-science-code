"""
Unit tests for basic functions from Chapter 7.

This demonstrates basic pytest usage exactly as shown in the book.
"""

import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
from sentiment_analyzer import create_booleans, calculate_average, extract_sentiment


def test_create_booleans():
    """Test the create_booleans function - this will fail due to the bug."""
    df = pd.DataFrame(
        {"num_apples": [1, 2, 3, 0], "num_oranges": [4, 5, 0, 6]}
    )
    expected_df = pd.DataFrame(
        {"has_apples": [1, 1, 1, 0], "has_oranges": [1, 1, 0, 1]}
    )
    df["has_apples"] = create_booleans(df["num_apples"])
    df["has_oranges"] = create_booleans(df["num_oranges"])
    assert_frame_equal(
        df[["has_apples", "has_oranges"]], expected_df
    )


def test_calculate_average_positive_numbers():
    """Test average calculation with positive numbers."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3


def test_calculate_average_empty_list():
    """Test average calculation with empty list - this will fail."""
    assert calculate_average([]) == 0


def test_extract_sentiment():
    """Test basic sentiment extraction."""
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)
    assert sentiment > 0


def test_extract_sentiment_positive():
    """Test positive sentiment."""
    text = "I think today will be a great day"
    sentiment = extract_sentiment(text)
    assert sentiment > 0


def test_extract_sentiment_negative():
    """Test negative sentiment."""
    text = "I do not think this will turn out well"
    sentiment = extract_sentiment(text)
    assert sentiment < 0