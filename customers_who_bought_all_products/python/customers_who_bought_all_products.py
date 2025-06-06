import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Get total number of distinct products
    total_products = product["product_key"].nunique()

    # Step 2: Count distinct products per customer
    customer_product_counts = (
        customer.groupby("customer_id")["product_key"]
        .nunique()
        .reset_index(name="product_count")
    )

    # Step 3: Calculate if customer bought all products (product_count == total_products)
    customer_product_counts["is_all_bought"] = (
        customer_product_counts["product_count"] / total_products
    )

    # Step 4: Filter for customers where is_all_bought == 1 and select customer_id
    return customer_product_counts[customer_product_counts["is_all_bought"] == 1][
        ["customer_id"]
    ]