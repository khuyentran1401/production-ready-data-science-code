"""Data preprocessing functions."""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from ..config import MODEL_CONFIG


def preprocess_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Preprocess the raw data for machine learning.
    
    Args:
        data: Raw data DataFrame
        
    Returns:
        Tuple of (features, target)
    """
    # Separate features and target
    feature_cols = [col for col in data.columns if col != "target"]
    X = data[feature_cols]
    y = data["target"]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X),
        columns=X.columns,
        index=X.index
    )
    
    print(f"Preprocessed data: {len(X_scaled)} samples, {X_scaled.shape[1]} features")
    return X_scaled, y


def split_data(X: pd.DataFrame, y: pd.Series) -> tuple:
    """Split data into training and testing sets.
    
    Args:
        X: Feature matrix
        y: Target vector
        
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    return train_test_split(
        X, y, 
        test_size=MODEL_CONFIG["test_size"],
        random_state=MODEL_CONFIG["random_state"]
    )