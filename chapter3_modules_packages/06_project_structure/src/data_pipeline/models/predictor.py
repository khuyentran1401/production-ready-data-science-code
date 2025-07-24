"""Model prediction functionality."""

import pandas as pd
from .trainer import ModelTrainer


class ModelPredictor:
    """Handles model predictions."""
    
    def __init__(self, trained_model: ModelTrainer):
        if not trained_model.is_trained:
            raise ValueError("Model must be trained before creating predictor")
        self.model = trained_model.model
    
    def predict(self, X: pd.DataFrame) -> pd.Series:
        """Make predictions on new data.
        
        Args:
            X: Features to predict on
            
        Returns:
            Predictions as a pandas Series
        """
        predictions = self.model.predict(X)
        return pd.Series(predictions, index=X.index)
    
    def predict_proba(self, X: pd.DataFrame) -> pd.DataFrame:
        """Get prediction probabilities.
        
        Args:
            X: Features to predict on
            
        Returns:
            DataFrame with prediction probabilities
        """
        probabilities = self.model.predict_proba(X)
        return pd.DataFrame(
            probabilities,
            index=X.index,
            columns=[f"class_{i}" for i in range(probabilities.shape[1])]
        )