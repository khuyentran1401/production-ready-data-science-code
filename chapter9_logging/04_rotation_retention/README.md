# Log Rotation and Retention

Automatically rotate log files by size or time and manage retention policies.

## Files

- `rotation_example.py` - Different rotation triggers and retention policies
- `logs/` - Directory where rotated logs are stored

## Key Points

- Rotate logs by size (`rotation="500 MB"`) or time (`rotation="12:00"`)
- Set retention policies (`retention="10 days"`) and compression

## How to Run

```bash
uv run --group chapter9 python rotation_example.py
```

## Expected Output

Check the `logs/` directory to see files automatically rotated, compressed, and cleaned up.

## Try This

1. **Test size rotation**: Generate large log entries to trigger size-based rotation
2. **Change retention**: Modify retention period and observe cleanup behavior

## Learn More

← [Back to Chapter 9](../README.md)

---

← [Previous: 03_file_logging](../03_file_logging/README.md) | **Next:** [05_filtering →](../05_filtering/README.md)

*Example 4 of 7*