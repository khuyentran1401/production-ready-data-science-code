"""
Basic tests for test organization example.
"""

import pytest


def add_numbers(a, b):
    """Simple function to add two numbers."""
    return a + b


def multiply_numbers(a, b):
    """Simple function to multiply two numbers."""
    return a * b


def test_addition():
    """Test basic addition."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_multiplication():
    """Test basic multiplication."""
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(0, 5) == 0


def test_edge_cases():
    """Test edge cases."""
    assert add_numbers(1000000, 1) == 1000001
    assert multiply_numbers(1, 1) == 1