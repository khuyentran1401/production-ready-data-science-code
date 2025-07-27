# Production-Ready Data Science Code Examples

This repository contains code examples and implementations from the book **"Production-Ready Data Science"** by Khuyen Tran.

🔗 **Book Link**: https://codecut.ai/production-ready-data-science/

## About the Book

"Production-Ready Data Science" bridges the gap between data science prototypes and production-ready systems. It covers essential practices, tools, and methodologies for building robust, scalable, and maintainable data science solutions.

## Environment Setup

### Prerequisites
- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager

### Installation

1. **Install uv** (if not already installed):
   ```bash
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/khuyentran1401/production-ready-data-science-code.git
   cd production-ready-data-science-code
   ```

3. **Install all dependencies**:
   ```bash
   # Install all dependencies for all chapters
   uv sync --all-groups
   
   # Or install only specific chapter dependencies
   uv sync --group chapter7  # For unit testing examples
   uv sync --group chapter9  # For logging examples
   ```

### Available Dependency Groups
- `dev` - Development tools (pre-commit)
- `chapter7` - Unit testing (pytest, pytest-mock, textblob)
- `chapter8` - Configuration management (hydra-core, pyyaml)
- `chapter9` - Logging (loguru)
- `chapter10` - Data validation (pandera)
- `chapter12` - CI/CD tools (pdoc3)
- `chapter13` - Packaging tools (hatchling, build)
- `chapter14` - Notebooks (jupyter, marimo, ipytest)

### Quick Start

```bash
# Run examples from a specific chapter
cd chapter7_unit_testing/01_basic_testing
uv run pytest -v

# Run Jupyter notebooks
uv run jupyter notebook chapter4_variables/chapter4_variables.ipynb

# Run logging examples
cd chapter9_logging/01_basic_logging
uv run python basic_loguru.py
```

## Repository Structure

This repository provides practical code examples that accompany the concepts discussed in the book, organized by chapter:

### 📁 **chapter3_modules_packages/**
**Module and Package Organization**
- Project structure best practices
- Import strategies and package design patterns
- Creating reusable Python modules

### 📁 **chapter4_variables/**
**Variable Management and Best Practices** 
- Variable naming conventions and type hints
- Data validation with Pydantic models
- Memory-efficient variable handling
- **Format**: Jupyter notebook with interactive examples

### 📁 **chapter5_functions/**
**Function Design Patterns**
- Writing clean, testable functions
- Error handling and input validation
- Function composition and decorators
- **Format**: Jupyter notebook with practical exercises

### 📁 **chapter6_classes/**
**Object-Oriented Programming with Pydantic**
- Class design principles for data science
- Pydantic models for data validation
- Inheritance and composition patterns
- **Format**: Jupyter notebook with class examples

### 📁 **chapter7_unit_testing/**
**Comprehensive Testing with pytest**
- Basic test structure and assertions
- Parametrization for multiple test scenarios
- Fixtures for shared test data and setup
- Mocking external dependencies (databases, APIs)
- Edge case testing and error handling
- **Dependencies**: `uv sync --group chapter7`

### 📁 **chapter8_configuration_management/**
**Configuration Management with Hydra**
- YAML-based configuration files
- Configuration interpolation and composition
- Config groups for different environments
- **Dependencies**: `uv sync --group chapter8`

### 📁 **chapter9_logging/**
**Advanced Logging with Loguru**
- Structured logging with custom formatters
- File rotation and retention policies
- Log filtering and exception handling
- Colorized output for better debugging
- **Dependencies**: `uv sync --group chapter9`

### 📁 **chapter10_data_validation/**
**Data Validation Techniques**
- Schema validation with Pandera
- Data quality checks and constraints
- Error reporting and data profiling
- **Format**: Jupyter notebook
- **Dependencies**: `uv sync --group chapter10`

### 📁 **chapter12_continuous_integration/**
**CI/CD Workflows and Automation**
- GitHub Actions for automated testing
- Documentation generation with pdoc3
- Job dependencies and workflow orchestration
- **Dependencies**: `uv sync --group chapter12`

### 📁 **chapter13_package_your_project/**
**Python Packaging with Modern Tools**
- Complete packaging example with hatchling
- PyPI publishing workflow
- Semantic versioning and changelog management
- Documentation generation and testing
- **Dependencies**: `uv sync --group chapter13`

### 📁 **chapter14_notebooks_in_production/**
**Production-Ready Notebooks**
- Marimo for reactive notebook development
- Dependency tracking and reproducibility
- Testing notebook code with ipytest
- Converting notebooks to production scripts
- **Dependencies**: `uv sync --group chapter14`

## Getting Started

1. **Choose a chapter** based on the concept you want to learn
2. **Install dependencies** for that chapter: `uv sync --group chapterX`
3. **Navigate to the chapter directory** and follow the chapter-specific README
4. **Run the examples** using the provided commands

Each chapter directory contains its own README with detailed instructions and explanations for the specific concepts covered.

---

**Author**: Khuyen Tran  
**Website**: https://codecut.ai/