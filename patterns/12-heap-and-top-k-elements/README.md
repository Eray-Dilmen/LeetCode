> 📌 **Guide:** This directory serves as a Concept Map for the **Heap & Top K Elements** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0215-Kth Largest Element in an Array`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Heap & Top K Elements Pattern?

* **Definition:** A Heap is a specialized tree-based data structure that satisfies the heap property. In a **Min-Heap**, the parent node is always smaller than or equal to its children (the smallest element is at the root). In a **Max-Heap**, the parent is always greater.
* **The Core Superpower:** The ultimate tool for finding the largest, smallest, or most frequent "K" elements in a dataset. Sorting an entire array takes **$O(n \log n)$** time. By maintaining a Heap of strictly size `k`, you can find the Top K elements in **$O(n \log k)$** time. If `k` is small, this is significantly faster and only uses **$O(k)$** auxiliary space.

---

## Core Variations & Algorithmic Strategies

Heaps are universally used whenever a problem asks for "the best", "the closest", or "the most frequent" elements without requiring the rest of the array to be perfectly sorted.

### 1. Top K Largest / Smallest Elements
* **Algorithm:** To find the Top K *Largest* elements, maintain a **Min-Heap** of size `k`. Iterate through the array and push each element into the heap. If the heap's size exceeds `k`, pop the root (which removes the smallest element currently in the heap). By the end of the loop, the Min-Heap will contain exactly the `k` largest elements. Reverse the logic (use a Max-Heap) to find the smallest elements.
* **When to use it:** When asked for the Kth largest/smallest element, or the K closest points to an origin.
* **Repository Examples:**
  * [0215-Kth Largest Element in an Array](./0215-Kth%20Largest%20Element%20in%20an%20Array)
  * [0973-K Closest Points to Origin](./0973-K%20Closest%20Points%20to%20Origin)

### 2. Top K Frequent Elements
* **Algorithm:** First, use a Hash Map to count the frequencies of all elements ($O(n)$ time). Then, iterate through the Hash Map and push `(frequency, element)` tuples into a Min-Heap of size `k`. If the size exceeds `k`, pop it. The heap automatically sorts tuples based on the first value (the frequency).
* **When to use it:** When filtering data based on occurrence rates or popularity.
* **Repository Examples:**
  * [0347-Top K Frequent Elements](./0347-Top%20K%20Frequent%20Elements)
  * [0692-Top K Frequent Words](./0692-Top%20K%20Frequent%20Words)

### 3. K-way Merge
* **Algorithm:** You are given `k` sorted arrays or Linked Lists and need to merge them into a single sorted list. Push the first element of each of the `k` lists into a Min-Heap. Pop the absolute smallest element from the heap, add it to your result, and immediately push the *next* element from the exact same list that the popped element originated from.
* **When to use it:** Merging multiple sorted streams of data simultaneously.
* **Repository Examples:**
  * [0023-Merge k Sorted Lists](./0023-Merge%20k%20Sorted%20Lists)

### 4. Two Heaps (Median of a Data Stream)
* **Algorithm:** To find the median of a dynamic stream of numbers in $O(1)$ time, maintain two heaps. Use a **Max-Heap** to store the smaller half of the numbers, and a **Min-Heap** to store the larger half. Rebalance them so their sizes never differ by more than 1. The median is either the root of the larger heap, or the average of both roots.
* **When to use it:** Calculating rolling medians or balancing dynamic halves of a dataset.
* **Repository Examples:**
  * [0295-Find Median from Data Stream](./0295-Find%20Median%20from%20Data%20Stream)

---

## 💡 Professional Details & Edge Cases

* **The Python Max-Heap Hack:** Python's built-in `heapq` module only provides a Min-Heap. To simulate a Max-Heap, multiply the values by `-1` before pushing them into the heap. When you pop them out, multiply by `-1` again to restore the original value.
* **Tuple Comparisons:** When pushing tuples like `(priority, value)` into a heap, the heap compares them based on the `priority`. However, if two items have the *exact same priority*, the heap will try to compare the `value`. If the `value` is an object that does not support comparison (like a custom class or a ListNode), Python will throw a `TypeError`. To fix this, add a unique counter to the tuple: `(priority, tie_breaker_id, value)`.
* **Heapify vs. Push:** If you already have an entire array of elements and want to turn it into a heap, do not use a `for` loop to push them one by one ($O(n \log n)$). Use `heapq.heapify(array)`, which rearranges the array in-place in strictly **$O(n)$** time.