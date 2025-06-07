import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create lagged columns for comparison
    # .shift(1) gets the value from the previous row
    logs['num_prev_1'] = logs['num'].shift(1)
    # .shift(2) gets the value from 2 rows before
    logs['num_prev_2'] = logs['num'].shift(2)

    # Step 2: Identify rows where num is consecutive for at least 3 times
    consecutive_condition = (
        (logs['num'] == logs['num_prev_1']) &
        (logs['num_prev_1'] == logs['num_prev_2'])
    )

    # Step 3: Filter the DataFrame based on the condition and select 
    # the distinct 'num'
    # We only care about the 'num' values from the rows that satisfy 
    # the condition
    result_df = logs[consecutive_condition][['num']].drop_duplicates()

    # Step 4: Rename the column
    return result_df.rename(columns={'num': 'ConsecutiveNums'})