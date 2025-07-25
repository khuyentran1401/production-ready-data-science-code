# Data Analysis Workflow

This example demonstrates a complete data analysis workflow using marimo.

## Files
- `data_analysis.py`: Complete data analysis notebook with visualization and insights

## Key Features Demonstrated
- Multi-cell data science workflow
- Library imports and data generation
- Data exploration and visualization  
- Statistical analysis and business insights
- Clean dependency chain throughout the analysis

## Running the Analysis

```bash
# Run the notebook
uv run --group chapter14 marimo edit data_analysis.py
```

## Workflow Steps

1. **Setup**: Import libraries (pandas, numpy, matplotlib)
2. **Data Creation**: Generate sample sales and marketing data
3. **Exploration**: Display dataset info and summary statistics
4. **Visualization**: Create scatter plots and histograms  
5. **Analysis**: Calculate correlations and derive business insights

## Interactive Features

- **Modify Parameters**: Change the random seed or data generation parameters
- **See Propagation**: Watch how changes automatically flow through the analysis
- **Update Visualizations**: Plots automatically refresh when data changes
- **Real-time Insights**: Business conclusions update based on new correlations

## Benefits Over Traditional Notebooks

- **Reproducible**: Always runs in the same order
- **Version Controllable**: Clean Python script format
- **Dependency Safe**: No hidden state or out-of-order execution
- **Interactive**: Modify parameters and see immediate results throughout the pipeline