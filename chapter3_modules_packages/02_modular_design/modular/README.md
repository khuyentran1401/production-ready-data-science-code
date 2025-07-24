# Modular Design Example

This example shows how to **break down monolithic code** into focused, maintainable modules. Each module has a clear responsibility, making the code easier to understand, test, and maintain.

## Modular Structure

### `process.py` - Data Processing Module
**Responsibility:** Data loading and preprocessing
- `load_data()` - Loads data from CSV files
- `preprocess_data()` - Handles missing values and feature scaling

### `train_model.py` - Model Training Module  
**Responsibility:** Machine learning model operations
- `train_model()` - Trains the model and splits data
- `evaluate_model()` - Evaluates model performance
- `cross_validate()` - Performs cross-validation (extended functionality)

### `main.py` - Coordination Module
**Responsibility:** Orchestrates the entire workflow
- Imports functions from other modules
- Creates sample data
- Coordinates the execution flow

## How to Run

```bash
uv run main.py
```

## Expected Output

```
Creating sample dataset...
Loading data from sample_data.csv
Loaded 100 rows and 4 columns
Preprocessing data...
Preprocessed data: 100 samples, 3 features
Training model...
Model trained on 80 samples
Evaluating model...
Model accuracy: 1.000
```
