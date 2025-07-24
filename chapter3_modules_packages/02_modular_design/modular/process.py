import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(filepath):
    """Load data from a CSV file."""
    print(f"Loading data from {filepath}")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df


def preprocess_data(df):
    """Preprocess the data by handling missing values and scaling."""
    print("Preprocessing data...")
    # Handle missing values
    df = df.dropna()

    # Separate features and target
    X = df.drop("target", axis=1)
    y = df["target"]

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

    print(f"Preprocessed data: {len(X_scaled)} samples, {len(X_scaled.columns)} features")
    return X_scaled, y
