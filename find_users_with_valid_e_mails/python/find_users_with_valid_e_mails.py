import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where mail matches the regex pattern for leetcode.com emails
    df = users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9_\.\-]*@leetcode\.com$')]

    # Select the required columns
    return df[['user_id', 'name', 'mail']]