import pandas as pd

def top_three_salaries(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    # Merge Employee and Department DataFrames
    merged_df = pd.merge(
        employee, department, left_on="departmentId", right_on="id", how="inner"
    )[["name_y", "name_x", "salary"]].rename(
        columns={
            "name_y": "department_name",
            "name_x": "employee_name",
            "salary": "salary",
        }
    )

    # Calculate dense rank within each department based on salary (descending)
    merged_df["salary_rank"] = merged_df.groupby("department_name")["salary"].rank(
        method="dense", ascending=False
    )

    # Filter for top 3 ranks
    return merged_df[merged_df["salary_rank"] <= 3][
        ["department_name", "employee_name", "salary"]
    ].rename(
        columns={
            "department_name": "Department",
            "employee_name": "Employee",
            "salary": "Salary",
        }
    )