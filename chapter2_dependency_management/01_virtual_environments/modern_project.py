import pandas as pd

print(f"pandas version: {pd.__version__}")

# Create sample data
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
additional = pd.DataFrame({'A': [5], 'B': [6]})

# Modern approach that works in pandas 2.0+
result = pd.concat([df, additional], ignore_index=True)
print("Using pd.concat() (modern pandas 2.0+ approach):")
print(result)