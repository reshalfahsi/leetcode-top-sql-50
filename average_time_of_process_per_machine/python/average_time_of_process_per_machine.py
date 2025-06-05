import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table to get start and end timestamps as columns
    pivoted = activity.pivot(index=['machine_id', 'process_id'], 
                           columns='activity_type', 
                           values='timestamp').reset_index()
    
    # Calculate processing time (end - start) for each process
    pivoted['processing_time'] = pivoted['end'] - pivoted['start']
    
    # Group by machine_id and compute the average processing time
    result = pivoted.groupby('machine_id')['processing_time'].mean().reset_index()
    
    # Round to 3 decimal places
    result['processing_time'] = result['processing_time'].round(3)
    
    return result