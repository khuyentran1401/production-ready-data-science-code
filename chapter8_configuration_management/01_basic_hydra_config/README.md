# Basic Hydra Configuration

**Problem**: Data science experiments often hardcode parameters in scripts, making it difficult to track different parameter combinations, reproduce results, or run experiments with different settings.

Manage application configuration with YAML files and command-line overrides.

**Why This Matters**: Centralized configuration management enables reproducible experiments, easy parameter sweeps, and the ability to switch between development and production settings without code changes.

## Files

- `config/main.yaml` - Configuration file with process parameters
- `process.py` - Python script using Hydra decorator

## Key Points

- `@hydra.main` decorator automatically loads config files
- Override any parameter from command line with dot notation

## How to Run

```bash
# Run with default configuration
uv run --group chapter8 python process.py

# Override parameters from command line
uv run --group chapter8 python process.py process.test_size=0.3

# Multi-run with different test sizes
uv run --group chapter8 python process.py --multirun process.test_size=0.2,0.3
```

## Expected Output

The script will load configuration from YAML and process data with the specified parameters.

## Learn More

← [Back to Chapter 8](../README.md)

---

**Next:** [02_interpolation →](../02_interpolation/README.md)

*Example 1 of 4*