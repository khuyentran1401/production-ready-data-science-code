# Custom Format Logging

Customize Loguru's output format with timestamps, module info, and log levels.

## Files

- `custom_format.py` - Custom format with module, function, and line info

## Key Points

- Use `logger.remove()` and `logger.add()` to customize format
- Include timestamps, module info, and set minimum log levels

## How to Run

```bash
uv run --group chapter9 python custom_format.py
```

## Expected Output

You'll see structured log messages with custom timestamp format and detailed source information.

## Learn More

← [Back to Chapter 9](../README.md) for more logging patterns and the complete guide.