"""
Colorized logging example from Chapter 9.

This demonstrates custom color formatting in Loguru.
"""

from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | <cyan>{message}</cyan>",
)


def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()