import pandas as pd
from itertools import chain
from collections import Counter

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    ctr = Counter(
        chain(
            request_accepted.requester_id.to_list(),
            request_accepted.accepter_id.to_list(),
        )
    )
    mx = max(ctr, key=lambda x: ctr[x])
    return pd.DataFrame({"id": [mx], "num": [ctr[mx]]})