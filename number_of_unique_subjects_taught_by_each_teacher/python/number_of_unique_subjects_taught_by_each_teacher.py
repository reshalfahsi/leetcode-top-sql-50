import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (
        teacher[['teacher_id', 'subject_id']] # Select relevant columns
        .drop_duplicates() # Remove duplicate teacher_id, subject_id pairs
        .groupby('teacher_id') # Group by teacher_id
        .size() # Count occurrences
        .reset_index(name='cnt') # Name the count column as 'cnt'
    )