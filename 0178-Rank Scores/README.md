# [178. Rank Scores](https://leetcode.com/problems/rank-scores/)

## Problem Description
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

- The scores should be ranked from the highest to the lowest.
- If there is a tie between two scores, both should have the same ranking.
- After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by `score` in descending order.

# Intuition
To rank scores from highest to lowest without skipping numbers after ties, we need a ranking method that handles duplicates by assigning them the same rank and continues with the next consecutive integer.

# Approach 1: SQL (DENSE_RANK) - Optimal Solution
The standard SQL window function `DENSE_RANK()` is designed specifically for this behavior:
- Unlike `RANK()`, which leaves gaps after tied values (e.g., 1, 2, 2, 4), `DENSE_RANK()` assigns consecutive integers without gaps (e.g., 1, 2, 2, 3).
- Using `OVER (ORDER BY score DESC)` sorts the dataset in descending order and assigns ranks dynamically in a declarative manner.

# Complexity
- **Time complexity:** $\mathcal{O}(N \log N)$
  Sorting the scores dominates the time complexity. The window function calculates ranks in a single pass after sorting.
- **Space complexity:** $\mathcal{O}(N)$
  Space is required by the database engine to store the intermediate sorted dataset and the resulting window function values.


# Code
```sql
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;
```

---

# Approach 2: Python (Pandas)
In Pandas, we achieve the same behavior using the `.rank()` method with `method='dense'` and `ascending=False`. We then sort the DataFrame by `score` in descending order.

# Complexity
- **Time complexity:** $\mathcal{O}(N \log N)$
  Both `.rank()` and `.sort_values()` use sorting algorithms under the hood, which take $\mathcal{O}(N \log N)$ time.
- **Space complexity:** $\mathcal{O}(N)$
  Pandas allocates memory for new Series and DataFrame objects to store the computed ranks and the final sorted output.

# Code
```python
# Python (Pandas) Solution
# The rank(method='dense') parameter works with the exact same logic as DENSE_RANK() in SQL.
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Calculate the rank column (from highest to lowest using the dense method)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Select the required columns and sort them in descending order by score
    result = scores[['score', 'rank']].sort_values(by='score', ascending=False)
    
    return result
```
---

# Approach 3: PL/SQL (Procedural Approach)
While this problem can be approached procedurally in PL/SQL by iterating over rows using a cursor and manually incrementing a counter when a new score is encountered, **pure SQL is preferred over PL/SQL**:
1. **Declarative vs. Procedural:** SQL specifies *what* to fetch, allowing the database engine to optimize execution internally, whereas PL/SQL explicitly dictates *how* to iterate.
2. **Performance:** PL/SQL loops process rows sequentially, introducing context switches and higher memory overhead, whereas `DENSE_RANK()` executes natively at the database engine level.
3. **Simplicity:** SQL solves the task concisely in a single query without requiring procedural blocks or cursor management.

# Complexity
- **Time complexity:** $\mathcal{O}(N \log N)$
  The dataset must still be sorted before iteration (`ORDER BY score DESC`), which takes $\mathcal{O}(N \log N)$. The subsequent procedural iteration adds $\mathcal{O}(N)$ time. However, sorting remains the dominant asymptotic factor, even though the constant time overhead is significantly higher due to engine context switching.
- **Space complexity:** $\mathcal{O}(N)$
  Memory is consumed for cursor row management, procedural variable storage, and output buffering.

# Code
```plsql
/* Write your PL/SQL query statement below */
CREATE OR REPLACE FUNCTION get_ranked_scores
RETURN SYS_REFCURSOR IS
    c_result SYS_REFCURSOR;
BEGIN
    OPEN c_result FOR
        SELECT 
            score,
            DENSE_RANK() OVER (ORDER BY score DESC) AS rank
        FROM Scores;
    RETURN c_result;
END;
```

