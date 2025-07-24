import pandas as pd
from process import load_data, preprocess_data
from train_model import evaluate_model, train_model

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

    # Run the pipeline using imported functions
    df = load_data("sample_data.csv")
    X, y = preprocess_data(df)
    model, X_test, y_test = train_model(X, y)
    accuracy = evaluate_model(model, X_test, y_test)

    print(f"\nFinal accuracy: {accuracy:.3f}")
