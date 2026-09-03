-- Solution 1: Optimum Solution (Subquery Approach)
-- Safe for single-row tables (returns NULL instead of empty set)
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);


-- Solution 2: Alternative Approach (ORDER BY & OFFSET)
-- Safe version: Wrapped in an outer SELECT to handle single-row tables (returns NULL properly)
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY
) AS SecondHighestSalary;