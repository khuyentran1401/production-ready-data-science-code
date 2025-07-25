"""
Edge case tests exactly as shown in Chapter 7.

This demonstrates testing boundary conditions using book examples.
"""

import pytest
import math
from calculator import calculate_average, calculate_distance


def test_calculate_average_empty_list():
    """Test that empty list raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        calculate_average([])


def test_calculate_average_normal():
    """Test normal average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10]) == 10.0


def test_calculate_distance_normal():
    """Test normal distance calculation."""
    # Distance between (0,0,0) and (3,4,0) should be 5
    distance = calculate_distance(0, 0, 0, 3, 4, 0)
    assert distance == 5.0
    
    # Distance between same point should be 0
    distance = calculate_distance(1, 2, 3, 1, 2, 3)
    assert distance == 0.0


def test_calculate_distance_negative_coordinates():
    """Test distance calculation with negative coordinates."""
    distance = calculate_distance(-1, -1, -1, 1, 1, 1)
    expected = math.sqrt(12)  # sqrt(2^2 + 2^2 + 2^2)
    assert distance == pytest.approx(expected)