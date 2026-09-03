# Python (Pandas) Solution
# The rank(method='dense') parameter works with the exact same logic as DENSE_RANK() in SQL.
import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate the rank column (from highest to lowest using the dense method)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    # Select the required columns and sort them in descending order by score
    result = scores[['score', 'rank']].sort_values(by='score', ascending=False)

    return result