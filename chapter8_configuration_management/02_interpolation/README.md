# Hydra Interpolation

**Problem**: Data science configurations often have redundant or dependent values (like file paths based on experiment names), leading to inconsistencies and manual updates across multiple parameters.

Reference configuration values within other values to reduce duplication.

**Why This Matters**: Configuration interpolation reduces redundancy, prevents inconsistencies, and automatically generates dependent values, making data science experiment configurations more maintainable.

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

← [Back to Chapter 8](../README.md)

---

← [Previous: 01_basic_hydra_config](../01_basic_hydra_config/README.md) | **Next:** [03_config_groups →](../03_config_groups/README.md)

*Example 2 of 4*