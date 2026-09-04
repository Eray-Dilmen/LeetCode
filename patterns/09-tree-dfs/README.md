> 📌 **Guide:** This directory serves as a Concept Map for the **Tree Depth-First Search (DFS)** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0104-Maximum Depth of Binary Tree`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Tree DFS Pattern?

* **Definition:** An algorithmic technique for traversing or searching tree data structures. It starts at the `root` and explores as far as possible along each branch before backtracking. It is almost always implemented using **Recursion** (which inherently uses the system's call stack) or iteratively using an explicit Stack.
* **The Core Superpower:** DFS perfectly maps to the recursive, hierarchical nature of trees. Instead of complex pointer manipulation, you define the logic for a single node and let the recursion handle the rest. Time complexity is strictly **$O(n)$** (visiting every node once), and space complexity is **$O(h)$** (where $h$ is the height of the tree, representing the maximum call stack depth).

---

## Core Variations & Algorithmic Strategies

Tree DFS generally splits into two main conceptual approaches: passing information *down* to the children, or passing information *up* to the parents.

### 1. Top-Down DFS (Pre-order Traversal)
* **Algorithm:** Process the current `node` first, then recursively call DFS on `node.left` and `node.right`. You usually pass a running state (like a current path or a running sum) as a parameter down to the recursive calls.
* **When to use it:** When a node's logic depends on the accumulated path from the root to itself, or when you are searching for a root-to-leaf path that meets a condition.
* **Repository Examples:**
  * [0112-Path Sum](./0112-Path%20Sum)
  * [0144-Binary Tree Preorder Traversal](./0144-Binary%20Tree%20Preorder%20Traversal)

### 2. Bottom-Up DFS (Post-order Traversal)
* **Algorithm:** Recursively call DFS on `node.left` and `node.right` *before* processing the current `node`. The base case returns a value, and the parent node uses the return values from its left and right children to calculate its own answer, which it then returns to its own parent.
* **When to use it:** When a node's answer relies completely on the answers of its subtrees (e.g., calculating height, diameter, or checking if the tree is balanced).
* **Repository Examples:**
  * [0104-Maximum Depth of Binary Tree](./0104-Maximum%20Depth%20of%20Binary%20Tree)
  * [0543-Diameter of Binary Tree](./0543-Diameter%20of%20Binary%20Tree)
  * [0236-Lowest Common Ancestor of a Binary Tree](./0236-Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree)

### 3. In-order Traversal & Binary Search Trees (BST)
* **Algorithm:** Traverse `node.left`, process the `node`, then traverse `node.right`. 
* **The BST Superpower:** When you perform an In-order DFS on a valid Binary Search Tree (where left children are strictly smaller and right children are strictly larger), it visits the nodes in **perfectly sorted, ascending order**.
* **When to use it:** Validating if a tree is a BST, finding the Kth smallest/largest element, or converting a BST to an array.
* **Repository Examples:**
  * [0098-Validate Binary Search Tree](./0098-Validate%20Binary%20Search%20Tree)
  * [0230-Kth Smallest Element in a BST](./0230-Kth%20Smallest%20Element%20in%20a%20BST)

---

## 💡 Professional Details & Edge Cases

* **The Ultimate Base Case:** The very first line of almost every DFS function should be `if not node: return ...`. Failing to handle the `None` (or `null`) node is the #1 cause of `AttributeError: 'NoneType' has no attribute 'left'` exceptions.
* **Global Variables vs. Return Values:** In Bottom-Up DFS (like finding the Diameter of a tree), you often need to return the height to the parent, but also update a `max_diameter` that is not part of the return path. Professionally, use a class-level variable (e.g., `self.max_diameter`) or a mutable array `[0]` to track this global state across recursive calls, rather than relying on messy global variables.
* **Recursion Limit:** Python has a default recursion depth limit (usually 1000). For extremely deep, unbalanced trees (which degenerate into Linked Lists), a recursive DFS might trigger a `RecursionError`. In production code, if trees are massive and unbalanced, you must rewrite the DFS iteratively using an explicit `Stack` array.