# Virtual Environments

Experience the pandas 1.5.x vs 2.x dependency conflict from the book.

## Files

- `legacy_project.py` - Uses deprecated `df.append()` method
- `modern_project.py` - Uses modern `pd.concat()` method  
- `requirements-legacy.txt` - pandas 1.5.x + numpy compatibility constraint
- `requirements-modern.txt` - pandas 2.x

## Key Points

- Different projects need different pandas versions
- Virtual environments prevent conflicts

## How to Run

**Legacy environment:**
```bash
python -m venv legacy_env
source legacy_env/bin/activate  # Windows: legacy_env\Scripts\activate
pip install -r requirements-legacy.txt
python legacy_project.py
deactivate
```

**Modern environment:**
```bash
python -m venv modern_env
source modern_env/bin/activate  # Windows: modern_env\Scripts\activate  
pip install -r requirements-modern.txt
python modern_project.py
deactivate
```

## Expected Output

**Legacy**: Shows `pandas 1.5.3`, `df.append()` works with FutureWarning
**Modern**: Shows `pandas 2.3.1`, `pd.concat()` works cleanly

**Without virtual environments:**
```bash
pip install -r requirements-legacy.txt  # Installs pandas 1.5.x
pip install -r requirements-modern.txt  # Overwrites with pandas 2.x
python legacy_project.py  # df.append() now removed, script fails
```
