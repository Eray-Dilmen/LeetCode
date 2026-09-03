> 📌 **Guide:** This directory covers the logic and practical applications of the **Hash Maps & Sets** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0001-Two Sum`) to see the pattern in action.

## What is the Hash Map (and Hash Set) Pattern?

* **Definition:** A Hash Map (or dictionary in Python, `dict`) is a data structure that stores **Key-Value** pairs. A Hash Set (`set`) is a variation that only stores unique keys without associated values.
* **The Core Superpower:** Checking if an element exists (**Lookup / Search**) takes $O(n)$ time in an array or list, but only **$O(1)$ (constant time)** in a Hash Map/Set. This makes it the ultimate tool for optimizing time complexity.

## When to Use It? (Indicators & Repository Examples)

1. **Checking Uniqueness & Existence:** *"Have I seen this element before?"*
   * *Example (`0217-Contains Duplicate`):* As you iterate through an array, add elements to a Hash Set. If you encounter an element that is already in the set, a duplicate exists. The $O(1)$ lookup prevents the need for nested $O(n^2)$ loops.

2. **Fast Matching & Complements (Memory Trade-off):** *"Do I have the exact piece I need to complete a pair?"*
   * *Example (`0001-Two Sum`):* For an equation like $x + y = \text{target}$, rewrite it as $y = \text{target} - x$. For every $x$ you visit, ask the Hash Map: *"Do you have the required `y` in your memory?"* 

3. **Frequency Counting:** *"How many times does this character/number appear?"*
   * *Example (`0383-Ransom Note` & `1189-Maximum Number of Balloons`):* Count the frequencies of characters in a source string and store them in a Hash Map to verify if you have the exact required amounts to construct a target word.

## Hash Set vs. Hash Map: Which One to Choose?

**Hash Set (`set`)**
* A collection of unique keys.
* **The Question it Answers:** *"Does this element exist in the pool?"*
* **Use Case (`0771-Jewels and Stones`):** You only need to know *if* a stone is a jewel. You store the jewels in a Set (`{"a", "A"}`) and check each stone against it. You do not need to know how many times the jewel appeared in the reference string.

**Hash Map (`dict`)**
* A mapping table linking a Key to a specific Value.
* **The Question it Answers:** *"Does this exist, and if so, what is its associated data (count, original index, etc.)?"*
* **Use Case (`0001-Two Sum`):** You need to know both *if* the complement exists AND *what its original array index was*. Therefore, you must map the data: `{"number": index}`.

## 💡 Professional Details & Edge Cases

* **Space-Time Trade-off:** Implementing this pattern almost always reduces Time Complexity from $O(n^2)$ or $O(n \log n)$ down to $O(n)$. However, it increases Space Complexity to $O(n)$ because you are allocating extra memory for the hash table.
* **Hashable Keys Only:** In Python, you can only use **immutable** data types (like integers, strings, or tuples) as keys in a Map or Set. Mutable types like lists or other dictionaries cannot be hashed.