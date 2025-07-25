"""
Simple functions for parametrization examples.

These match the examples shown in Chapter 7 of the book.
"""

from textblob import TextBlob


def extract_sentiment(text: str):
    """Extract sentiment using textblob."""
    text = TextBlob(text)
    return text.sentiment.polarity


def sentence_contain_word(word: str, sentence: str):
    """Check if sentence contains a specific word."""
    return word in sentence