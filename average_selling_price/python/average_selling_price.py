import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Merge UnitsSold with Prices on product_id
    # We use an outer join initially to get all combinations before applying date filter.
    # However, a more direct way for this problem is often to use an inner merge
    # and then filter, as we only care about units that *do* have a price.
    merged_df = pd.merge(units_sold, prices, on='product_id', how='left')

    # Step 2: Filter by date range
    # This is the equivalent of the `us.purchase_date BETWEEN p.start_date AND p.end_date` in SQL
    valid_sales = merged_df[
        (merged_df['purchase_date'] >= merged_df['start_date']) &
        (merged_df['purchase_date'] <= merged_df['end_date'])
    ]

    # Step 3: Calculate weighted revenue for valid sales
    valid_sales['total_revenue_per_sale'] = valid_sales['price'] * valid_sales['units']

    # Step 4: Group by product_id and aggregate sums
    # We sum both 'total_revenue_per_sale' and 'units'
    product_summary = valid_sales.groupby('product_id').agg(
        total_revenue=('total_revenue_per_sale', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()

    # Step 5: Calculate Average Price
    product_summary['average_price'] = product_summary['total_revenue'] / product_summary['total_units']

    # Step 6: Handle products with no sales
    # Get all unique product_ids from the original Prices table
    all_products = prices[['product_id']].drop_duplicates()

    # Left merge all products with the calculated summary.
    # This ensures products with no sales are included.
    final_result = pd.merge(all_products, product_summary, on='product_id', how='left')

    # Fill NaN average_price with 0 for products with no sales
    final_result['average_price'] = final_result['average_price'].fillna(0)

    # Step 7: Round the result
    final_result['average_price'] = final_result['average_price'].round(2)

    # Select and order final columns
    final_result = final_result[['product_id', 'average_price']]

    return final_result