import pandas as pd
from typing import Dict

def load_sales_data(filepath: str) -> pd.DataFrame:
    """Load sales data from CSV file."""
    df = pd.read_csv(filepath, parse_dates=['date'])
    return df

def calculate_metrics(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate key business metrics."""
    metrics = {
        'total_revenue': df['revenue'].sum(),
        'avg_revenue_per_sale': df['revenue'].mean(),
        'total_quantity_sold': df['quantity'].sum(),
        'unique_products': df['product'].nunique()
    }
    return metrics

def get_top_performers(df: pd.DataFrame, by: str = 'product', n: int = 5) -> pd.DataFrame:
    """Get top performers by specified dimension."""
    return df.groupby(by)['revenue'].sum().nlargest(n).reset_index()

if __name__ == "__main__":
    print("Data processing module loaded successfully!")