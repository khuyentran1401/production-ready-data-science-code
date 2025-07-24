# API Documentation

## data_pipeline.data

### loader.py

#### `load_data(filename: str) -> pd.DataFrame`
Load data from a CSV file in the raw data directory.

**Parameters:**
- `filename`: Name of the CSV file to load

**Returns:**
- DataFrame containing the loaded data

#### `save_data(data: pd.DataFrame, filename: str, directory: Path) -> None`
Save data to a CSV file.

**Parameters:**
- `data`: DataFrame to save
- `filename`: Name of the CSV file
- `directory`: Directory to save the file in

### processor.py

#### `preprocess_data(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]`
Preprocess the raw data for machine learning.

**Parameters:**
- `data`: Raw data DataFrame

**Returns:**
- Tuple of (features, target)

#### `split_data(X: pd.DataFrame, y: pd.Series) -> tuple`
Split data into training and testing sets.

**Parameters:**
- `X`: Feature matrix
- `y`: Target vector

**Returns:**
- Tuple of (X_train, X_test, y_train, y_test)

## data_pipeline.models

### trainer.py

#### `class ModelTrainer`
Handles model training and evaluation.

**Methods:**
- `train(X_train, y_train)`: Train the model on training data
- `evaluate(X_test, y_test)`: Evaluate the model on test data
- `get_feature_importance()`: Get feature importance scores

### predictor.py

#### `class ModelPredictor`
Handles model predictions.

**Methods:**
- `predict(X)`: Make predictions on new data
- `predict_proba(X)`: Get prediction probabilities

## data_pipeline.utils

### helpers.py

#### `format_results(accuracy: float, feature_importance: pd.Series) -> str`
Format model results for display.

#### `create_summary(data: pd.DataFrame) -> dict`
Create a data summary dictionary.

#### `validate_data(data: pd.DataFrame, required_columns: list) -> bool`
Validate that data contains required columns.