# Hydra Interpolation

This example demonstrates Hydra's interpolation feature to reduce configuration duplication.

## Files
- `config/main.yaml`: Configuration file using interpolation syntax `${...}`
- `interpolation_demo.py`: Python script showing interpolated values

## Running the Example

```bash
# Run to see interpolated values
uv run --group chapter8 python interpolation_demo.py

# Override project name and see all paths update
uv run --group chapter8 python interpolation_demo.py project.name=new_project

# Override version
uv run --group chapter8 python interpolation_demo.py project.version=v2
```

## Key Features Demonstrated
- Interpolation syntax `${project.name}` and `${project.version}`
- Referencing other config values `${paths.base}`
- How changing one value automatically updates all dependent values