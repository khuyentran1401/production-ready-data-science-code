# Custom Format Logging

This example demonstrates how to customize Loguru's output format.

## Files
- `custom_format.py`: Custom logging format with module, function, and line info

## Running the Example

```bash
uv run --group chapter9 python custom_format.py
```

## Key Features Demonstrated
- `logger.remove()` to clear default handler
- `logger.add()` with custom format
- Time formatting tokens (`{time:YYYY-MM-DD HH:mm:ss}`)
- Module, function, and line information (`{module}:{function}:{line}`)
- Setting minimum log level (`level="INFO"`)