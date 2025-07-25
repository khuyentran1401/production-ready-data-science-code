# Log Rotation and Retention

This example demonstrates various log rotation and retention strategies.

## Files
- `rotation_example.py`: Different rotation triggers and retention policies
- `logs/`: Directory where rotated logs are stored

## Running the Example

```bash
uv run --group chapter9 python rotation_example.py
```

Check the generated log files to see the rotation and retention in action.

## Key Features Demonstrated
- Basic rotation and retention (`rotation="1 week", retention="4 weeks"`)
- Size-based rotation (`rotation="500 MB"`)
- Time-based rotation (`rotation="12:00"`, `rotation="1 week"`)
- Retention policies (`retention="10 days"`)
- Log compression (`compression="zip"`)

## Rotation Strategies
1. **Size-based**: `rotation="500 MB"` - rotate when file exceeds size
2. **Time-based**: `rotation="12:00"` - rotate daily at noon
3. **Periodic**: `rotation="1 week"` - rotate weekly
4. **Retention**: `retention="10 days"` - keep logs for specified time
5. **Compression**: `compression="zip"` - compress old logs