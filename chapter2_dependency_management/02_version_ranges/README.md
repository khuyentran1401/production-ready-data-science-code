# Version Ranges

## Problem

Pinning exact versions like `pandas==1.5.3` prevents you from receiving bug fixes in `1.5.4`. However, allowing unrestricted updates risks breaking changes when major versions jump from `1.5.3` to `2.0.0`. Version ranges solve this by allowing safe updates while blocking potentially breaking changes.

## Files

- `requirements-exact.txt` - Exact versions like `pandas==1.5.3`, `numpy==1.24.0`
- `requirements-ranges.txt` - Version ranges like `pandas>=1.5.3,<1.6.0`, `numpy>=1.24.0,<1.25.0`
- `check_versions.py` - Shows installed package versions

## Key Points

- Exact pinning prevents bug fixes (stuck on 1.5.3, miss 1.5.4 security patches)
- Ranges like `>=1.5.3,<1.6.0` automatically get patch/minor updates
- Major version changes (1.x to 2.x) are blocked to prevent breaking changes

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

## Why This Matters

Automatic security patches and bug fixes reduce maintenance overhead while preventing surprise breaking changes in production.

← [Back to Chapter 2](../README.md)

---

← [Previous: 01_virtual_environments](../01_virtual_environments/README.md) | **Next:** [03_dev_prod_separation →](../03_dev_prod_separation/README.md)

*Example 2 of 4*