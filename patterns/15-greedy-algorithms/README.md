> 📌 **Guide:** This directory serves as a Concept Map for the **Greedy Algorithms** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0055-Jump Game`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Greedy Algorithms Pattern?

* **Definition:** An algorithmic paradigm that builds a solution piece by piece, always choosing the next piece that offers the most immediate benefit. It makes a **locally optimal choice** at each step with the hope that these local choices will lead to a **globally optimal solution**.
* **The Core Superpower:** Extreme speed and memory efficiency. Instead of exhaustively exploring all possible paths (like Backtracking) or caching overlapping subproblems (like Dynamic Programming), a greedy algorithm simply picks the "best" current option and moves forward. It never looks back to reconsider previous choices. Time complexity is usually `O(n)` or `O(n log n)` (if sorting is required), with `O(1)` space complexity.

---

## Core Variations & Algorithmic Strategies

The main challenge in Greedy algorithms is not writing the code, but *proving* that a greedy choice actually works for the specific problem.

### 1. Sorting + Greedy Choice
* **Algorithm:** The raw data is chaotic, making it impossible to know what the "best" choice is. You first sort the input array based on a specific metric (e.g., sizes, start times, or ratios). Once sorted, you iterate through the array and greedily satisfy conditions one by one until you run out of resources.
* **When to use it:** Resource allocation, scheduling, or pairing problems (like matching the smallest cookies to the least greedy children).
* **Repository Examples:**
  * [0455-Assign Cookies](./0455-Assign%20Cookies)
  * [0406-Queue Reconstruction by Height](./0406-Queue%20Reconstruction%20by%20Height)

### 2. Maximum Reach / Jumps
* **Algorithm:** You iterate through an array and continuously update the "farthest possible reach" or "maximum capacity" you can achieve from your current position. If your current index exceeds your maximum reach, you are stuck. If your reach exceeds the last index, you win.
* **When to use it:** Array traversal problems where elements represent jump lengths or fuel.
* **Repository Examples:**
  * [0055-Jump Game](./0055-Jump%20Game)
  * [0045-Jump Game II](./0045-Jump%20Game%20II)

### 3. Greedy Accumulation (Running Totals)
* **Algorithm:** You maintain a running balance (e.g., fuel in a tank). As you iterate, you add to the balance. If the balance drops below zero, it means the current path is completely invalid. You greedily reset your starting position to the *next* index and reset your balance to zero, knowing that any index before it would have also failed.
* **When to use it:** Circular route problems, or finding valid starting points in a sequence.
* **Repository Examples:**
  * [0134-Gas Station](./0134-Gas%20Station)
  * [0763-Partition Labels](./0763-Partition%20Labels)

---

## 💡 Professional Details & Edge Cases

* **Greedy vs. Dynamic Programming:** This is the most common trap. A greedy algorithm only works if the problem has the **Greedy Choice Property** (a global optimum can be arrived at by selecting a local optimum). For example, finding the minimum coins for `$0.30` using `[25, 10, 1]` coins:
  * Greedy picks `25`, then needs five `1`s -> total 6 coins.
  * DP explores all paths and finds three `10`s -> total 3 coins (Global Optimum).
  * Always verify if taking the immediate largest/best option might block a mathematically better combination later. If it does, you must use DP.
* **The Sorting Bottleneck:** While the greedy traversal itself is often $O(n)$, the prerequisite sorting step takes $O(n \log n)$. Therefore, the overall time complexity is fundamentally bound by the sorting algorithm.
* **No Backtracking:** A true greedy algorithm evaluates the current state, makes a definitive choice, and advances. If you find yourself writing logic to "undo" a choice and try another path, you are writing a Backtracking algorithm, not a Greedy one.