import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:

    st = students.reindex(
        fill_value=0, columns=["student_id", "student_name", "attended_exams"]
    )

    sb = subjects.reindex(fill_value=0, columns=["subject_name", "attended_exams"])

    ex = examinations.reindex(
        fill_value=1, columns=["student_id", "subject_name", "attended_exams"]
    )
    df = st.merge(sb, on="attended_exams", how="outer")

    df = df.merge(ex, on=["student_id", "subject_name", "attended_exams"], how="outer")

    df = (
        df.groupby(["student_id", "subject_name"])
        .agg({"attended_exams": "sum", "student_name": "first"})
        .reset_index()
    )

    return df[["student_id", "student_name", "subject_name", "attended_exams"]]