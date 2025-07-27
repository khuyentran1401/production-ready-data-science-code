# Hydra Config Groups

Organize related configurations into swappable groups for easy strategy switching.

## Files

- `config/main.yaml` - Main config file with defaults
- `config/process/drop_missing.yaml` - Strategy that drops missing values
- `config/process/impute.yaml` - Strategy that imputes missing values
- `config_groups_demo.py` - Script using config groups

## Key Points

- Organize configs in subdirectories (`process/`)
- Switch strategies easily via command line

## How to Run

```bash
# Run with default processing strategy (drop_missing)
uv run --group chapter8 python config_groups_demo.py

# Switch to impute strategy
uv run --group chapter8 python config_groups_demo.py process=impute

# Compare both strategies with multirun
uv run --group chapter8 python config_groups_demo.py --multirun process=drop_missing,impute
```

## Expected Output

The script will show how different processing strategies handle missing data.

## Try This

1. **Add a new strategy**: Create `config/process/fill_zero.yaml` and test it
2. **Mix groups**: Try combining different configuration groups in multirun mode

## Learn More

← [Back to Chapter 8](../README.md) for more configuration patterns and the complete guide.