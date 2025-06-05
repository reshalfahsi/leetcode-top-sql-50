import pandas as pd


def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions["month"] = pd.to_datetime(transactions["trans_date"]).dt.strftime(
        "%Y-%m"
    )
    transactions["state"] = (
        transactions["state"].str.replace("approved", "1").replace("declined", "0")
    )
    transactions["state"] = transactions["state"].astype(int)
    transactions["approved_total_amount"] = (
        transactions["amount"] * transactions["state"]
    )
    resq = (
        transactions.groupby(["month", "country"], dropna=False)
        .agg(
            {
                "id": "count",
                "state": "sum",
                "amount": "sum",
                "approved_total_amount": "sum",
            }
        )
        .reset_index()
    )
    return resq.rename(
        columns={
            "id": "trans_count",
            "state": "approved_count",
            "amount": "trans_total_amount",
        }
    )