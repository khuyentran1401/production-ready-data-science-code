import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
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


def train_model(X, y):
    """Train a model and return model with test data."""
    print("Training model...")
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print(f"Model trained on {len(X_train)} samples")
    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return accuracy."""
    print("Evaluating model...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.3f}")
    return accuracy


# Main execution
if __name__ == "__main__":
    # Create sample data for demonstration
    print("Creating sample dataset...")
    sample_data = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10,
        "feature2": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] * 10,
        "feature3": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] * 10,
        "target": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0] * 10
    })
    sample_data.to_csv("sample_data.csv", index=False)

    # Run the pipeline
    df = load_data("sample_data.csv")
    X, y = preprocess_data(df)
    model, X_test, y_test = train_model(X, y)
    accuracy = evaluate_model(model, X_test, y_test)

    print(f"\nFinal accuracy: {accuracy:.3f}")
