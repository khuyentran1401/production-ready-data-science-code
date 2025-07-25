"""
Parametrized tests exactly as shown in Chapter 7.

This demonstrates @pytest.mark.parametrize using the book's examples.
"""

import pytest
from text_processor import extract_sentiment, sentence_contain_word


# Example 1: Parametrize with a list of samples (from book)
testdata = [
    "I think today will be a great day",
    "I do not think this will turn out well",
]


@pytest.mark.parametrize("sample", testdata)
def test_extract_sentiment(sample):
    """Test sentiment extraction with parametrized inputs."""
    sentiment = extract_sentiment(sample)
    assert sentiment > 0


# Example 2: Parametrize with input-output pairs (from book) 
testdata_pairs = [
    ("There is a duck", True), 
    ("There is nothing here", False)
]


@pytest.mark.parametrize("sample, expected_output", testdata_pairs)
def test_sentence_contain_word(sample, expected_output):
    """Test word containment with expected outputs."""
    word = "duck"
    assert sentence_contain_word(word, sample) == expected_output