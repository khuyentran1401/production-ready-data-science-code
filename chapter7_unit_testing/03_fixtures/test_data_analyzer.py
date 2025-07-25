"""
Tests demonstrating fixtures exactly as shown in Chapter 7.

This uses the simple fixture example from the book.
"""

import pytest
from simple_functions import extract_sentiment, sentence_contain_word


@pytest.fixture
def example_data():
    """Fixture providing test data as shown in the book."""
    return 'Today I found a duck and I am happy'


def test_extract_sentiment(example_data):
    """Test sentiment extraction using fixture."""
    sentiment = extract_sentiment(example_data)
    assert sentiment > 0


def test_sentence_contain_word(example_data):
    """Test word containment using fixture."""
    word = 'duck'
    assert sentence_contain_word(word, example_data) == True