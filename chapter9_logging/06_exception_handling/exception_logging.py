"""
Exception handling and tracing examples from Chapter 9.

This demonstrates Loguru's improved exception logging capabilities.
"""

from loguru import logger


def division(a, b):
    return a / b


def nested(c):
    try:
        division(1, c)
    except ZeroDivisionError:
        logger.exception("ZeroDivisionError")


@logger.catch
def divide_with_decorator(a, b):
    return a / b


@logger.catch
def main():
    print("1. Exception with detailed traceback:")
    nested(0)
    
    print("\n2. Exception caught by decorator:")
    divide_with_decorator(1, 0)


if __name__ == "__main__":
    main()