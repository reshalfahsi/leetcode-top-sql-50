import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(bonus, on='empId', how='left')[['name', 'bonus']]
    result = result[(result['bonus'] < 1000) | (result['bonus'].isna())]
    return result