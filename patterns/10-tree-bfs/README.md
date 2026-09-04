> 📌 **Guide:** This directory serves as a Concept Map for the **Tree Breadth-First Search (BFS)** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0102-Binary Tree Level Order Traversal`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Tree BFS Pattern?

* **Definition:** An algorithmic technique for traversing a tree data structure level by level. It visits the `root`, then all of the root's direct children (level 1), then all of their children (level 2), moving from left to right. It is implemented iteratively using a **Queue** (First-In, First-Out / FIFO).
* **The Core Superpower:** BFS is the ultimate tool for processing nodes in horizontal batches and finding the **shortest path** to a target. Because it explores uniformly outward, the first time it reaches a target, it is mathematically guaranteed to be the shortest path. Time complexity is **$O(n)$**, and space complexity is **$O(w)$** (where $w$ is the maximum width of the tree, which can be up to $O(n/2)$ for the leaf level of a balanced tree).

---

## Core Variations & Algorithmic Strategies

The way you structure the `while` loop determines how the BFS processes the tree.

### 1. Standard Level-by-Level Traversal
* **Algorithm:** Initialize a queue with the `root`. Use an outer `while queue:` loop. Inside, take a snapshot of the current queue length (`level_size = len(queue)`). Use an inner `for i in range(level_size):` loop to pop exactly that many nodes. This guarantees you are only processing nodes from the current level before moving to their children.
* **When to use it:** When you need to group node values by their depth level, or when finding the rightmost/leftmost node of every level (Right Side View).
* **Repository Examples:**
  * [0102-Binary Tree Level Order Traversal](./0102-Binary%20Tree%20Level%20Order%20Traversal)
  * [0199-Binary Tree Right Side View](./0199-Binary%20Tree%20Right%20Side%20View)

### 2. Early Exit (Shortest Path / Minimum Depth)
* **Algorithm:** Use the standard level-by-level approach, but maintain a `depth` counter. As soon as you pop a node that satisfies the target condition (e.g., it is a leaf node with `not node.left and not node.right`), immediately return the `depth`.
* **When to use it:** Finding the minimum depth of a tree or the shortest path to a specific node. BFS is infinitely more efficient than DFS here, because DFS might waste time exploring a massive 10,000-node deep branch when the target was actually just 2 steps down on a different branch.
* **Repository Examples:**
  * [0111-Minimum Depth of Binary Tree](./0111-Minimum%20Depth%20Binary%20Tree)

### 3. Level Aggregation & Metrics
* **Algorithm:** Similar to the level-by-level traversal. Instead of just appending node values to a list, you maintain running variables (like `level_sum`, `level_max`) inside the outer `while` loop, update them in the inner `for` loop, and append the aggregated result before moving to the next level.
* **When to use it:** Calculating averages, maximums, or sums for each specific depth level of the tree.
* **Repository Examples:**
  * [0637-Average of Levels in Binary Tree](./0637-Average%20of%20Levels%20in%20Binary%20Tree)
  * [0515-Find Largest Value in Each Tree Row](./0515-Find%20Largest%20Value%20in%20Each%20Tree%20Row)

---

## 💡 Professional Details & Edge Cases

* **The `deque` Rule:** In Python, **never** use a standard list (`[]`) as a queue if you are using `pop(0)`. A standard list shifts all elements in memory when the first element is removed, resulting in an $O(n)$ operation and severely slowing down your BFS. Always import `collections.deque` and use `popleft()`, which strictly operates in $O(1)$ time.
* **Null Node Handling:** Do not push `None` values into the queue. The standard practice is to explicitly check children before enqueueing: `if node.left: queue.append(node.left)`. This keeps the queue clean and prevents `NoneType` errors inside the processing loop.
* **Inner Loop Snapshot:** A common beginner bug is iterating over the queue dynamically without taking a snapshot of its length. If you use a `while` loop for the inner level processing instead of a `for` loop bound by the initial `len(queue)`, you will end up processing the newly added children as part of the current level, destroying the level-by-level grouping.