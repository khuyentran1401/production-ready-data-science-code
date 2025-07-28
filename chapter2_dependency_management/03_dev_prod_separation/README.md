# Dev/Prod Separation

Separate development and production dependencies as shown in the book.

## Files

- `requirements.txt` - Production dependencies + numpy compatibility constraint
- `requirements-dev.txt` - Includes production + development tools
- `analyze.py` - Simple data analysis script (needs only production deps)

## Key Points

- Production deployments don't need pytest, black, etc.
- Development needs additional tools for testing and code quality
- Use `-r requirements.txt` to include production deps in dev file

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