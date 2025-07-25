"""
Mocking tests exactly as shown in Chapter 7.

This demonstrates the simple mocking example from the book.
"""

import pytest
import pandas as pd
from unittest.mock import patch
from data_fetcher import get_active_users


@patch("pandas.read_sql")
def test_get_active_users(mock_read_sql):
    """Test get_active_users with mocking - exactly as shown in the book."""
    # Step 1: Set up the mock response
    mock_df = pd.DataFrame({"user_id": [1, 2, 3]})
    # Tell the mock what to return when called
    mock_read_sql.return_value = mock_df
    
    # Step 2: Call the function under test
    result = get_active_users()
    
    # Step 3: Assert the results
    assert len(result) == 3
    assert list(result.columns) == ["user_id"]
    
    # Step 4: Verify the mock was called correctly
    mock_read_sql.assert_called_once()


@patch("pandas.read_sql")
def test_get_active_users_error(mock_read_sql):
    """Test error handling with side_effect - as shown in the book."""
    # Make the mock raise an error
    mock_read_sql.side_effect = ConnectionError("DB Error")
    
    # Test error handling
    with pytest.raises(ConnectionError, match="DB Error"):
        get_active_users()