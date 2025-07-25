"""
File logging example from Chapter 9.

This demonstrates logging to both terminal and file simultaneously.
"""

from loguru import logger

# Add file handler (terminal logging is default)
logger.add(
    "info.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | "
           "{module}:{function}:{line} - {message}",
    level="INFO",
)


def main():
    logger.debug("This debug message won't be saved to file (level=INFO)")
    logger.info("This message appears in both terminal and file")
    logger.warning("This warning appears in both terminal and file")
    logger.error("This error appears in both terminal and file")


if __name__ == "__main__":
    main()