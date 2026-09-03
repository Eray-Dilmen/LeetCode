# [177. Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/)

## Problem Description
Find the $N^{\text{th}}$ highest distinct salary from the `Employee` table. If there are fewer than $N$ distinct salaries, return `null`.

## Intuition
To find the $N^{\text{th}}$ highest distinct salary, we need to extract unique salary values from the table, sort them in descending order, and iterate through them using a counter until we reach the $N^{\text{th}}$ position.

## Approach
1. Use `SELECT DISTINCT salary` to eliminate duplicate values and order the results in descending order (`ORDER BY salary DESC`).
2. Iterate over the sorted query result set using a PL/SQL `FOR` loop cursor.
3. Maintain a counter variable `c` initialized to `0`. Increment `c` by `1` for each iteration.
4. When `c` matches `N`, immediately return `rec.salary`.
5. If the loop completes without reaching `N` (i.e., there are fewer than $N$ distinct salaries), return `NULL`.

## Complexity
- **Time complexity:** $\mathcal{O}(K \log K)$ where $K$ is the number of distinct salaries due to the sorting operation (`ORDER BY salary DESC`).
- **Space complexity:** $\mathcal{O}(K)$ for storing the sorted distinct salary records in memory during cursor execution.

## Solution Code

```sql
CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
c NUMBER := 0;
BEGIN
    FOR rec IN (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC)
    LOOP
        c := c + 1;
        IF c = N THEN
            RETURN rec.salary;
        END IF;
    END LOOP;

    RETURN NULL;
END;
```