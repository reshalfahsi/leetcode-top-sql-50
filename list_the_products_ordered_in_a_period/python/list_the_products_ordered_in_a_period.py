import pandas as pd

mnth = pd.to_datetime("2020-02").to_period("M")

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = (
        orders[orders["order_date"].dt.to_period("M") == mnth]
        .merge(products[["product_id", "product_name"]], on="product_id")
        .reset_index()[["product_name", "unit"]]
        .groupby(["product_name"], as_index=False)["unit"]
        .sum()
    )
    return orders[orders["unit"] >= 100]