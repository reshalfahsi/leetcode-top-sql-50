import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    # Step 1 & 2: Filter price changes on or before the target date
    prices_before_target = products[products['change_date'] <= '2019-08-16'].copy()

    # Step 3: Find the latest price for each product before/on the target date
    # Sort by product_id and change_date in descending order to get the latest price first
    prices_before_target = prices_before_target.sort_values(by=['product_id', 'change_date'], ascending=[True, False])

    # Drop duplicates, keeping the first occurrence (which is the latest change_date due to sorting)
    latest_prices = prices_before_target.drop_duplicates(subset=['product_id'], keep='first')

    # Select only the relevant columns for the merge
    latest_prices = latest_prices[['product_id', 'new_price']].rename(columns={'new_price': 'price'})

    # Step 4: Handle default prices for all products
    # Get a list of all unique product_ids from the original table
    all_product_ids = products[['product_id']].drop_duplicates()

    # Left merge all products with their latest prices.
    # Products without any price changes before or on the target date will have NaN for 'price'.
    final_prices = pd.merge(all_product_ids, latest_prices, on='product_id', how='left')

    # Fill NaN values with the default price of 10
    final_prices['price'] = final_prices['price'].fillna(10).astype(int)

    return final_prices