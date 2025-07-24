# Import Grouping: Organizing Imports Properly

This example demonstrates how to **organize imports** following PEP 8 guidelines and Python best practices. Proper import organization makes code more readable and maintainable.

## Import Organization Rules

Imports should be grouped in this order, with **blank lines** between groups:

1. **Standard library imports** - Built-in Python modules
2. **Third-party imports** - External packages (installed via pip)
3. **Local application imports** - Your own modules and packages

Within each group, imports should be **sorted alphabetically**.

## Files in This Example

### `example.py`
Demonstrates proper import organization:

```python
# Standard library imports
import datetime
import json
import os
import sys

# Third-party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
# ... more sklearn imports

# Local application imports
from utils import helpers, format_results
```

### `utils.py`
A simple local module to demonstrate local imports.

## How to Run

```bash
uv run example.py
```