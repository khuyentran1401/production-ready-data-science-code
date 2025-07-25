# Pandas Processors

Utilities for pandas DataFrame processing, demonstrating Python packaging with uv and hatchling.

## Overview

This package provides utilities for creating, imputing, and normalizing pandas DataFrames. It serves as a complete example of Python packaging as demonstrated in Chapter 13 of "Production-Ready Data Science".

## Features

- **DataFrame Creation**: Functions for creating DataFrames with sample data
- **Data Imputation**: Classes for handling missing values (mean, median, constant)
- **Data Normalization**: Classes for scaling features (min-max, standard/z-score)

## Installation

```bash
pip install pandas-processors
```

## Quick Start

```python
import pandas_processors as pp

# Create sample data with missing values
df = pp.create_sample_data(n_rows=100, n_cols=3, missing_rate=0.1)

# Impute missing values with mean
imputer = pp.MeanMedianImputer(strategy="mean")
df_imputed = imputer.fit_transform(df)

# Normalize features to 0-1 range
normalizer = pp.MinMaxNormalizer()
df_normalized = normalizer.fit_transform(df_imputed)

print(df_normalized.head())
```

## API Reference

### Creating DataFrames

```python
from pandas_processors.create import create_dataframe, create_sample_data

# Create DataFrame from dictionary
data = {"name": ["Alice", "Bob"], "age": [25, 30]}
df = create_dataframe(data)

# Create sample data for testing
df = create_sample_data(n_rows=100, n_cols=5, missing_rate=0.1)
```

### Data Imputation

```python
from pandas_processors.impute import MeanMedianImputer, SimpleImputer

# Mean/median imputation
imputer = MeanMedianImputer(strategy="mean")
df_imputed = imputer.fit_transform(df)

# Constant value imputation
imputer = SimpleImputer(fill_value=0)
df_imputed = imputer.transform(df)
```

### Data Normalization

```python
from pandas_processors.normalize import MinMaxNormalizer, StandardNormalizer

# Min-max scaling (0-1)
normalizer = MinMaxNormalizer(feature_range=(0, 1))
df_normalized = normalizer.fit_transform(df)

# Standard scaling (z-score)
normalizer = StandardNormalizer()
df_normalized = normalizer.fit_transform(df)
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/example/pandas-processors.git
cd pandas-processors

# Install development dependencies
uv add pytest pandas numpy --dev
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=pandas_processors --cov-report=html
```

### Building the Package

```bash
# Build source and wheel distributions
uv build
```

This creates files in the `dist/` directory:
- `pandas_processors-0.1.0.tar.gz` (source distribution)
- `pandas_processors-0.1.0-py3-none-any.whl` (wheel distribution)

### Publishing to PyPI

```bash
# Publish to PyPI
uv publish
```

### Generating Documentation

```bash
# Install documentation dependencies
uv add pdoc3 --dev

# Generate HTML documentation
pdoc --html pandas_processors -o docs
```

### Version Management

Follow semantic versioning (MAJOR.MINOR.PATCH):

1. Update version in `pyproject.toml`:
   ```toml
   [tool.uv]
   version = "0.1.1"
   ```

2. Create Git tag:
   ```bash
   git tag -a v0.1.1 -m "Version 0.1.1"
   git push origin v0.1.1
   ```

3. Build and publish:
   ```bash
   uv build
   uv publish
   ```

## Package Structure

```
pandas_processors/
├── pandas_processors/           # Source package
│   ├── __init__.py             # Package initialization
│   ├── create.py              # DataFrame creation utilities
│   ├── impute.py              # Missing value imputation
│   └── normalize.py           # Feature normalization
├── tests/                     # Test suite
│   ├── test_create.py
│   ├── test_impute.py
│   └── test_normalize.py
├── docs/                      # Generated documentation
├── pyproject.toml             # Package configuration
├── README.md                  # This file
├── LICENSE                    # MIT License
└── CHANGELOG.md               # Version history
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.