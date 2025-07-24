# ruff: noqa: F403, F405
import pandas as pd

# BAD: Using wildcard imports
from processors import *
from sklearn.impute import *


simple_imputer = SimpleImputer()
knn_imputer = KNNImputer()

print("Imputer objects:")
print(
	f"simple_imputer: {simple_imputer} (from {simple_imputer.__class__.__module__})"
)
print(
	f"knn_imputer: {knn_imputer} (from {knn_imputer.__class__.__module__})"
)

"""
Imputer objects:
simple_imputer: SimpleImputer() (from sklearn.impute._base)
knn_imputer: KNNImputer() (from sklearn.impute._knn)
"""
