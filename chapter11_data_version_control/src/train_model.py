"""Model training stage for customer churn prediction pipeline."""

import pandas as pd
import numpy as np
import yaml
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from pathlib import Path


def load_params():
    """Load parameters from params.yaml file."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def prepare_data(df, test_size=0.2, random_state=42):
    """Split data into training and testing sets."""
    # Separate features and target
    feature_cols = [col for col in df.columns if col not in ['customer_id', 'churn']]
    X = df[feature_cols]
    y = df['churn']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set: {X_test.shape[0]} samples")
    print(f"Feature count: {X_train.shape[1]}")
    
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train, model_params):
    """Train the Random Forest model."""
    # Create model with parameters
    model = RandomForestClassifier(
        n_estimators=model_params["n_estimators"],
        max_depth=model_params["max_depth"],
        min_samples_split=model_params["min_samples_split"],
        min_samples_leaf=model_params["min_samples_leaf"],
        random_state=model_params["random_state"],
        n_jobs=-1
    )
    
    # Train model
    print("Training Random Forest model...")
    model.fit(X_train, y_train)
    
    # Print feature importance
    feature_importance = pd.DataFrame({
        'feature': X_train.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\nTop 5 Most Important Features:")
    for i, row in feature_importance.head().iterrows():
        print(f"  {row['feature']}: {row['importance']:.4f}")
    
    return model


def main():
    """Main model training function."""
    print("=== Model Training Stage ===")
    
    # Load parameters
    params = load_params()
    model_params = params["model"]
    eval_params = params["evaluation"]
    
    # Load feature data
    df = pd.read_csv("data/features/features.csv")
    print(f"Loaded feature data: {df.shape}")
    
    # Prepare training/test split
    X_train, X_test, y_train, y_test = prepare_data(
        df,
        test_size=eval_params["test_size"],
        random_state=eval_params["random_state"]
    )
    
    # Train model
    model = train_model(X_train, y_train, model_params)
    
    # Calculate training accuracy
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    
    print(f"\nModel Performance:")
    print(f"- Training accuracy: {train_accuracy:.4f}")
    print(f"- Test accuracy: {test_accuracy:.4f}")
    
    # Save model
    Path("models").mkdir(parents=True, exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump({
            'model': model,
            'feature_names': X_train.columns.tolist(),
            'model_params': model_params
        }, f)
    
    print("Saved trained model to models/model.pkl")


if __name__ == "__main__":
    main()