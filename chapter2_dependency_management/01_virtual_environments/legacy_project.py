import pandas as pd

print(f"pandas version: {pd.__version__}")

# Create sample data
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
additional = pd.DataFrame({'A': [5], 'B': [6]})

# This works in pandas 1.x but shows deprecation warning in 1.5+
result = df.append(additional, ignore_index=True)
print("Using df.append() (works in pandas 1.x):")
print(result)