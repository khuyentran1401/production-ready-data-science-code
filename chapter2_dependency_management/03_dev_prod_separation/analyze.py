import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Create sample data
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
df = pd.DataFrame(X, columns=['feature1', 'feature2'])
df['target'] = y

print("Sample data analysis:")
print(f"Dataset shape: {df.shape}")
print(f"Target distribution:\n{df['target'].value_counts()}")

# Create simple plot
plt.figure(figsize=(8, 6))
plt.scatter(df['feature1'], df['feature2'], c=df['target'], alpha=0.7)
plt.title("Sample Classification Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.savefig("analysis.png")
print("Plot saved as analysis.png")