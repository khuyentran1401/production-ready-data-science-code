"""
Custom formatting example from Chapter 9.

This demonstrates how to customize Loguru's output format.
"""

import sys
from loguru import logger

# Remove the default handler
logger.remove()

# Add a stream handler
logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
           "{module}:{function}:{line} - {message}",
    level="INFO",
)


def main():
    logger.debug("This debug message won't appear (level=INFO)")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()