# Hydra Config Groups

This example demonstrates organizing related configurations into logical groups.

## Files
- `config/main.yaml`: Main config file with defaults
- `config/process/drop_missing.yaml`: Processing strategy that drops missing values
- `config/process/impute.yaml`: Processing strategy that imputes missing values
- `config_groups_demo.py`: Python script that uses config groups

## Running the Example

```bash
# Run with default processing strategy (drop_missing)
uv run --group chapter8 python config_groups_demo.py

# Switch to impute strategy
uv run --group chapter8 python config_groups_demo.py process=impute

# Compare both strategies with multirun
uv run --group chapter8 python config_groups_demo.py --multirun process=drop_missing,impute
```

## Key Features Demonstrated
- `defaults` section in main config
- Config groups organized in subdirectories (`process/`)
- Easy switching between strategies via command line
- Mix and match different configuration groups