import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Assign row numbers to each player's events, ordered by event_date
    activity['rank'] = activity.groupby('player_id')['event_date'].rank(method='first').astype(int)
    
    # Step 2: Filter to keep only the first two events per player
    ranked_date = activity[activity['rank'] <= 2][['player_id', 'event_date']]
    
    # Step 3: Calculate login_streak_flag (1 if consecutive days, 0 otherwise)
    # Sort by player_id and event_date to ensure correct lag calculation
    ranked_date = ranked_date.sort_values(['player_id', 'event_date'])
    
    # Calculate difference between consecutive event_dates
    ranked_date['prev_event_date'] = ranked_date.groupby('player_id')['event_date'].shift(1)
    ranked_date['login_streak_flag'] = (
        (ranked_date['event_date'] - ranked_date['prev_event_date']).dt.days == 1
    ).astype(int)
    
    # Step 4: Get the first row per player_id, prioritizing login_streak_flag DESC
    first_rows = ranked_date.sort_values(
        ['player_id', 'login_streak_flag'], ascending=[True, False]
    ).drop_duplicates('player_id', keep='first')
    
    # Step 5: Calculate fraction: sum of login_streak_flag / total count
    total_players = first_rows['player_id'].nunique()
    streak_count = first_rows['login_streak_flag'].sum()
    fraction = round(streak_count / total_players, 2) if total_players > 0 else 0.0
    
    # Return as a DataFrame for consistency with SQL output
    return pd.DataFrame({'fraction': [fraction]})