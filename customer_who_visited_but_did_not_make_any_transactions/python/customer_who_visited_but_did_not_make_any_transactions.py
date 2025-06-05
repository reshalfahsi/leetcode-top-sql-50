import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return visits[
        ~visits['visit_id'].isin(
            visits.merge(transactions, on='visit_id')['visit_id']
        )
    ][['customer_id']].groupby(
        'customer_id'
    ).size().reset_index(name='count_no_trans')