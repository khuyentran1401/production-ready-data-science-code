"""
Log rotation and retention examples from Chapter 9.

This demonstrates various rotation and retention strategies.
"""

from loguru import logger
import time

# Basic rotation and retention
logger.add(
    "debug.log", level="INFO",
    rotation="1 week", retention="4 weeks",
)

# Different rotation strategies
logger.add("logs/file_1.log", rotation="500 MB")  # Rotate if file exceeds 500 MB
logger.add("logs/file_2.log", rotation="12:00")   # Create new log file daily at noon
logger.add("logs/file_3.log", rotation="1 week")  # Rotate weekly
logger.add("logs/file_X.log", retention="10 days")  # Keep logs for 10 days
logger.add("logs/file_Y.log", compression="zip")   # Compress old logs


def main():
    for i in range(10):
        logger.info(f"Log message {i}")
        logger.warning(f"Warning message {i}")
        logger.error(f"Error message {i}")
        time.sleep(0.1)  # Small delay to see timestamp differences


if __name__ == "__main__":
    main()