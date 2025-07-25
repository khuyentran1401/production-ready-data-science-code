"""
Simple functions from Chapter 7 examples.

These match exactly the functions shown in the book to demonstrate
basic unit testing concepts.
"""

import pandas as pd
from textblob import TextBlob


def create_booleans(feature):
    """
    Convert features to boolean indicators.
    This function contains a bug as shown in the book.
    """
    return (feature == 0) * 1


def calculate_average(nums: list) -> float:
    """
    Calculate average of a list of numbers.
    This has an edge case with empty lists.
    """
    return sum(nums) / len(nums)


def extract_sentiment(text: str):
    """
    Extract sentiment using textblob.
    Polarity is within range [-1, 1]
    """
    text = TextBlob(text)
    return text.sentiment.polarity