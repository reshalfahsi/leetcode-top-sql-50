import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter for odd id and non-boring description
    filtered = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    
    # Select columns and sort by rating in descending order
    result = filtered[['id', 'movie', 'description', 'rating']].sort_values(by='rating', ascending=False)
    
    return result