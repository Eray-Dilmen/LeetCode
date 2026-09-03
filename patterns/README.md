# Algorithmic Patterns

This directory aims to solve problems encountered in LeetCode and technical interviews by classifying them into specific design patterns rather than relying on memorization.

---

## Why a Pattern-Based Approach?

* **Easy Recognition:** When faced with a new problem, identifying key clues allows you to quickly determine which pattern to apply (e.g., *Two Pointers* or *Sliding Window*).

* **Complexity Optimization:** It standardizes the transition steps from a Brute Force solution (e.g., `O(n²)`) to an optimal result (e.g., `O(n)` or `O(log n)`) by using the most suitable data structure or algorithmic pattern.

---

## Pattern List

| # | Pattern Name | Description |
|---|---|---|
| **01** | [01-hash-maps-and-sets](./01-hash-maps-and-sets/) | $O(1)$ frequency tracking, existence checking, and fast lookups |
| **02** | [02-two-pointers](./02-two-pointers/) | Bi-directional or same-direction traversal in sorted arrays |
| **03** | [03-sliding-window](./03-sliding-window/) | Dynamic or fixed windowing in subarray/substring problems |
| **04** | [04-prefix-sum](./04-prefix-sum/) | Calculating range sums and cumulative queries in $O(1)$ time |
| **05** | [05-fast-and-slow-pointers](./05-fast-and-slow-pointers/) | Linked list traversal and cycle detection (Floyd's Cycle Algorithm) |
| **06** | [06-binary-search](./06-binary-search/) | $O(\log n)$ search and optimization intervals in sorted spaces |
| **07** | [07-monotonic-stack](./07-monotonic-stack/) | Finding the next/previous greater/smaller elements |
| **08** | [08-intervals](./08-intervals/) | Merging and inserting overlapping intervals |
| **09** | [09-tree-dfs](./09-tree-dfs/) | Depth-first recursive traversal in trees |
| **10** | [10-tree-bfs](./10-tree-bfs/) | Level-order traversal in trees |
| **11** | [11-graphs-and-topological-sort](./11-graphs-and-topological-sort/) | Graph traversal, cycle detection, and dependency sorting |
| **12** | [12-heap-and-top-k-elements](./12-heap-and-top-k-elements/) | Finding the top/bottom $k$ elements using priority queues |
| **13** | [13-backtracking](./13-backtracking/) | Permutations, combinations, and state-space tree traversal |
| **14** | [14-dynamic-programming](./14-dynamic-programming/) | Subproblem optimization and state transitions (Memoization/Tabulation) |
| **15** | [15-greedy-algorithms](./15-greedy-algorithms/) | Reaching a global optimum through local optimum choices |
| **16** | [16-trie](./16-trie/) | Prefix-based text and dictionary searches |
| **17** | [17-bit-manipulation](./17-bit-manipulation/) | Bit-level operations and optimizations |

---

## Standard Pattern Structure

Each pattern directory contains two fundamental components:
1. **`README.md`:** The core logic of the pattern, when to use it, and template code approaches.
2. **Problem Folders (e.g., `0771-Jewels and Stones/`):** The problem description, Brute Force approach, Optimal approach, and complexity analysis.