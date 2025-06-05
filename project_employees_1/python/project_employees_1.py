import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # Join Project and Employee on employee_id
    merged = project.merge(employee, on='employee_id', how='inner')
    
    # Group by project_id and calculate average experience years, rounded to 2 decimals
    result = merged.groupby('project_id')['experience_years'].mean().round(2).reset_index()
    
    # Rename the column to average_years
    result.columns = ['project_id', 'average_years']
    
    return result