# Log Filtering

Filter log messages using lambda functions for selective logging.

## Files

- `filtering_example.py` - Filters messages containing "Hello"
- `hello.log` - Generated file with only filtered messages

## Key Points

- Use lambda functions to filter messages by content
- Apply different filters to different output destinations

## How to Run

```bash
uv run --group chapter9 python filtering_example.py
```

## Expected Output

Only messages containing "Hello" will be saved to `hello.log`, while all messages appear in terminal.

## Learn More

← [Back to Chapter 9](../README.md) for more logging patterns and the complete guide.