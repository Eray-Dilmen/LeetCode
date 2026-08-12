# [182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

## Problem Description
Report all the duplicate emails from the table.

# Intuition
To identify duplicates, we need to count the occurrences of each unique email. If an email appears more than once in the table, it is considered a duplicate.

# Approach
1. Group the records by the `email` column using the `GROUP BY` clause.
2. Filter these grouped records using the `HAVING` clause.
3. Retain only the groups where the `COUNT(email)` is strictly greater than 1.
4. Select the `email` column and alias it as `Email` to match the required output format.

# Complexity
- **Time complexity:** $\mathcal{O}(N)$ where $N$ is the number of rows in the table. The database engine performs a single scan and aggregates the data using a hash map or sorting algorithm.
- **Space complexity:** $\mathcal{O}(U)$ where $U$ is the number of unique emails, which is the memory required to store the grouped results during execution.

# Code
```sql
/* Write your PL/SQL query statement below */
SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
```