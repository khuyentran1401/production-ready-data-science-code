"""
Advanced tests for test organization example.
"""

import pytest


def divide_numbers(a, b):
    """Simple function to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_percentage(part, total):
    """Calculate percentage of part relative to total."""
    if total == 0:
        return 0
    return (part / total) * 100


def test_division():
    """Test basic division."""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(7, 2) == 3.5
    assert divide_numbers(-10, 2) == -5


def test_division_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_numbers(10, 0)


def test_percentage_calculation():
    """Test percentage calculations."""
    assert calculate_percentage(25, 100) == 25.0
    assert calculate_percentage(1, 4) == 25.0
    assert calculate_percentage(0, 100) == 0.0


def test_percentage_with_zero_total():
    """Test percentage with zero total."""
    assert calculate_percentage(10, 0) == 0