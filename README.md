# Data Structures, Algorithms & LeetCode Solutions

A curated collection designed to build a strong foundation in computer science fundamentals and practical problem-solving for technical interviews. This repository combines theoretical algorithm analyses, pattern-based coding techniques, and optimized LeetCode solutions in Python and SQL.

> **Note:** Problem titles in each folder are hyperlinked directly to the corresponding LeetCode problem page.

---

## Repository Structure

The repository is organized into three main domains to separate theoretical concepts, algorithmic practice, and database queries:

* **`patterns/`**: Pattern-based practical problem solving (Data Structures & Algorithms).
* **`sql/`**: LeetCode SQL problem solutions and query optimizations.
* **`algorithms/`**: Theoretical foundations, mathematical analysis, and Big-O notation.

### Problem Folder Format
Regardless of the domain (DSA or SQL), each specific problem is stored in its own directory containing:
* `solution.sql` / `solution.py`: Clean and optimized code.
* `README.md`: Problem summary, step-by-step approach, and asymptotic complexity in English.
* `README.tr.md`: Turkish translation of the problem explanation, occasionally including personal study notes.

---

## 1. Algorithmic Patterns (`patterns/`)

Instead of memorizing individual LeetCode problems, this section categorizes them into 17 fundamental problem-solving patterns. For each problem, we first present the **Optimal** solution to immediately focus on the most efficient and cleanest approach. Afterward, we explore the **Brute Force** or alternative solutions to provide extra theoretical context and comparison.

**`patterns/`**  
├── [01-hash-maps-and-sets](patterns/01-hash-maps-and-sets)  
├── [02-two-pointers](patterns/02-two-pointers)  
├── [03-sliding-window](patterns/03-sliding-window)  
├── [04-prefix-sum](patterns/04-prefix-sum)  
├── [05-fast-and-slow-pointers](patterns/05-fast-and-slow-pointers)  
├── [06-binary-search](patterns/06-binary-search)  
├── [07-monotonic-stack](patterns/07-monotonic-stack)  
├── [08-intervals](patterns/08-intervals)  
├── [09-tree-dfs](patterns/09-tree-dfs)  
├── [10-tree-bfs](patterns/10-tree-bfs)  
├── [11-graphs-and-topological-sort](patterns/11-graphs-and-topological-sort)  
├── [12-heap-and-top-k-elements](patterns/12-heap-and-top-k-elements)  
├── [13-backtracking](patterns/13-backtracking)  
├── [14-dynamic-programming](patterns/14-dynamic-programming)  
├── [15-greedy-algorithms](patterns/15-greedy-algorithms)  
├── [16-trie](patterns/16-trie)  
└── [17-bit-manipulation](patterns/17-bit-manipulation)  

> Each pattern folder contains a core `README.md` explaining *when* and *why* to use the pattern, followed by the specific LeetCode problem folders that apply it.

---

## 2. Database & SQL (`sql/`)

A dedicated section for LeetCode database problems. This directory focuses on writing efficient and scalable queries using SQL. 

Topics covered include:
* Complex Joins & Subqueries
* Aggregations & Grouping
* Window Functions
* Query performance and execution logic

---

## 3. Core Algorithms & Complexity (`algorithms/`)

The theoretical and mathematical backbone of the repository. This section covers the fundamental rules of algorithmic analysis before writing any code.

* **Time & Space Complexity:** Asymptotic notations (Big O, Big $\Omega$, Big $\Theta$).
* **Analysis Techniques:** Calculating the cost of loops, consecutive operations, nested structures, and recursive relations.
* **Classic Algorithms:** Theoretical comparisons of foundational searching, sorting, and data manipulation algorithms.