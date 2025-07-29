# Dev/Prod Separation

## Problem

Mixing development tools (pytest, black, debugging utilities) with production dependencies creates bloated deployments. Production servers don't need testing frameworks or code formatters, but they waste bandwidth, storage, and introduce potential security vulnerabilities when included.

## Files

- `requirements.txt` - Production dependencies + numpy compatibility constraint
- `requirements-dev.txt` - Includes production + development tools
- `analyze.py` - Simple data analysis script (needs only production deps)

## Key Points

- Production deployments don't need pytest, black, or debugging tools
- Development environments need additional tools for testing and code quality
- Use `-r requirements.txt` to include production deps in dev file, avoiding duplication

## How to Run

**Production environment:**
```bash
python -m venv prod_env
source prod_env/bin/activate  # Windows: prod_env\Scripts\activate
pip install -r requirements.txt
python analyze.py
pip list  # See only essential packages
deactivate
```

**Development environment:**
```bash
python -m venv dev_env
source dev_env/bin/activate  # Windows: dev_env\Scripts\activate
pip install -r requirements-dev.txt
python analyze.py
pip list  # See production + dev tools
deactivate
```

## Expected Output

**Production**: Installs 4 packages + dependencies, runs analysis
**Development**: Installs 6 packages + dependencies, can also run tests

Development environment is larger but has testing tools!

## Why This Matters

Smaller production deployments reduce attack surface, deployment time, and infrastructure costs while keeping development workflows productive.

← [Back to Chapter 2](../README.md)

---

← [Previous: 02_version_ranges](../02_version_ranges/README.md) | **Next:** [04_uv_basics →](../04_uv_basics/README.md)

*Example 3 of 4*