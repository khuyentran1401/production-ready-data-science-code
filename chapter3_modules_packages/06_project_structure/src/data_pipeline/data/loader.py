"""Data loading functions."""

import pandas as pd
from pathlib import Path
from ..config import RAW_DATA_DIR


def load_data(filename: str) -> pd.DataFrame:
    """Load data from a CSV file in the raw data directory.
    
    Args:
        filename: Name of the CSV file to load
        
    Returns:
        DataFrame containing the loaded data
    """
    filepath = RAW_DATA_DIR / filename
    
    if not filepath.exists():
        # Create sample data if file doesn't exist
        sample_data = pd.DataFrame({
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [2, 4, 6, 8, 10], 
            "target": [0, 1, 0, 1, 0]
        })
        filepath.parent.mkdir(parents=True, exist_ok=True)
        sample_data.to_csv(filepath, index=False)
        print(f"Created sample data at {filepath}")
    
    data = pd.read_csv(filepath)
    print(f"Loaded {len(data)} rows from {filename}")
    return data


def save_data(data: pd.DataFrame, filename: str, directory: Path) -> None:
    """Save data to a CSV file.
    
    Args:
        data: DataFrame to save
        filename: Name of the CSV file
        directory: Directory to save the file in
    """
    directory.mkdir(parents=True, exist_ok=True)
    filepath = directory / filename
    data.to_csv(filepath, index=False)
    print(f"Saved {len(data)} rows to {filepath}")