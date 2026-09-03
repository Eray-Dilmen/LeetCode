# [175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

## Problem Description
Write a solution to report the first name, last name, city, and state of each person in the `Person` table. If the address of a `personId` is not present in the `Address` table, report `null` instead.

## Intuition
We need to combine information from two separate tables (`Person` and `Address`) based on a common field, `personId`. Since we must report all records from the `Person` table regardless of whether they have a corresponding entry in the `Address` table, a `LEFT JOIN` is required.

## Approach
1. Select the required columns: `firstName`, `lastName`, `city`, and `state`.
2. Perform a `LEFT JOIN` starting from the `Person` table (`Person p LEFT JOIN Address a`).
3. Match records using the join condition `p.personId = a.personId`.
4. This ensures all individuals in `Person` are included, and missing address data (`city`, `state`) will automatically default to `null`.

## Complexity
- **Time complexity:** $\mathcal{O}(N + M)$ where $N$ is the number of rows in `Person` and $M$ is the number of rows in `Address`.
- **Space complexity:** $\mathcal{O}(1)$ as no additional memory structures are allocated beyond the query execution result set.

## Solution Code

```sql
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;
```