import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # Calculate the total number of users
    total_users = len(users['user_id'])

    # Group by contest_id, count users, calculate percentage, and round to 2 decimals
    result = (register.groupby('contest_id')
            .agg({'user_id': 'count'})
            .assign(percentage=lambda x: round(x['user_id'] * 100.0 / total_users, 2))
            .reset_index()
            [['contest_id', 'percentage']])

    # Sort by percentage in descending order, then by contest_id in ascending order
    result = result.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    return result