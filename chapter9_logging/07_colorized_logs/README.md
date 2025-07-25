# Colorized Logging

This example demonstrates custom color formatting in Loguru.

## Files
- `colorized_logging.py`: Custom color scheme for different log components

## Running the Example

```bash
uv run --group chapter9 python colorized_logging.py
```

## Key Features Demonstrated
- `colorize=True` to enable color formatting
- Custom color tags (`<green>`, `<level>`, `<cyan>`)
- `{level.color}` token for automatic level-based coloring
- Enhanced readability with color-coded timestamps and messages