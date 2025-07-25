# Log Filtering

This example demonstrates filtering log messages using lambda functions.

## Files
- `filtering_example.py`: Filters messages containing "Hello"
- `hello.log`: Generated file containing only filtered messages

## Running the Example

```bash
uv run --group chapter9 python filtering_example.py
```

Check the generated `hello.log` file - it will only contain messages with "Hello" in them.

## Key Features Demonstrated
- Lambda function filters (`filter=lambda record: "Hello" in record["message"]`)
- Selective logging to file based on message content
- Simple filtering without complex filter classes