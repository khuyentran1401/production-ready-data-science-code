"""Model evaluation stage for customer churn prediction pipeline."""

import pandas as pd
import numpy as np
import yaml
import pickle
import json
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from pathlib import Path


def load_params():
    """Load parameters from params.yaml file."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def load_model():
    """Load the trained model."""
    with open("models/model.pkl", "rb") as f:
        model_data = pickle.load(f)
    return model_data['model'], model_data['feature_names']


def prepare_test_data(df, feature_names, test_size=0.2, random_state=42):
    """Prepare test data for evaluation."""
    # Separate features and target
    feature_cols = [col for col in df.columns if col not in ['customer_id', 'churn']]
    X = df[feature_cols]
    y = df['churn']
    
    # Ensure we have the same features as training
    X = X[feature_names]
    
    # Split data (use same split as training)
    _, X_test, _, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    return X_test, y_test


def evaluate_model(model, X_test, y_test, X_full, y_full, cv_folds=5):
    """Evaluate model performance with multiple metrics."""
    # Test set predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Cross-validation scores
    cv_scores = cross_val_score(model, X_full, y_full, cv=cv_folds, scoring='accuracy')
    cv_mean = cv_scores.mean()
    cv_std = cv_scores.std()
    
    # Classification report
    class_report = classification_report(y_test, y_pred, output_dict=True)
    
    metrics = {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1_score": float(f1),
        "cv_accuracy_mean": float(cv_mean),
        "cv_accuracy_std": float(cv_std),
        "test_samples": int(len(y_test)),
        "positive_class_ratio": float(y_test.mean())
    }
    
    return metrics, class_report


def print_evaluation_results(metrics, class_report):
    """Print evaluation results in a formatted way."""
    print("=== Model Evaluation Results ===")
    print(f"Test Set Performance:")
    print(f"  Accuracy:  {metrics['accuracy']:.4f}")
    print(f"  Precision: {metrics['precision']:.4f}")
    print(f"  Recall:    {metrics['recall']:.4f}")
    print(f"  F1-Score:  {metrics['f1_score']:.4f}")
    
    print(f"\nCross-Validation (5-fold):")
    print(f"  CV Accuracy: {metrics['cv_accuracy_mean']:.4f} ± {metrics['cv_accuracy_std']:.4f}")
    
    print(f"\nDataset Info:")
    print(f"  Test samples: {metrics['test_samples']}")
    print(f"  Positive class ratio: {metrics['positive_class_ratio']:.3f}")
    
    print(f"\nDetailed Classification Report:")
    print(f"  Class 0 (No Churn) - Precision: {class_report['0']['precision']:.3f}, Recall: {class_report['0']['recall']:.3f}")
    print(f"  Class 1 (Churn)    - Precision: {class_report['1']['precision']:.3f}, Recall: {class_report['1']['recall']:.3f}")


def main():
    """Main model evaluation function."""
    print("=== Model Evaluation Stage ===")
    
    # Load parameters
    params = load_params()
    eval_params = params["evaluation"]
    
    # Load model and feature data
    model, feature_names = load_model()
    df = pd.read_csv("data/features/features.csv")
    
    print(f"Loaded model and feature data: {df.shape}")
    
    # Prepare test data
    X_test, y_test = prepare_test_data(
        df, 
        feature_names,
        test_size=eval_params["test_size"],
        random_state=eval_params["random_state"]
    )
    
    # Prepare full dataset for cross-validation
    X_full = df[feature_names]
    y_full = df['churn']
    
    # Evaluate model
    metrics, class_report = evaluate_model(
        model, X_test, y_test, X_full, y_full,
        cv_folds=eval_params["cv_folds"]
    )
    
    # Print results
    print_evaluation_results(metrics, class_report)
    
    # Save metrics
    Path("metrics").mkdir(parents=True, exist_ok=True)
    with open("metrics/scores.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    print("\nSaved evaluation metrics to metrics/scores.json")


if __name__ == "__main__":
    main()