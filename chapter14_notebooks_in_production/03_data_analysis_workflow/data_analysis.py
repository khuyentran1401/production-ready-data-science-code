import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    # Import libraries
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    return (pd, np, plt)


@app.cell
def _(pd, np):
    # Create sample dataset
    np.random.seed(42)
    data = {
        'sales': np.random.normal(1000, 200, 100),
        'marketing_spend': np.random.normal(500, 100, 100),
        'customer_satisfaction': np.random.uniform(1, 5, 100)
    }
    df = pd.DataFrame(data)
    print("Dataset created:")
    print(df.head())
    return (data, df)


@app.cell
def _(df):
    # Data exploration and summary statistics
    print("Dataset Info:")
    print(f"Shape: {df.shape}")
    print("\nSummary Statistics:")
    print(df.describe())
    return


@app.cell
def _(df, plt):
    # Visualization - scatter plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Sales vs Marketing Spend
    axes[0].scatter(df['marketing_spend'], df['sales'], alpha=0.6)
    axes[0].set_xlabel('Marketing Spend')
    axes[0].set_ylabel('Sales')
    axes[0].set_title('Sales vs Marketing Spend')
    
    # Sales Distribution
    axes[1].hist(df['sales'], bins=20, alpha=0.7)
    axes[1].set_xlabel('Sales')
    axes[1].set_ylabel('Frequency')
    axes[1].set_title('Sales Distribution')
    
    plt.tight_layout()
    plt.show()
    return (fig, axes)


@app.cell
def _(df, np):
    # Analysis - correlation and insights
    correlation_matrix = df.corr()
    print("Correlation Matrix:")
    print(correlation_matrix)
    
    # Key insights
    sales_marketing_corr = correlation_matrix.loc['sales', 'marketing_spend']
    print(f"\nKey Insight: Sales and Marketing correlation: {sales_marketing_corr:.3f}")
    
    if sales_marketing_corr > 0.5:
        insight = "Strong positive correlation - marketing investment drives sales"
    elif sales_marketing_corr > 0.2:
        insight = "Moderate positive correlation - marketing has some impact on sales"
    else:
        insight = "Weak correlation - other factors may be more important for sales"
    
    print(f"Business insight: {insight}")
    return (correlation_matrix, sales_marketing_corr, insight)


if __name__ == "__main__":
    app.run()