"""
Simple functions for edge case testing from Chapter 7.

These match the examples shown in the book.
"""

import math


def calculate_average(nums: list) -> float:
    """Calculate average - has edge case with empty list."""
    return sum(nums) / len(nums)


def calculate_distance(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    """Calculate 3D distance between two points."""
    return math.sqrt(
        (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
    )