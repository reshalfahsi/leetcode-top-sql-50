import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by managerId and count direct reports
    report_counts = employee.groupby('managerId').size().reset_index(name='count')
    
    # Filter for managers with at least 5 direct reports
    valid_managers = report_counts[report_counts['count'] >= 5]
    
    # Merge with employee table to get manager names
    result = employee[employee['id'].isin(valid_managers['managerId'])][['name']]
    
    return result