# ruff: noqa: F403, F405
import pandas as pd

# BAD: Using wildcard imports
from processors import *
from sklearn.impute import *

# Create sample data with missing values
data = pd.DataFrame({
    "feature1": [1, 2, None, 4, 5],
    "feature2": [None, 2, 3, 4, 5],
    "feature3": [1, 2, 3, None, 5]
})

print("Original data:")
print(data)
print()

# PROBLEM: Which SimpleImputer are we using?
# We intended to use our custom processors.SimpleImputer,
# but we're actually using sklearn.impute.SimpleImputer!
simple_imputer = SimpleImputer()  # This is from sklearn.impute!
knn_imputer = KNNImputer()        # This is from sklearn.impute

print("Imputer objects:")
print(f"simple_imputer: {simple_imputer}")
print(f"knn_imputer: {knn_imputer}")
print()

# The SimpleImputer from sklearn works differently than our custom one
imputed_data = simple_imputer.fit_transform(data)
print("Data imputed with sklearn.impute.SimpleImputer:")
print(pd.DataFrame(imputed_data, columns=data.columns))
print()

print("⚠️  PROBLEM DEMONSTRATED:")
print("- We intended to use our custom processors.SimpleImputer")
print("- But wildcard imports caused us to use sklearn.impute.SimpleImputer instead")
print("- This happens because Python uses the LAST imported definition when names conflict")
print("- It's unclear which module each function/class comes from")
print("- This makes debugging much harder!")
