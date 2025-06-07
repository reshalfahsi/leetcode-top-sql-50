import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee["x"] = employee.groupby("employee_id")["employee_id"].transform("count")
    df = employee[
        ((employee["x"] == 1) & (employee["primary_flag"] == "N"))
        | ((employee["x"] > 1) & (employee["primary_flag"] == "Y"))
    ]
    return df[["employee_id", "department_id"]]