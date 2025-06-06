import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    # Select the first row for each customer_id based on order_date
    first_orders = delivery.sort_values(['customer_id', 'order_date']).drop_duplicates('customer_id', keep='first')
    
    # Calculate the number of rows where order_date equals customer_pref_delivery_date
    immediate_count = first_orders[first_orders['order_date'] == first_orders['customer_pref_delivery_date']].shape[0]
    
    # Calculate total number of rows
    total_count = first_orders.shape[0]
    
    # Calculate percentage and round to 2 decimal places
    immediate_percentage = round((immediate_count * 100.0 / total_count), 2) if total_count > 0 else 0.0
    
    # Return as a DataFrame for consistency with SQL output
    return pd.DataFrame({'immediate_percentage': [immediate_percentage]})