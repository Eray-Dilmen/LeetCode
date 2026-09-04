> 📌 **Guide:** This directory serves as a Concept Map for the **Trie (Prefix Tree)** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0208-Implement Trie (Prefix Tree)`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Trie Pattern?

* **Definition:** A Trie (pronounced "try"), also known as a Prefix Tree, is a specialized tree data structure used to store an associative array, where the keys are usually strings. Unlike a binary tree, nodes do not store the key associated with that node; instead, its position in the tree defines the key with which it is associated.
* **The Core Superpower:** The ultimate tool for **Prefix Matching** and **Autocomplete**. While a Hash Set can find a complete word in $O(1)$ time, it cannot easily find all words starting with "auto-". A Trie searches for a word or prefix in strict **$O(L)$** time (where $L$ is the length of the word), completely independent of how many millions of words are stored in the tree.

---

## Core Variations & Algorithmic Strategies

The Trie pattern revolves around building a custom `TrieNode` class and traversing it character by character.

### 1. Standard Trie (Insert / Search / StartsWith)
* **Algorithm:** Create a `TrieNode` containing a Hash Map (or an array of size 26) for its children, and a boolean `is_word` flag. 
  * **Insert:** Iterate through the word's characters. If a character is not in the current node's children, create a new node. Move the pointer down. Mark the final node's `is_word = True`.
  * **Search:** Traverse down using the characters. If a character is missing, return `False`. At the end of the word, return the `is_word` flag.
  * **StartsWith:** Same as Search, but return `True` simply if you successfully reach the end of the prefix.
* **When to use it:** Autocomplete systems, spell checkers, and IP routing.
* **Repository Examples:**
  * [0208-Implement Trie (Prefix Tree)](./0208-Implement%20Trie%20%28Prefix%20Tree%29)
  * [0211-Design Add and Search Words Data Structure](./0211-Design%20Add%20and%20Search%20Words%20Data%20Structure)

### 2. Trie + DFS / Backtracking (Grid Traversal)
* **Algorithm:** When searching for multiple words inside a 2D matrix (Boggle/Word Search), checking every word individually using DFS is incredibly slow. Instead, insert all target words into a Trie. As you run DFS on the matrix, pass the current `TrieNode`. If the matrix character is not in the `TrieNode`'s children, you immediately prune (abandon) the DFS branch.
* **When to use it:** When you have a dictionary of words to find within a matrix or a string.
* **Repository Examples:**
  * [0212-Word Search II](./0212-Word%20Search%20II)
  * [0140-Word Break II](./0140-Word%20Break%20II)

### 3. Bitwise Trie
* **Algorithm:** Instead of storing characters, the Trie stores the bits (`0` and `1`) of integers (usually 32 levels deep). To find the maximum XOR of any two numbers in an array, insert all numbers into the Trie. Then, for each number, traverse the Trie trying to always pick the opposite bit (`1` if the current bit is `0`) to maximize the XOR result.
* **When to use it:** Finding Maximum XOR pairs or subarrays in $O(n)$ time instead of $O(n^2)$.
* **Repository Examples:**
  * [0421-Maximum XOR of Two Numbers in an Array](./0421-Maximum%20XOR%20of%20Two%20Numbers%20in%20an%20Array)

---

## 💡 Professional Details & Edge Cases

* **Hash Map vs. Array for Children:** Inside the `TrieNode`, you can store children as `children = {}` (Hash Map) or `children = [None] * 26` (Array). The Hash Map is more space-efficient if the character set is large or sparse (e.g., Unicode). The Array is slightly faster due to cache locality but wastes memory if you only have a few branches. In Python, the dictionary approach is the professional standard.
* **Space Complexity Warning:** While Tries are incredibly fast, they are memory hogs. Every character potentially spawns a new node object. If memory is strictly limited, compressed Tries (Radix Trees) are used in production, though they are rarely required for standard LeetCode problems.
* **The "Prefix Deletion" Trap:** Deleting a word from a Trie requires extreme caution. You cannot just delete the nodes, because other words might share that prefix. You must only delete a node if it is not the end of another word and has no other children. Often, just setting `is_word = False` is the safest "lazy deletion" strategy.