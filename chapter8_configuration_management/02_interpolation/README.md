# Hydra Interpolation

Reference configuration values within other values to reduce duplication.

## Files

- `config/main.yaml` - Configuration using interpolation syntax `${...}`
- `interpolation_demo.py` - Script showing interpolated values

## Key Points

- Use `${key}` syntax to reference other configuration values
- Changing one value automatically updates all dependent values

## How to Run

```bash
# Run to see interpolated values
uv run --group chapter8 python interpolation_demo.py

# Override project name and see all paths update
uv run --group chapter8 python interpolation_demo.py project.name=new_project
```

## Expected Output

You'll see how changing `project.name` automatically updates all paths that reference it.

## Learn More

← [Back to Chapter 8](../README.md) for more configuration patterns and the complete guide.