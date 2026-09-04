> 📌 **Guide:** This directory serves as a Concept Map for the **Intervals** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0056-Merge Intervals`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Intervals Pattern?

* **Definition:** An algorithmic technique used to manage and process sets of ranges (intervals), usually represented as pairs of numbers `[start, end]`.
* **The Core Superpower:** Overlapping intervals can create chaotic, `O(n²)` comparison problems. By proactively **sorting the intervals based on their start times**, this pattern linearizes the chaos, allowing you to resolve all overlaps in a single `O(n)` pass. The overall time complexity becomes **$O(n \log n)$** strictly due to the initial sorting phase.

---

## Core Variations & Algorithmic Strategies

The way you handle the `end` times determines the specific variation of the pattern.

### 1. Merging Intervals
* **Algorithm:** Sort the array of intervals by their `start` times. Push the first interval into a `merged` list. Iterate through the rest. If the current interval's `start` is less than or equal to the previous interval's `end` (an overlap), merge them by updating the previous interval's `end` to the `max(previous_end, current_end)`. If they do not overlap, simply append the current interval to the list.
* **When to use it:** When the problem asks you to combine all overlapping meetings, ranges, or schedules into continuous blocks.
* **Repository Examples:**
  * [0056-Merge Intervals](./0056-Merge%20Intervals)

### 2. Inserting a New Interval
* **Algorithm:** You are given a sorted list of non-overlapping intervals and a new interval to insert. Instead of sorting everything again (which takes $O(n \log n)$), you can do this in `O(n)` time. Iterate through the intervals: add all intervals that end *before* the new one starts, merge all overlapping intervals into the new interval by expanding its bounds (`min(starts)`, `max(ends)`), and finally add the remaining intervals that start *after* the new one ends.
* **When to use it:** When managing an already sorted calendar/schedule and adding a new event.
* **Repository Examples:**
  * [0057-Insert Interval](./0057-Insert%20Interval)

### 3. Overlap Counting & Removal (Greedy Intervals)
* **Algorithm:** Instead of merging, you want to find the minimum number of intervals to remove to make the rest non-overlapping, or the maximum number of simultaneous events. **Sort by `start` time** (or sometimes `end` time for greedy approaches). Keep track of the `prev_end`. When an overlap occurs, increment your removal counter and greedily keep the interval that ends *earlier* (update `prev_end = min(prev_end, current_end)`) to leave more room for future intervals.
* **When to use it:** Meeting Rooms problems, finding maximum non-overlapping events, or counting conflicts.
* **Repository Examples:**
  * [0435-Non-overlapping Intervals](./0435-Non-overlapping%20Intervals)
  * [0252-Meeting Rooms](./0252-Meeting%20Rooms)

### 4. Interval Intersections (Two Pointers)
* **Algorithm:** Given two separate lists of sorted intervals, find their intersections. Use Two Pointers (`i` for list A, `j` for list B). An intersection exists if `start_max <= end_min`. If it exists, the overlapping range is `[start_max, end_min]`. Move the pointer of the interval that ends *earlier*, because it cannot possibly overlap with any future intervals.
* **When to use it:** Finding common free time between two people's schedules.
* **Repository Examples:**
  * [0986-Interval List Intersections](./0986-Interval%20List%20Intersections)

---

## 💡 Professional Details & Edge Cases

* **Sorting is Mandatory:** Unless the problem explicitly states the intervals are already sorted, your first line of code should almost always be `intervals.sort(key=lambda x: x[0])`.
* **The Overlap Formula:** Two intervals `A` and `B` (where `A` starts before `B`) overlap if and only if `B.start <= A.end`. This single logical check is the heart of the entire pattern.
* **The Subsumed Interval Bug:** When merging, do not assume the second interval's end is always larger. For example, merging `[1, 5]` and `[2, 3]`. The second interval is completely swallowed by the first. Always use `max(A.end, B.end)` to establish the new boundary, otherwise you might incorrectly shrink the merged interval to `[1, 3]`.