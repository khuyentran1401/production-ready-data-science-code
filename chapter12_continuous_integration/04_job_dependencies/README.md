# Job Dependencies - ML Workflow

Job dependencies in a machine learning workflow, ensuring tasks execute in the correct order.

## Files

- `.github/workflows/ml_workflow.yaml` - Complete ML pipeline with job dependencies

## Key Points

- Uses `needs` keyword to define job dependencies
- Enables parallel execution where possible (evaluation and prediction run simultaneously)

## How to Run

Workflow triggers automatically on pull requests to main branch, executing jobs in this order:

```
data_preprocessing → model_training → evaluate_model
                                   → get_predictions
```

## Expected Output

Jobs execute in correct sequence with parallel execution where safe, ensuring efficient resource usage and proper failure handling.

## Try This

1. **Study the dependencies**: Examine how `needs` creates the execution graph
2. **Test failure handling**: See how a failed training job prevents dependent jobs from running
3. **Observe parallelism**: Watch evaluation and prediction jobs run simultaneously after training

## Learn More

← [Back to Chapter 12](../README.md)

---

← [Previous: 03_generate_report](../03_generate_report/README.md)

*Example 4 of 4*