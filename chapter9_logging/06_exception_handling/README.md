# Exception Handling and Tracing

This example demonstrates Loguru's improved exception logging capabilities.

## Files
- `exception_logging.py`: Exception handling with detailed tracebacks

## Running the Example

```bash
uv run --group chapter9 python exception_logging.py
```

## Key Features Demonstrated
- `logger.exception()` for detailed exception logging
- `@logger.catch` decorator for automatic exception catching
- Full stack trace with local variable states
- Enhanced debugging information compared to standard logging