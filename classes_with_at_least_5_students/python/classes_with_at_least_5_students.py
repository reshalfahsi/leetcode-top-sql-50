import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses.groupby("class")  # Group by class
        .size()  # Count occurrences of each class
        .reset_index(name="class_count")  # Name the count column as 'class_count'
        .query("class_count >= 5")[["class"]]  # Filter for classes with count >= 5
    )  # Select only the class column