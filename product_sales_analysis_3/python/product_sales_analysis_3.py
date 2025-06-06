import pandas as pd


def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Create ProductFirstYear equivalent by finding the minimum year per product

    product_first_year = (
        sales.groupby("product_id")["year"].min().reset_index(name="first_year")
    )

    # Step 2: Merge with original Sales DataFrame to get sales details for the first year

    result = sales.merge(product_first_year, on=["product_id"], how="inner").query(
        "year == first_year"
    )[["product_id", "first_year", "quantity", "price"]]
    return result