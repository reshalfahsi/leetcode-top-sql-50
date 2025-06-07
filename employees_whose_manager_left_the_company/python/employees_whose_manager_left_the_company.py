import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get the set of all current employee_ids
    current_employee_ids = set(employees["employee_id"])

    # Step 2: Filter employees whose salary is strictly less than $30000
    low_salary_employees_df = employees[employees["salary"] < 30000].copy()

    # Step 3: Identify managers who left the company
    # A manager left if their manager_id is not null AND
    # their manager_id is NOT in the set of current_employee_ids
    manager_left_condition = (
        low_salary_employees_df["manager_id"].notna()
    ) & (  # Manager ID must not be null
        ~low_salary_employees_df["manager_id"].isin(current_employee_ids)
    )  # Manager ID not in current employees

    # Step 4: Apply the conditions to get the final employees
    result_employees_df = low_salary_employees_df[manager_left_condition]

    # Step 5: Select only 'employee_id' and order by it
    return (
        result_employees_df[["employee_id"]]
        .sort_values(by="employee_id")
        .reset_index(drop=True)
    )