"""Data preparation stage for customer churn prediction pipeline."""

import pandas as pd
import yaml
import numpy as np
from pathlib import Path


def load_params():
    """Load parameters from params.yaml file."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def clean_data(df, missing_threshold=0.1, outlier_method="iqr", outlier_factor=1.5):
    """Clean the raw customer data."""
    print(f"Input data shape: {df.shape}")
    
    # Handle missing values
    missing_ratio = df.isnull().sum() / len(df)
    high_missing_cols = missing_ratio[missing_ratio > missing_threshold].index
    if len(high_missing_cols) > 0:
        print(f"Dropping columns with >{missing_threshold*100}% missing: {list(high_missing_cols)}")
        df = df.drop(columns=high_missing_cols)
    
    # Fill remaining missing values
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())
    
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    # Handle outliers for numerical columns
    if outlier_method == "iqr":
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        numerical_cols = numerical_cols.drop('customer_id', errors='ignore')
        numerical_cols = numerical_cols.drop('churn', errors='ignore')
        
        for col in numerical_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - outlier_factor * IQR
            upper_bound = Q3 + outlier_factor * IQR
            
            outliers_before = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
            if outliers_before > 0:
                df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
                print(f"Clipped {outliers_before} outliers in {col}")
    
    print(f"Cleaned data shape: {df.shape}")
    return df


def main():
    """Main data preparation function."""
    print("=== Data Preparation Stage ===")
    
    # Load parameters
    params = load_params()
    prep_params = params["data_preparation"]
    
    # Load raw data
    df = pd.read_csv("data/raw/customer_churn.csv")
    print(f"Loaded raw data: {df.shape}")
    
    # Clean data
    df_clean = clean_data(
        df,
        missing_threshold=prep_params["missing_threshold"],
        outlier_method=prep_params["outlier_method"],
        outlier_factor=prep_params["outlier_factor"]
    )
    
    # Save cleaned data
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    df_clean.to_csv("data/processed/clean_data.csv", index=False)
    print("Saved cleaned data to data/processed/clean_data.csv")
    
    # Print basic statistics
    print(f"\nData Quality Summary:")
    print(f"- Total customers: {len(df_clean)}")
    print(f"- Churn rate: {df_clean['churn'].mean():.1%}")
    print(f"- Missing values: {df_clean.isnull().sum().sum()}")


if __name__ == "__main__":
    main()