> 📌 **Guide:** This directory covers the logic and practical applications of the **Two Pointers** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0167-Two Sum II - Input Array Is Sorted`) to see the pattern in action.

## What is the Two Pointers Pattern?

* **Definition:** An algorithmic technique that uses two variables (pointers or indices) to iterate through a data structure (usually an array or string) simultaneously. 
* **The Core Superpower:** It optimizes algorithms by replacing nested loops (`O(n²)`) with a single concurrent pass (`O(n)`). Crucially, it achieves this while maintaining a strict `O(1)` space complexity because it only requires two integer variables, completely avoiding extra memory allocation like Hash Maps.

## When to Use It? (Indicators & Repository Examples)

1. **Sorted Arrays & Target Finding:** *"Find a pair that sums to a specific value."*
   * *Example (`0167-Two Sum II`):* By placing one pointer at the start and one at the end of a sorted array, you can conditionally shrink the search space based on whether the current sum is too large or too small.

2. **Symmetry & Palindromes:** *"Does this read the same forwards and backwards?"*
   * *Example (`0125-Valid Palindrome`):* Start pointers at both ends and move them inward. If they ever point to different characters, the sequence is not a palindrome. 

3. **In-Place Array Modifications:** *"Remove duplicates without using extra memory."*
   * *Example (`0026-Remove Duplicates from Sorted Array`):* Use a "Slow" pointer to track the position of the last unique element, and a "Fast" pointer to scan for the next new element, modifying the array directly.

## Opposite Ends vs. Same Direction: Which One to Choose?

**Left & Right Pointers (Opposite Direction)**
* Pointers start at `index 0` and `index len - 1` and move towards the center until they meet (`left < right`).
* **The Question it Answers:** *"How do the extremes of this sequence relate to each other?"*
* **Use Case:** Sorted arrays (Two Sum II), reversing a string, or palindrome checks.

**Slow & Fast Pointers (Same Direction)**
* Both pointers start at `index 0`. The Fast pointer moves every step, while the Slow pointer only moves when a specific condition is met.
* **The Question it Answers:** *"How can I filter, shift, or detect cycles in this data as I read it?"*
* **Use Case:** Removing duplicates in-place, moving zeros to the end, or finding the middle of a Linked List.

## 💡 Professional Details & Edge Cases

* **The Sorted Prerequisite:** For Opposite Direction pointers to work effectively in search or sum problems, the data **must** be sorted. If the data is unsorted and you cannot sort it (which would take `O(n log n)`), you should likely use a Hash Map instead.
* **Pointer Bounds (Index Out of Bounds):** Always ensure your loop condition (`while left < right` or `while fast < len(nums)`) strictly prevents pointers from crossing improperly or accessing indices outside the array bounds.