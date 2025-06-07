import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Define categories and calculate counts
    categories = ['Low Salary', 'Average Salary', 'High Salary']
    counts = [
        (accounts['income'] < 20000).sum(),
        ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum(),
        (accounts['income'] > 50000).sum()
    ]

    # Create result DataFrame
    return pd.DataFrame({
        'category': categories,
        'accounts_count': counts
    })