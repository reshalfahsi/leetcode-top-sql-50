import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    flip = lambda x: x - (1 - 2 * (x % 2)) * (x <= len(seat) // 2 * 2)
    seat["id"] = seat["id"].apply(flip)
    return seat.sort_values("id")