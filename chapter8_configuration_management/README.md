# Chapter 8: Configuration Management Examples

This directory contains examples for configuration management using Hydra as demonstrated in Chapter 8 of the book.

## Examples Overview

### 1. Basic Hydra Configuration (`01_basic_hydra_config/`)
- Introduction to Hydra's `@hydra.main` decorator
- Basic configuration file structure
- Command-line parameter overrides
- Multi-run execution

### 2. Interpolation (`02_interpolation/`)
- Using `${...}` syntax to reference other config values
- Reducing configuration duplication
- Dynamic path generation

### 3. Config Groups (`03_config_groups/`)
- Organizing related configurations into groups
- Using `defaults` section
- Switching between configuration variants

## Prerequisites

Install dependencies using:
```bash
uv sync --group chapter8
```

## Key Concepts Covered

1. **Configuration Management Benefits**:
   - Separate configuration from code
   - Enable flexible experimentation
   - Keep code clean and focused

2. **Hydra Features**:
   - Intuitive parameter access via dot notation
   - Command-line configuration overrides
   - Multi-run execution for testing multiple configurations
   - Configuration interpolation to reduce duplication
   - Logical grouping of related configurations

3. **Best Practices**:
   - Use hierarchical structure in configuration files
   - Never include sensitive data in configuration files
   - Organize configurations into logical groups

## Running All Examples

Each subdirectory contains its own README with specific instructions. Generally:

```bash
# Navigate to any example directory
cd 01_basic_hydra_config/

# Run with default config
uv run --group chapter8 python <script_name>.py

# Override parameters
uv run --group chapter8 python <script_name>.py param.key=value

# View help
uv run --group chapter8 python <script_name>.py --help
```