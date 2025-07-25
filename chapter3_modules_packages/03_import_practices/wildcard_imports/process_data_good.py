# GOOD: Using explicit imports
from processors import SimpleImputer  # Our custom SimpleImputer
from sklearn.impute import KNNImputer  # sklearn's KNNImputer

# CLEAR: We know exactly which SimpleImputer we're using
simple_imputer = SimpleImputer()  # This is clearly from processors
knn_imputer = KNNImputer()        # This is clearly from sklearn.impute

print("Imputer objects:")
print(f"simple_imputer: {simple_imputer} (from {simple_imputer.__class__.__module__})")
print(f"knn_imputer: {knn_imputer} (from {knn_imputer.__class__.__module__})")

"""
Expected output:
simple_imputer: <processors.SimpleImputer object> (from processors)
knn_imputer: KNNImputer() (from sklearn.impute._knn)
"""
