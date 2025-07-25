"""
Example showing why print-based testing is problematic.

This demonstrates the limitations of using print statements
for testing compared to structured unit tests.
"""

from sentiment_analyzer import extract_sentiment, classify_sentiment


def test_with_print_statements():
    """
    This shows the problems with print-based testing:
    1. No automated verification
    2. Manual inspection required
    3. No failure detection
    4. Cluttered output
    """
    print("Testing sentiment analysis functions...")
    
    # Test positive sentiment
    text1 = "I love this amazing day"
    result1 = extract_sentiment(text1)
    print(f"Positive test: '{text1}' -> {result1}")
    print("Expected: > 0")  # Manual verification needed!
    
    # Test negative sentiment  
    text2 = "This is terrible and awful"
    result2 = extract_sentiment(text2)
    print(f"Negative test: '{text2}' -> {result2}")
    print("Expected: < 0")  # Manual verification needed!
    
    # Test classification
    text3 = "I'm happy today"
    result3 = classify_sentiment(text3) 
    print(f"Classification test: '{text3}' -> {result3}")
    print("Expected: 'positive'")  # Manual verification needed!
    
    print("All tests completed!")  # But did they actually pass?


def test_broken_function_with_print():
    """
    This shows how print-based testing fails to catch bugs.
    The function has a bug but the test appears to "pass".
    """
    def broken_sentiment(text):
        # Bug: always returns 0 instead of actual sentiment
        return 0.0
    
    print("Testing broken function...")
    
    positive_text = "I absolutely love this!"
    result = broken_sentiment(positive_text)
    print(f"Positive text result: {result}")
    print("Expected: > 0")
    
    # The bug is not automatically detected!
    # A human has to manually verify the output
    print("Test completed!")  # False sense of success


if __name__ == "__main__":
    print("=== Print-based Testing Example ===")
    test_with_print_statements()
    print("\n=== Broken Function Example ===")
    test_broken_function_with_print()
    
    print("\n=== Problems with this approach ===")
    print("1. No automatic verification of results")
    print("2. Requires manual inspection of output") 
    print("3. Doesn't fail when functions return wrong values")
    print("4. Difficult to run automatically in CI/CD")
    print("5. Hard to identify which specific tests failed")
    print("\nCompare this with: uv run pytest test_sentiment_analyzer.py -v")