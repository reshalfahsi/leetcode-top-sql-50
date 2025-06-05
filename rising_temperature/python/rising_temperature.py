import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Ensure recordDate is in datetime format
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    # Sort by recordDate to ensure correct ordering
    weather = weather.sort_values('recordDate')
    
    # Create columns for previous temperature and previous date
    weather['prev_temperature'] = weather['temperature'].shift(1)
    weather['prev_recordDate'] = weather['recordDate'].shift(1)
    
    # Calculate the date difference in days
    weather['date_diff'] = (weather['recordDate'] - weather['prev_recordDate']).dt.days
    
    # Filter rows where temperature is higher than previous and dates differ by 1 day
    result = weather[
        (weather['temperature'] > weather['prev_temperature']) & 
        (weather['date_diff'] == 1)
    ][['id']]
    
    return result