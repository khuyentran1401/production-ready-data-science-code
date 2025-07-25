# Job Dependencies - ML Workflow

This example demonstrates job dependencies in a machine learning workflow, ensuring tasks execute in the correct order.

## Files
- `.github/workflows/ml_workflow.yaml`: Complete ML pipeline with job dependencies

## Workflow Structure

The workflow contains four jobs with specific dependencies:

1. **data_preprocessing** - Runs first (no dependencies)
2. **model_training** - Waits for data preprocessing to complete
3. **evaluate_model** - Waits for model training to complete
4. **get_predictions** - Also waits for model training to complete

## Job Dependencies

```
data_preprocessing → model_training → evaluate_model
                                   → get_predictions
```

## Key Features Demonstrated
- `needs` keyword to define job dependencies
- Sequential execution where required (data → training → evaluation/prediction)
- Parallel execution where possible (evaluation and prediction run simultaneously)
- Proper workflow orchestration for ML pipelines
- Failure handling (if training fails, dependent jobs won't run)

## How It Works

1. **Trigger**: Pull request to main branch
2. **Data Processing**: Prepares and cleans data first
3. **Model Training**: Trains model using processed data
4. **Parallel Evaluation**: Both evaluation and prediction jobs run simultaneously after training completes

## Benefits

- **Efficiency**: Independent jobs run in parallel
- **Reliability**: Dependencies ensure correct execution order
- **Failure Safety**: Failed jobs prevent dependent jobs from running with bad inputs
- **Resource Optimization**: No wasted compute on jobs that would fail due to missing inputs