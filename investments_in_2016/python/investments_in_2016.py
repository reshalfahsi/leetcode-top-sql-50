import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    dup = insurance[insurance.duplicated(subset="tiv_2015", keep=False)].pid
    pos = insurance.drop_duplicates(subset=["lat", "lon"], keep=False).pid
    return pd.DataFrame(
        {
            "tiv_2016": [
                insurance[
                    insurance.pid.isin(pos) & (insurance.pid.isin(dup))
                ].tiv_2016.sum()
            ]
        }
    )