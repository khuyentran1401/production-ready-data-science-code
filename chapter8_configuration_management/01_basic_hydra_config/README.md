# Basic Hydra Configuration

This example demonstrates the basic Hydra configuration management as shown in Chapter 8.

## Files
- `config/main.yaml`: Main configuration file with process parameters
- `process.py`: Python script using Hydra decorator

## Running the Example

```bash
# Run with default configuration
uv run --group chapter8 python process.py

# Override parameters from command line
uv run --group chapter8 python process.py process.test_size=0.3

# View help
uv run --group chapter8 python process.py --help

# Multi-run with different test sizes
uv run --group chapter8 python process.py --multirun process.test_size=0.2,0.3
```

## Key Features Demonstrated
- `@hydra.main` decorator usage
- Dot notation (`config.process.feature`) and bracket notation (`config["process"]["cols_to_drop"]`)
- Command-line parameter overrides
- Multi-run execution