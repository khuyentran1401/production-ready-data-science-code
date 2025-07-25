"""
Report generation script for CI workflow demonstration.

This script would generate analysis reports when triggered by changes.
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def generate_report():
    """Generate a sample analysis report."""
    # Create sample data
    data = {
        'date': pd.date_range('2023-01-01', periods=30),
        'sales': [100 + i * 5 + (i % 7) * 10 for i in range(30)],
        'customers': [50 + i * 2 + (i % 5) * 5 for i in range(30)]
    }
    df = pd.DataFrame(data)
    
    # Create a simple plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    ax1.plot(df['date'], df['sales'])
    ax1.set_title('Daily Sales')
    ax1.set_ylabel('Sales ($)')
    
    ax2.plot(df['date'], df['customers'])
    ax2.set_title('Daily Customers')
    ax2.set_ylabel('Number of Customers')
    
    plt.tight_layout()
    
    # Save the report
    plt.savefig('analysis/report.pdf')
    print("Report generated successfully at analysis/report.pdf")


if __name__ == "__main__":
    generate_report()