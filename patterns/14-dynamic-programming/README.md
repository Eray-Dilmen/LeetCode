> 📌 **Guide:** This directory serves as a Concept Map for the **Dynamic Programming (DP)** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0070-Climbing Stairs`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Dynamic Programming Pattern?

* **Definition:** An algorithmic optimization technique that solves complex problems by breaking them down into simpler, **overlapping subproblems**. It relies on two main properties: Overlapping Subproblems (the same subproblem is solved multiple times) and Optimal Substructure (the optimal solution to the main problem is built from the optimal solutions of its subproblems).
* **The Core Superpower:** DP trades memory for speed. Instead of recalculating the same states repeatedly (which causes exponential `O(2^n)` time complexity in naive recursion), DP "caches" or "memorizes" the results of these subproblems. This reduces the time complexity drastically to `O(n)` or `O(n²)`.

---

## Core Variations & Algorithmic Strategies

Dynamic Programming has two primary implementation methods (Top-Down and Bottom-Up) and varying dimensions based on the problem's states.

### 1. Top-Down (Memoization)
* **Algorithm:** Start from the main problem (the "top") and use recursion to break it down. Before computing a state, check if it already exists in a cache (usually a Hash Map or an array). If it does, return the cached value. If not, compute it, store it in the cache, and then return it.
* **When to use it:** When the problem naturally feels like a recursive tree (like Backtracking), but you notice that the same parameters are being passed to the recursive function multiple times.
* **Repository Examples:**
  * [0322-Coin Change](./0322-Coin%20Change)

### 2. Bottom-Up (Tabulation)
* **Algorithm:** Avoid recursion entirely. Start from the absolute smallest subproblems (the base cases) and build up to the final answer using an iterative `for` loop and a `dp` array. The answer to `dp[i]` is computed using the previously calculated values like `dp[i - 1]` or `dp[i - 2]`.
* **When to use it:** When you know the exact order in which subproblems must be solved, and you want to avoid the memory overhead of the recursive call stack.
* **Repository Examples:**
  * [0070-Climbing Stairs](./0070-Climbing%20Stairs)
  * [0198-House Robber](./0198-House%20Robber)

### 3. 2D Dynamic Programming (Grids & Strings)
* **Algorithm:** The state depends on two variables instead of one. You use a 2D matrix (like `dp[r][c]`) to cache results. The value of a cell usually depends on the cell above it, the cell to its left, or its diagonal.
* **When to use it:** Matrix traversal where you can only move right/down, or comparing two different strings (like Longest Common Subsequence or Edit Distance).
* **Repository Examples:**
  * [0062-Unique Paths](./0062-Unique%20Paths)
  * [1143-Longest Common Subsequence](./1143-Longest%20Common%20Subsequence)

---

## 💡 Professional Details & Edge Cases

* **State and Recurrence Relation:** The hardest part of DP is defining the "State" (what does `dp[i]` represent?) and the "Recurrence Relation" (how does `dp[i]` relate to `dp[i-1]`). Before writing any code, write the mathematical equation on paper (e.g., `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`).
* **Space Optimization:** In Bottom-Up 1D DP, if `dp[i]` only depends on the previous two states (`dp[i-1]` and `dp[i-2]`), you **do not need an entire `O(n)` array**. You can just use two variables to track the previous two values, dropping the space complexity from `O(n)` to strictly `O(1)`. This is a massive professional advantage in interviews.
* **Initialization (Base Cases):** A DP algorithm is only as good as its base cases. Always initialize `dp[0]` (and sometimes `dp[1]`) carefully. For minimum problems, initialize the array with `infinity` (`float('inf')`). For maximum/counting problems, initialize with `0`.