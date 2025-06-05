import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Left join Signups with Confirmations on user_id
    merged = signups.merge(confirmations, on='user_id', how='left')
    
    # Create a column for confirmed actions (1 if confirmed, 0 otherwise)
    merged['is_confirmed'] = (merged['action'] == 'confirmed').astype(int)
    
    # Group by user_id and calculate mean of is_confirmed, rounded to 2 decimals
    result = merged.groupby('user_id')['is_confirmed'].mean().round(2).reset_index()
    
    # Rename the column to confirmation_rate
    result.columns = ['user_id', 'confirmation_rate']
    
    return result