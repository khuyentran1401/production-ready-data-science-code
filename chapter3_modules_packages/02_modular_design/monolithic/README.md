# Monolithic Design Example

This example shows a **monolithic approach** where all functionality is contained in a single file. While this works for small projects, it becomes difficult to maintain as the codebase grows.

## What This Shows

This `main.py` contains multiple responsibilities in one file:
- **Data loading** (`load_data` function)
- **Data preprocessing** (`preprocess_data` function) 
- **Model training** (`train_model` function)
- **Model evaluation** (`evaluate_model` function)
- **Main execution logic**

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
Model accuracy: 0.850

Final accuracy: 0.850
```