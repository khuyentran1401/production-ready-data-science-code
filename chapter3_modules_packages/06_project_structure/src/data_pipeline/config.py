"""Configuration management for the data pipeline."""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model configuration
MODEL_CONFIG = {
    "random_state": 42,
    "test_size": 0.2,
    "n_estimators": 100,
}

# File paths
SAMPLE_DATA_FILE = RAW_DATA_DIR / "sample_data.csv"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "processed_data.csv"

def get_config():
    """Get the current configuration dictionary."""
    return {
        "data_dir": str(DATA_DIR),
        "raw_data_dir": str(RAW_DATA_DIR),
        "processed_data_dir": str(PROCESSED_DATA_DIR),
        "model_config": MODEL_CONFIG,
    }
