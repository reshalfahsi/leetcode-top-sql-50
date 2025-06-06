import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Group by reports_to to count direct reports and calculate average age
    manager_stats = employees.groupby("reports_to").agg(
        reports_count=("employee_id", "count"), average_age=("age", "mean")
    )

    # Round average_age to nearest integer using numpy.round to mimic 
    # SQL ROUND
    manager_stats["average_age"] = manager_stats["average_age"].apply(
        lambda x: int(x + 0.5)
    )

    # Filter out employees who are not managers (no reports)
    manager_stats = manager_stats[manager_stats["reports_count"] > 0]

    # Merge with employees to get manager names
    result = manager_stats.merge(
        employees[["employee_id", "name"]], 
        left_index=True, 
        right_on="employee_id",
    )

    # Select required columns and sort by employee_id
    result = result[["employee_id", "name", "reports_count", "average_age"]]
    return result.sort_values("employee_id")