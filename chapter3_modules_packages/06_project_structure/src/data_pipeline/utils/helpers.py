"""Helper utility functions."""

import pandas as pd
from datetime import datetime


def format_results(accuracy: float, feature_importance: pd.Series) -> str:
    """Format model results for display.
    
    Args:
        accuracy: Model accuracy score
        feature_importance: Feature importance Series
        
    Returns:
        Formatted results string
    """
    results = [
        f"Model Performance Summary",
        f"=" * 25,
        f"Accuracy: {accuracy:.3f}",
        f"",
        f"Feature Importance:",
    ]
    
    for feature, importance in feature_importance.sort_values(ascending=False).items():
        results.append(f"  {feature}: {importance:.3f}")
    
    return "\n".join(results)


def create_summary(data: pd.DataFrame) -> dict:
    """Create a data summary dictionary.
    
    Args:
        data: DataFrame to summarize
        
    Returns:
        Dictionary with summary statistics
    """
    return {
        "timestamp": datetime.now().isoformat(),
        "shape": data.shape,
        "columns": list(data.columns),
        "dtypes": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "numeric_summary": data.describe().to_dict() if len(data.select_dtypes(include=['number']).columns) > 0 else None
    }


def validate_data(data: pd.DataFrame, required_columns: list) -> bool:
    """Validate that data contains required columns.
    
    Args:
        data: DataFrame to validate
        required_columns: List of required column names
        
    Returns:
        True if valid, False otherwise
    """
    missing_columns = set(required_columns) - set(data.columns)
    if missing_columns:
        print(f"Missing required columns: {missing_columns}")
        return False
    return True