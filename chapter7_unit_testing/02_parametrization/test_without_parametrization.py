"""
Example showing the problems with non-parametrized tests.

This demonstrates why parametrization is useful by showing
the repetitive, hard-to-maintain alternative.
"""

from text_processor import count_words, get_text_sentiment, clean_text


# Without parametrization - lots of repetitive code
def test_word_count_hello_world():
    """Test word count for 'hello world'."""
    assert count_words("hello world") == 2


def test_word_count_single_word():
    """Test word count for single word."""
    assert count_words("one") == 1


def test_word_count_empty_string():
    """Test word count for empty string."""
    assert count_words("") == 0


def test_word_count_spaces_only():
    """Test word count for spaces only."""
    assert count_words("   ") == 0


def test_word_count_three_words():
    """Test word count for three words."""
    assert count_words("word1 word2 word3") == 3


def test_word_count_extra_spaces():
    """Test word count with extra spaces."""
    assert count_words("extra   spaces   between") == 3


# Without parametrization - sentiment tests
def test_sentiment_positive_love():
    """Test positive sentiment with 'love'."""
    assert get_text_sentiment("I love this amazing product!") == "positive"


def test_sentiment_negative_terrible():
    """Test negative sentiment with 'terrible'."""
    assert get_text_sentiment("This is terrible and awful") == "negative"


def test_sentiment_neutral_fact():
    """Test neutral sentiment with factual statement."""
    assert get_text_sentiment("The sky is blue") == "neutral"


def test_sentiment_empty_string():
    """Test sentiment for empty string."""
    assert get_text_sentiment("") == "neutral"


def test_sentiment_positive_happy():
    """Test positive sentiment with 'happy'."""
    assert get_text_sentiment("I'm so happy and excited!") == "positive"


def test_sentiment_negative_hate():
    """Test negative sentiment with 'hate'."""
    assert get_text_sentiment("I hate everything about this") == "negative"


# Without parametrization - text cleaning tests
def test_clean_text_with_exclamation():
    """Test cleaning text with exclamation mark."""
    assert clean_text("hello world!") == "hello world"


def test_clean_text_extra_spaces():
    """Test cleaning text with extra spaces."""
    assert clean_text("extra   spaces") == "extra spaces"


def test_clean_text_special_chars():
    """Test cleaning text with special characters."""
    assert clean_text("special@#$chars") == "specialchars"


def test_clean_text_empty():
    """Test cleaning empty string."""
    assert clean_text("") == ""


def test_clean_text_numbers():
    """Test cleaning text with numbers."""
    assert clean_text("123 numbers 456") == "123 numbers 456"


def test_clean_text_mixed():
    """Test cleaning mixed text."""
    assert clean_text("Mixed!@# Text$%^ Here") == "Mixed Text Here"


"""
PROBLEMS WITH THIS APPROACH:

1. CODE DUPLICATION:
   - Same test logic repeated many times
   - Similar function calls with different inputs
   - Duplicate assertion patterns

2. MAINTENANCE BURDEN:
   - Adding new test case requires new function
   - Changes to test logic need updates in multiple places
   - Harder to see patterns across tests

3. READABILITY ISSUES:
   - Hard to see all test cases at a glance
   - Individual functions don't show relationship between cases
   - More scrolling needed to understand test coverage

4. NAMING CHALLENGES:
   - Need unique function names for each case
   - Names become verbose and repetitive
   - Hard to maintain consistent naming

5. DISCOVERY PROBLEMS:
   - Difficult to quickly identify missing test cases
   - No clear overview of what scenarios are covered
   - Easy to accidentally duplicate test cases

SOLUTION: Use parametrization!
See test_text_processor.py for the improved approach.
"""