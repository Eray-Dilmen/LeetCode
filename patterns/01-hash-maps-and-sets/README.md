> 📌 **Guide:** This directory serves as a Concept Map for the **Hash Maps & Sets** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0001-Two Sum`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Hash Map (and Hash Set) Pattern?

* **Definition:** A Hash Map (or dictionary in Python, `dict`) is a data structure that stores **Key-Value** pairs. A Hash Set (`set`) is a variation that only stores unique keys without associated values.
* **The Core Superpower:** Checking if an element exists (**Lookup / Search**) takes $O(n)$ time in an array or list, but only **$O(1)$ (constant time)** in a Hash Map/Set. This makes it the ultimate tool for optimizing time complexity by trading memory for speed.

---

## Core Variations & Algorithmic Strategies

The Hash Map pattern is highly versatile. Here is how it is typically deployed:

### 1. Frequency Counting (Histograms)
* **Algorithm:** Iterate through a sequence (string/array) and count the occurrences of each element. If the element is not in the map, add it with a value of 1. If it exists, increment its value (`map[char] = map.get(char, 0) + 1`).
* **When to use it:** When you need to verify if you have the exact required amounts to construct a target word, or checking if two strings have identical character counts.
* **Repository Examples:**
  * [0242-Valid Anagram](./0242-Valid%20Anagram)
  * [0383-Ransom Note](./0383-Ransom%20Note)

### 2. Fast Matching & Complement Search
* **Algorithm:** Instead of checking every pair with nested loops, calculate the "complement" you need to satisfy a condition. For an equation like $x + y = target$, rewrite it as $y = target - x$. As you iterate, ask the Hash Map: *"Do you have the required `y` in your memory?"* If not, store the current element and its index in the map for future lookups.
* **When to use it:** Finding pairs that sum/multiply to a specific target without sorting the array first.
* **Repository Examples:**
  * [0001-Two Sum](./0001-Two%20Sum)

### 3. Uniqueness & Existence (Hash Set)
* **Algorithm:** Add elements to a Hash Set as you iterate. If you encounter an element that is already in the set, a duplicate exists. Alternatively, store a reference pool (like jewels) in a set and check each target element against it.
* **When to use it:** You only need to know *if* an element exists in the pool, and do not care about counts or indices.
* **Repository Examples:**
  * [0217-Contains Duplicate](./0217-Contains%20Duplicate)
  * [0771-Jewels and Stones](./0771-Jewels%20and%20Stones)

### 4. Grouping & Mapping Relationships
* **Algorithm:** Process an item to find a common "signature" or property (e.g., sorting a string alphabetically). Use this signature as the **Key** in a Hash Map, and append the original item to a list stored in the **Value** (`map[signature].append(item)`).
* **When to use it:** Grouping elements that share a common trait (like anagrams) or mapping character replacements.
* **Repository Examples:**
  * [0049-Group Anagrams](./0049-Group%20Anagrams)

---

## 💡 Professional Details & Edge Cases

* **Space-Time Trade-off:** Implementing this pattern almost always reduces Time Complexity from $O(n^2)$ or $O(n \log n)$ down to $O(n)$. However, it increases Space Complexity to $O(n)$ because you are allocating extra memory for the hash table.
* **Hashable Keys Only:** In Python, you can only use **immutable** data types (like integers, strings, or tuples) as keys in a Map or Set. Mutable types like lists or other dictionaries cannot be hashed.