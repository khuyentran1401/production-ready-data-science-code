"""Model training functionality."""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from ..config import MODEL_CONFIG


class ModelTrainer:
    """Handles model training and evaluation."""

    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=MODEL_CONFIG["n_estimators"],
            random_state=MODEL_CONFIG["random_state"]
        )
        self.is_trained = False

    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """Train the model on training data.
        
        Args:
            X_train: Training features
            y_train: Training targets
        """
        self.model.fit(X_train, y_train)
        self.is_trained = True
        print(f"Model trained on {len(X_train)} samples")

    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> float:
        """Evaluate the model on test data.
        
        Args:
            X_test: Test features
            y_test: Test targets
            
        Returns:
            Accuracy score
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before evaluation")

        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy:.3f}")
        return accuracy

    def get_feature_importance(self) -> pd.Series:
        """Get feature importance scores.
        
        Returns:
            Series with feature importance scores
        """
        if not self.is_trained:
            raise ValueError("Model must be trained to get feature importance")

        return pd.Series(
            self.model.feature_importances_,
            index=self.model.feature_names_in_
        )
