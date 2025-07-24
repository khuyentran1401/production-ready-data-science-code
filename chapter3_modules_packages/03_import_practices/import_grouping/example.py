# Standard library imports
import datetime
import json
import os
import sys

# Third-party imports
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Local application imports
from utils import helpers


def demonstrate_proper_import_organization():
    """
    This function demonstrates how to properly organize imports
    following PEP 8 guidelines and best practices.
    """
    print("🔄 Import Organization Example")
    print("=" * 40)

    # Standard library usage
    print(f"📅 Current date/time: {datetime.datetime.now()}")
    print(f"🐍 Python version: {sys.version_info.major}.{sys.version_info.minor}")
    print(f"📁 Current directory: {os.getcwd()}")

    # Third-party library usage
    print(f"🔢 NumPy version: {np.__version__}")
    print(f"🐼 Pandas version: {pd.__version__}")

    # Create sample data using third-party libraries
    np.random.seed(42)
    data = {
        "feature1": np.random.normal(0, 1, 100),
        "feature2": np.random.normal(2, 1.5, 100),
        "target": np.random.choice([0, 1], 100)
    }
    df = pd.DataFrame(data)

    print(f"📊 Created DataFrame with shape: {df.shape}")

    # Demonstrate machine learning workflow
    X = df[["feature1", "feature2"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(random_state=42)
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, predictions)

    print(f"🎯 Model accuracy: {accuracy:.3f}")

    # Use local helper function
    print(f"🔗 {helpers()}")

    # Save results to JSON (using standard library)
    results = {
        "accuracy": float(accuracy),
        "test_size": len(y_test),
        "timestamp": datetime.datetime.now().isoformat()
    }

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("💾 Results saved to results.json")

    print("\n✅ Import Organization Benefits:")
    print("- Standard library imports first")
    print("- Third-party imports second")
    print("- Local imports last")
    print("- Each group sorted alphabetically")
    print("- Clear separation between groups")
    print("- Easy to identify dependencies")


if __name__ == "__main__":
    demonstrate_proper_import_organization()
