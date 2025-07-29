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

← [Back to Chapter 9](../README.md)

---

← [Previous: 04_rotation_retention](../04_rotation_retention/README.md) | **Next:** [06_exception_handling →](../06_exception_handling/README.md)

*Example 5 of 7*