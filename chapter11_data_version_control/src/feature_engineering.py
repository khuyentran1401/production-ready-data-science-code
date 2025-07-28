"""Feature engineering stage for customer churn prediction pipeline."""

import pandas as pd
import numpy as np
import yaml
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from pathlib import Path


def load_params():
    """Load parameters from params.yaml file."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def engineer_features(df):
    """Create new features from existing data."""
    df = df.copy()
    
    # Create new features
    df['avg_monthly_charges'] = df['total_charges'] / (df['tenure'] + 1)  # +1 to avoid division by zero
    df['tenure_months'] = df['tenure']
    df['charges_per_month'] = df['monthly_charges']
    
    # Categorical encoding
    categorical_cols = df.select_dtypes(include=['object']).columns
    categorical_cols = categorical_cols.drop('customer_id', errors='ignore')
    
    le_dict = {}
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        le_dict[col] = le
        print(f"Encoded {col}: {len(le.classes_)} categories")
    
    return df, le_dict


def scale_features(df, target_col='churn', scaling_method='standard'):
    """Scale numerical features."""
    # Separate features and target
    feature_cols = [col for col in df.columns if col not in ['customer_id', target_col]]
    X = df[feature_cols]
    y = df[target_col]
    
    if scaling_method == 'standard':
        scaler = StandardScaler()
        X_scaled = pd.DataFrame(
            scaler.fit_transform(X),
            columns=X.columns,
            index=X.index
        )
    else:
        X_scaled = X
        scaler = None
    
    # Combine back with target
    df_scaled = X_scaled.copy()
    if 'customer_id' in df.columns:
        df_scaled['customer_id'] = df['customer_id']
    df_scaled[target_col] = y
    
    print(f"Scaled features using {scaling_method} scaling")
    return df_scaled, scaler


def select_features(df, target_col='churn', max_features=20, correlation_threshold=0.95):
    """Select the most important features."""
    feature_cols = [col for col in df.columns if col not in ['customer_id', target_col]]
    X = df[feature_cols]
    y = df[target_col]
    
    # Remove highly correlated features
    corr_matrix = X.corr().abs()
    upper_triangle = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )
    
    high_corr_features = [
        column for column in upper_triangle.columns 
        if any(upper_triangle[column] > correlation_threshold)
    ]
    
    if high_corr_features:
        X = X.drop(columns=high_corr_features)
        print(f"Removed {len(high_corr_features)} highly correlated features")
    
    # Select top features using univariate selection
    if len(X.columns) > max_features:
        selector = SelectKBest(f_classif, k=max_features)
        X_selected = selector.fit_transform(X, y)
        selected_features = X.columns[selector.get_support()].tolist()
        
        df_selected = pd.DataFrame(X_selected, columns=selected_features, index=X.index)
        print(f"Selected top {max_features} features using univariate selection")
    else:
        df_selected = X
        selected_features = X.columns.tolist()
        selector = None
    
    # Add back non-feature columns
    if 'customer_id' in df.columns:
        df_selected['customer_id'] = df['customer_id']
    df_selected[target_col] = y
    
    return df_selected, selected_features, selector


def main():
    """Main feature engineering function."""
    print("=== Feature Engineering Stage ===")
    
    # Load parameters
    params = load_params()
    feature_params = params["feature_engineering"]
    
    # Load cleaned data
    df = pd.read_csv("data/processed/clean_data.csv")
    print(f"Loaded cleaned data: {df.shape}")
    
    # Engineer features
    df_engineered, label_encoders = engineer_features(df)
    print(f"Engineered features: {df_engineered.shape}")
    
    # Scale features
    df_scaled, scaler = scale_features(
        df_engineered,
        scaling_method=feature_params["scaling_method"]
    )
    
    # Select features
    if feature_params["feature_selection"]:
        df_final, selected_features, feature_selector = select_features(
            df_scaled,
            max_features=feature_params["max_features"],
            correlation_threshold=feature_params["correlation_threshold"]
        )
    else:
        df_final = df_scaled
        selected_features = [col for col in df_scaled.columns if col not in ['customer_id', 'churn']]
        feature_selector = None
    
    # Save processed features
    Path("data/features").mkdir(parents=True, exist_ok=True)
    df_final.to_csv("data/features/features.csv", index=False)
    print(f"Saved engineered features to data/features/features.csv")
    
    # Print feature summary
    print(f"\nFeature Engineering Summary:")
    print(f"- Final feature count: {len([col for col in df_final.columns if col not in ['customer_id', 'churn']])}")
    print(f"- Selected features: {selected_features[:5]}..." if len(selected_features) > 5 else f"- Selected features: {selected_features}")
    print(f"- Final data shape: {df_final.shape}")


if __name__ == "__main__":
    main()