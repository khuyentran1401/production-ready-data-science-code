"""
Shared fixtures for data analysis tests.

This file contains fixtures that are available to all test files
in this directory and subdirectories.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


@pytest.fixture
def sample_dataframe():
    """
    Create a sample DataFrame for testing.
    This fixture is available to all tests in this directory.
    """
    np.random.seed(42)  # For reproducible results
    
    data = {
        "id": range(1, 101),
        "name": [f"Customer_{i}" for i in range(1, 101)],
        "age": np.random.randint(18, 80, 100),
        "score": np.random.normal(75, 15, 100),
        "category": np.random.choice(["A", "B", "C"], 100),
        "is_active": np.random.choice([True, False], 100),
        "signup_date": [
            datetime(2023, 1, 1) + timedelta(days=i) 
            for i in np.random.randint(0, 365, 100)
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values for testing
    df.loc[df.sample(5).index, "score"] = np.nan
    df.loc[df.sample(3).index, "age"] = np.nan
    
    return df


@pytest.fixture
def sales_data():
    """
    Create sample sales data for more complex testing scenarios.
    """
    np.random.seed(123)
    
    products = ["Widget_A", "Widget_B", "Widget_C", "Widget_D"]
    regions = ["North", "South", "East", "West"]
    
    data = []
    for _ in range(200):
        data.append({
            "product": np.random.choice(products),
            "region": np.random.choice(regions),
            "sales_amount": np.random.uniform(100, 5000),
            "quantity": np.random.randint(1, 50),
            "discount": np.random.uniform(0, 0.3),
            "month": np.random.randint(1, 13),
            "year": np.random.choice([2022, 2023])
        })
    
    df = pd.DataFrame(data)
    df["profit"] = df["sales_amount"] * (1 - df["discount"]) * 0.2
    
    return df


@pytest.fixture
def empty_dataframe():
    """
    Create an empty DataFrame for edge case testing.
    """
    return pd.DataFrame()


@pytest.fixture
def single_row_dataframe():
    """
    Create a DataFrame with a single row for boundary testing.
    """
    return pd.DataFrame({
        "col1": [1],
        "col2": ["test"],
        "col3": [3.14]
    })


@pytest.fixture(scope="module")
def large_dataframe():
    """
    Create a large DataFrame for performance testing.
    This fixture has module scope so it's created once per test module.
    """
    np.random.seed(999)
    
    size = 10000
    data = {
        "numeric_col1": np.random.normal(0, 1, size),
        "numeric_col2": np.random.exponential(2, size),
        "categorical_col": np.random.choice(["X", "Y", "Z"], size),
        "boolean_col": np.random.choice([True, False], size),
        "string_col": [f"item_{i}" for i in range(size)]
    }
    
    return pd.DataFrame(data)


@pytest.fixture
def dataframe_with_outliers():
    """
    Create a DataFrame with obvious outliers for filtering tests.
    """
    np.random.seed(456)
    
    # Normal data
    normal_data = np.random.normal(50, 10, 95)
    
    # Add outliers
    outliers = [200, -100, 500, -200, 300]
    
    data = {
        "values": list(normal_data) + outliers,
        "group": ["normal"] * 95 + ["outlier"] * 5,
        "id": range(100)
    }
    
    return pd.DataFrame(data)


@pytest.fixture
def setup_and_teardown_example():
    """
    Example fixture that demonstrates setup and teardown.
    This uses yield to provide cleanup after the test.
    """
    # Setup: Create some resource
    print("\nSETUP: Creating test resource")
    resource = {"connection": "database_connection", "status": "connected"}
    
    # Provide the resource to the test
    yield resource
    
    # Teardown: Clean up after the test
    print("TEARDOWN: Cleaning up test resource")
    resource["status"] = "disconnected"


@pytest.fixture
def fixture_with_parameters(request):
    """
    Example of a parametrized fixture.
    This fixture can be used with different parameter values.
    """
    if hasattr(request, 'param'):
        size = request.param
    else:
        size = 10
    
    return pd.DataFrame({
        "x": range(size),
        "y": [i * 2 for i in range(size)]
    })