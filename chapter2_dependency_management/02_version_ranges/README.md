# Version Ranges

Compare exact version pinning vs version ranges from the book.

## Files

- `requirements-exact.txt` - Exact versions like `pandas==1.5.3`, `numpy==1.24.0`
- `requirements-ranges.txt` - Version ranges like `pandas>=1.5.3,<1.6.0`, `numpy>=1.24.0,<1.25.0`
- `check_versions.py` - Shows installed package versions

## Key Points

- Exact pinning prevents bug fixes (stuck on 1.5.3, miss 1.5.4)
- Ranges allow safe updates while avoiding breaking changes

## How to Run

**With exact versions:**
```bash
python -m venv exact_env
source exact_env/bin/activate  # Windows: exact_env\Scripts\activate
pip install -r requirements-exact.txt
python check_versions.py
deactivate
```

**With version ranges:**
```bash
python -m venv ranges_env
source ranges_env/bin/activate  # Windows: ranges_env\Scripts\activate
pip install -r requirements-ranges.txt
python check_versions.py
deactivate
```

## Expected Output

**Exact**: Always installs pandas 1.5.3, matplotlib 3.6.0, scikit-learn 1.2.0
**Ranges**: Installs latest compatible version (pandas 1.5.3, matplotlib 3.6.3, scikit-learn 1.2.2)

Version ranges get you bug fixes automatically!