> 📌 **Guide:** This directory serves as a Concept Map for the **Binary Search** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0704-Binary Search`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Binary Search Pattern?

* **Definition:** A divide-and-conquer algorithm that efficiently locates a target value within a **sorted** search space by repeatedly dividing the search interval in half.
* **The Core Superpower:** It reduces Time Complexity from $O(n)$ (linear search) to **$O(\log n)$** (logarithmic time). This means even for an array of 1 billion elements, it takes a maximum of 30 steps to find the target. When implemented iteratively, its Space Complexity is strictly $O(1)$.

---

## Core Variations & Algorithmic Strategies

Binary Search is not limited to just finding a number in a standard array. It can be adapted to find boundaries, minimums, or even optimal answers.

### 1. Standard Binary Search (Exact Match)
* **Algorithm:** Set `left = 0` and `right = len(nums) - 1`. Use a `while left <= right` loop. Calculate `mid`. If `nums[mid] == target`, return `mid`. If the target is greater, discard the left half (`left = mid + 1`). If smaller, discard the right half (`right = mid - 1`).
* **When to use it:** Finding the exact index of a target element in a perfectly sorted array.
* **Repository Examples:**
  * [0704-Binary Search](./0704-Binary%20Search)
  * [0035-Search Insert Position](./0035-Search%20Insert%20Position)

### 2. Finding Boundaries (First or Last Occurrence)
* **Algorithm:** The array contains duplicate elements, and you need the first or last instance of the target. When `nums[mid] == target`, **do not return immediately**. To find the *first* occurrence, record the position and continue searching in the left half (`right = mid - 1`). To find the *last* occurrence, record it and search in the right half (`left = mid + 1`).
* **When to use it:** When the problem asks for ranges, counts of a specific target, or the first/last time an event occurs in sorted logs.
* **Repository Examples:**
  * [0034-Find First and Last Position of Element in Sorted Array](./0034-Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array)
  * [0278-First Bad Version](./0278-First%20Bad%20Version)

### 3. Binary Search on Answer (Search Space Optimization)
* **Algorithm:** You are not searching on a given array, but on a **range of possible answers** (e.g., minimum capacity `1` to maximum capacity `max(nums)`). You guess an answer (`mid`) and write a helper function `isValid(mid)` to check if this guess satisfies the problem's conditions. Depending on the boolean result, you adjust `left` or `right` to find the absolute minimum or maximum valid answer.
* **When to use it:** When the problem asks for the "minimum maximum", "maximum minimum", or "least capacity/speed" to complete a task within given constraints.
* **Repository Examples:**
  * [0875-Koko Eating Bananas](./0875-Koko%20Eating%20Bananas)
  * [1011-Capacity To Ship Packages Within D Days](./1011-Capacity%20To%20Ship%20Packages%20Within%20D%20Days)

### 4. Search in Rotated Sorted Arrays
* **Algorithm:** The array is sorted but shifted (pivoted) at an unknown point (e.g., `[4,5,6,7,0,1,2]`). Calculate `mid`. You must determine **which half is perfectly sorted**. If `nums[left] <= nums[mid]`, the left half is sorted. Check if the target lies within this sorted range; if so, search left, otherwise search right. Reverse the logic if the right half is sorted.
* **When to use it:** When dealing with shifted/rotated data sequences.
* **Repository Examples:**
  * [0033-Search in Rotated Sorted Array](./0033-Search%20in%20Rotated%20Sorted%20Array)
  * [0153-Find Minimum in Rotated Sorted Array](./0153-Find%20Minimum%20in%20Rotated%20Sorted%20Array)

---

## 💡 Professional Details & Edge Cases

* **Integer Overflow:** In languages like Java or C++, calculating `mid = (left + right) / 2` can cause an integer overflow if `left` and `right` are massive numbers. The professional standard is to calculate it as `mid = left + (right - left) / 2`. (Python handles arbitrarily large integers automatically, but it is still good practice).
* **Loop Condition (`<=` vs `<`):** 
  * Use `while left <= right` when you are actively discarding `mid` from the search space (`left = mid + 1`, `right = mid - 1`).
  * Use `while left < right` when `mid` itself might be the final answer, meaning you cannot discard it (`right = mid`).
* **The "Sorted" Prerequisite:** Binary search inherently requires a sorted search space. If the data is unsorted, you must account for the $O(n \log n)$ time complexity required to sort it first, which might make a Hash Map ($O(n)$) a better alternative depending on the problem.