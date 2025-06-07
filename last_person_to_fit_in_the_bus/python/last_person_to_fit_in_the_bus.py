import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # Calculate cumulative weight ordered by turn (CummulativeWeight CTE)
    queue = queue.sort_values("turn")
    queue["cummulative_weight"] = queue["weight"].cumsum()

    # Filter for cumulative weight <= 1000 and assign ranks (RankedWeight CTE)
    ranked_weight = queue[queue["cummulative_weight"] <= 1000][
        ["person_name", "cummulative_weight"]
    ].assign(
        rank=lambda x: x["cummulative_weight"].rank(method="first", ascending=False)
    )

    # Select person_name where rank = 1
    return ranked_weight[ranked_weight["rank"] == 1][["person_name"]]