# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2024-01-XX

### Added
- Initial release of pandas-processors package
- DataFrame creation utilities (`create_dataframe`, `create_sample_data`)
- Data imputation classes (`MeanMedianImputer`, `SimpleImputer`)
- Data normalization classes (`MinMaxNormalizer`, `StandardNormalizer`)
- Comprehensive test suite with pytest
- Complete documentation with examples
- MIT License
- Package configuration with uv and hatchling build system

### Features
- **Create Module**: Functions for creating DataFrames with sample data and missing values
- **Impute Module**: Classes for handling missing values with mean, median, or constant strategies
- **Normalize Module**: Classes for feature scaling with min-max and standard normalization
- **Type Hints**: Full type annotation support throughout the package
- **Error Handling**: Proper validation and error messages for edge cases

### Documentation
- README with comprehensive usage examples
- API documentation support with pdoc3
- Development guide with building and publishing instructions
- Test coverage reporting

[Unreleased]: https://github.com/example/pandas-processors/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/example/pandas-processors/releases/tag/v0.1.0