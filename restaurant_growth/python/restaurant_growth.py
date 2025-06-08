import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.sort_values("visited_on").groupby("visited_on")[["amount"]].sum()
    df = df.assign(
        amount=df.rolling("7D").sum(),
        average_amount=round(df.rolling("7D").sum() / 7, 2),
    )
    return df.loc[df.index >= df.index.min() + pd.DateOffset(6)].reset_index()