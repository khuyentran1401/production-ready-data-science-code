"""
Log filtering example from Chapter 9.

This demonstrates filtering log messages using lambda functions.
"""

from loguru import logger

logger.remove()
logger.add(
    "hello.log",
    filter=lambda record: "Hello" in record["message"],
)


def main():
    logger.info("Hello World")  # This will be logged to file
    logger.info("Bye World")    # This will NOT be logged to file
    logger.info("Hello again")  # This will be logged to file
    logger.warning("Hello warning")  # This will be logged to file
    logger.error("Goodbye error")    # This will NOT be logged to file


if __name__ == "__main__":
    main()