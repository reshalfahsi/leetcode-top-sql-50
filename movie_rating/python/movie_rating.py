import pandas as pd

mx = lambda x: (-x[0], x[1])

def movie_rating(
    movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame
) -> pd.DataFrame:

    df1 = movie_rating.merge(users).groupby(["name"], as_index=False)["rating"].count()

    df2 = (
        movie_rating.loc[movie_rating.created_at.dt.to_period("M") == "2020-02"]
        .merge(movies)
        .groupby("title")
        .mean()
        .reset_index()
    )

    _, mx_name = min(zip(df1.rating, df1.name), key=mx)
    _, mx_title = min(zip(df2.rating, df2.title), key=mx)

    return pd.DataFrame([mx_name, mx_title], columns=["results"])