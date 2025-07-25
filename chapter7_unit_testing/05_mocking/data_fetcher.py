"""
Simple function for mocking demonstration from Chapter 7.

This matches the example shown in the book.
"""

import pandas as pd


def get_active_users():
    """Get active users from database - exactly as shown in the book."""
    return pd.read_sql("SELECT user_id FROM users WHERE active = 1", "connection")