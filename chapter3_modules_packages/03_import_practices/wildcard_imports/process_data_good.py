import pandas as pd

# GOOD: Using explicit imports
from processors import SimpleImputer  # Our custom SimpleImputer
from sklearn.impute import KNNImputer  # sklearn's KNNImputer

# Create sample data with missing values
data = pd.DataFrame({
    "feature1": [1, 2, None, 4, 5],
    "feature2": [None, 2, 3, 4, 5],
    "feature3": [1, 2, 3, None, 5]
})

print("Original data:")
print(data)
print()

# CLEAR: We know exactly which SimpleImputer we're using
simple_imputer = SimpleImputer()  # This is clearly from processors
knn_imputer = KNNImputer()        # This is clearly from sklearn.impute

print("Imputer objects:")
print(f"simple_imputer: {simple_imputer}")
print(f"knn_imputer: {knn_imputer}")
print()

# Use our custom SimpleImputer
imputed_data = simple_imputer.fit_transform(data)
print("Data imputed with our custom processors.SimpleImputer:")
print(imputed_data)
print()

# Now use sklearn's KNNImputer for comparison
sklearn_data = knn_imputer.fit_transform(data)
print("Data imputed with sklearn.impute.KNNImputer:")
print(pd.DataFrame(sklearn_data, columns=data.columns))
print()

print("✅ BENEFITS OF EXPLICIT IMPORTS:")
print("- It's clear which SimpleImputer we're using (our custom one)")
print("- No naming conflicts or confusion")
print("- Easy to debug and maintain")
print("- Code is self-documenting")
print("- IDE can provide better autocomplete and error checking")
