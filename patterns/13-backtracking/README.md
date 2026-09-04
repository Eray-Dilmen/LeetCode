> 📌 **Guide:** This directory serves as a Concept Map for the **Backtracking** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0078-Subsets`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Backtracking Pattern?

* **Definition:** An algorithmic technique for solving recursive problems by trying to build a solution incrementally, one piece at a time. If a partial solution violates the problem's constraints, it abandons that path (backtracks) and tries the next available option. 
* **The Core Superpower:** It explores all possible configurations, but intelligently optimizes a pure brute-force approach by **pruning** (abandoning) invalid branches of the decision tree early. Time complexity is typically exponential `O(2^n)` or factorial `O(n!)` because the output space itself is that large. Space complexity is usually `O(n)` representing the maximum depth of the recursion stack.

---

## Core Variations & Algorithmic Strategies

Backtracking algorithms are generally structured with a `backtrack(start_index, current_path)` helper function. The variations depend on how you iterate and select the next elements.

### 1. Subsets & Combinations (Order Does Not Matter)
* **Algorithm:** You want to generate groupings where `[1, 2]` is the same as `[2, 1]`. To prevent duplicate groupings, use a `start_index` in your `for` loop. The recursive call will pass `i + 1` as the new start index, ensuring you only look strictly forward in the array and never backwards.
* **When to use it:** Finding all subsets of a set, or combinations of `k` numbers.
* **Repository Examples:**
  * [0078-Subsets](./0078-Subsets)
  * [0077-Combinations](./0077-Combinations)

### 2. Permutations (Order Matters)
* **Algorithm:** You want to generate arrangements where `[1, 2]` is distinct from `[2, 1]`. Do **not** use a `start_index`. Instead, your `for` loop always starts from `0` to `n`. To prevent reusing the exact same element in the same path, you must check `if nums[i] in current_path` (or use a `visited` boolean array/set) and skip it.
* **When to use it:** Generating all possible passwords, arrangements, or orderings of a dataset.
* **Repository Examples:**
  * [0046-Permutations](./0046-Permutations)
  * [0047-Permutations II](./0047-Permutations%20II)

### 3. Constraint Satisfaction & Pruning
* **Algorithm:** Similar to Subsets/Combinations, but with an explicit target or constraint. Before diving deeper into the recursion, check if the current state exceeds the target. If it does, `return` immediately (pruning the tree). If you can reuse the same element multiple times, pass `i` instead of `i + 1` into the recursive call.
* **When to use it:** Coin change problems, combination sums, or placing queens on a chessboard (N-Queens).
* **Repository Examples:**
  * [0039-Combination Sum](./0039-Combination%20Sum)
  * [0051-N-Queens](./0051-N-Queens)

### 4. Grid DFS with Backtracking
* **Algorithm:** Navigating a 2D matrix where you are looking for a specific path (like a word). You use DFS to explore directions. The key backtracking step: you must mark the current cell as "visited" (e.g., changing its character to `#`) *before* the recursive calls, and then **unmark** it (change it back to the original character) *after* the recursive calls return. This allows the cell to be visited again by a different path.
* **When to use it:** Word Search, maze solving with multiple possible paths.
* **Repository Examples:**
  * [0079-Word Search](./0079-Word%20Search)

---

## 💡 Professional Details & Edge Cases

* **The Deep Copy Bug:** The most common backtracking bug is appending the `current_path` directly to the `results` array (`results.append(path)`). Because lists are passed by reference, when the recursion backtracks and pops elements from `path`, it will also erase them from the `results` array. **Always append a deep copy:** `results.append(path[:])` in Python or `new ArrayList<>(path)` in Java.
* **Handling Duplicates (Sorting & Skipping):** If the input array contains duplicate numbers and you want unique subsets/combinations, you must first sort the array (`nums.sort()`). Then, inside your `for` loop, add a check: `if i > start_index and nums[i] == nums[i-1]: continue`. This strictly skips processing the same number at the same depth level of the recursive tree.
* **Accepting `O(2^n)`:** Do not be afraid of exponential time complexity in backtracking problems. If a problem asks you to "return all possible combinations", the mathematical number of combinations is `2^n`. The `O(2^n)` algorithm is the absolute optimal solution.