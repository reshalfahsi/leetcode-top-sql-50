import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # Create the triangle condition using vectorized operations
    triangle['triangle'] = (
        ((triangle['x'] + triangle['y'] > triangle['z']) & 
        (triangle['x'] + triangle['z'] > triangle['y']) & 
        (triangle['z'] + triangle['y'] > triangle['x']))
        .map({True: 'Yes', False: 'No'})
    )

    # Select the required columns
    return triangle[['x', 'y', 'z', 'triangle']]