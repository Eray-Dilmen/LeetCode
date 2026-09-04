> 📌 **Guide:** This directory serves as a Concept Map for the **Graphs & Topological Sort** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0200-Number of Islands`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Graphs & Topological Sort Pattern?

* **Definition:** A Graph is a data structure consisting of **Vertices (nodes)** and **Edges (connections)**. It can be directed (one-way) or undirected (two-way). Topological Sort is a specialized algorithm used exclusively on Directed Acyclic Graphs (DAGs) to linearly order nodes so that for every directed edge `u -> v`, node `u` comes before `v`.
* **The Core Superpower:** Graphs model complex, non-linear relationships like social networks, city maps, and network routing. Topological Sort specifically resolves **dependency chains** (e.g., prerequisite courses, task scheduling) in `O(V + E)` time (Vertices + Edges), making it the ultimate tool for ordering dependent events.

---

## Core Variations & Algorithmic Strategies

Graph problems usually fall into traversal (exploring the network) or ordering (resolving dependencies). 

### 1. Matrix / Grid Traversal (Implicit Graphs)
* **Algorithm:** A 2D grid is implicitly a graph where each cell is a node and its 4 directions (up, down, left, right) are edges. Use DFS (Recursion) or BFS (Queue) to explore connected components. **Crucial step:** You must mark visited cells (e.g., change `1` to `0` or use a `visited` set) to prevent infinite loops.
* **When to use it:** Finding islands, calculating areas of connected regions, or navigating mazes.
* **Repository Examples:**
  * [0200-Number of Islands](./0200-Number%20of%20Islands)
  * [0695-Max Area of Island](./0695-Max%20Area%20of%20Island)

### 2. Standard Graph DFS/BFS (Explicit Graphs)
* **Algorithm:** The graph is given as an Adjacency List (a dictionary mapping a node to a list of its neighbors) or an Edge List. You build the Adjacency List first. Then, use a `visited` set and perform DFS or BFS to explore paths, clone the graph, or find the shortest path in unweighted networks.
* **When to use it:** When mapping network connections, finding mutual friends, or copying a graph structure.
* **Repository Examples:**
  * [0133-Clone Graph](./0133-Clone%20Graph)
  * [0323-Number of Connected Components in an Undirected Graph](./0323-Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph)

### 3. Topological Sort (Kahn's Algorithm / BFS approach)
* **Algorithm:** First, calculate the `in-degree` (number of incoming edges) for every node. Push all nodes with an `in-degree` of 0 (no prerequisites) into a Queue. While the Queue is not empty, pop a node, append it to your topological order result, and decrement the `in-degree` of all its neighbors by 1. If a neighbor's `in-degree` drops to 0, push it into the Queue.
* **When to use it:** When scheduling tasks with prerequisites, determining build orders, or compiling code dependencies.
* **Repository Examples:**
  * [0207-Course Schedule](./0207-Course%20Schedule)
  * [0210-Course Schedule II](./0210-Course%20Schedule%20II)

### 4. Cycle Detection in Directed Graphs
* **Algorithm:** If a directed graph has a cycle (a loop), a valid Topological Sort is impossible. Using Kahn's Algorithm, if the final topological order array's length is *less* than the total number of nodes, it means the remaining nodes are stuck in a cycle (their in-degrees never reached 0).
* **When to use it:** Verifying if it is even possible to finish a set of tasks, or detecting circular dependencies in software modules.
* **Repository Examples:**
  * [0207-Course Schedule](./0207-Course%20Schedule) (often used purely for cycle detection)

---

## 💡 Professional Details & Edge Cases

* **The Disconnected Graph Trap:** A graph is not always a single connected web; it can have isolated islands. Always use an outer loop that iterates through *all* nodes in the input. If a node is `not in visited`, only then launch your DFS/BFS from it.
* **Adjacency List vs. Matrix:** Professionally, always convert an Edge List (e.g., `[[0, 1], [1, 2]]`) into an Adjacency List (dictionary of lists) before running traversals. Iterating over an Adjacency List is $O(V + E)$, whereas searching an Edge List repeatedly can degrade to $O(V \times E)$.
* **DFS Topological Sort (Alternative):** Topo Sort can also be done using a recursive DFS with 3 states (0 = unvisited, 1 = visiting, 2 = visited). You detect cycles if you encounter a node in state `1`. If successful, you push the node to a stack *after* visiting all its neighbors, and reverse the stack at the end. Kahn's (BFS) is generally easier to implement and reason about.