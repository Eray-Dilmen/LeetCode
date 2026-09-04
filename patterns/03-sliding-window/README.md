> 📌 **Guide:** This directory serves as a Concept Map for the **Sliding Window** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0209-Minimum Size Subarray Sum`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Sliding Window Pattern?

* **Definition:** A specific sub-type of the Two Pointers pattern where the two pointers (`left` and `right`) define a "window" or boundary. This window slides across an array or string to track a contiguous subset of elements.
* **The Core Superpower:** Instead of recalculating the sum, product, or frequency of a subarray from scratch using nested loops (`O(n²)`), a sliding window reuses the work from the previous step. It adds the new element entering the window and subtracts the old element leaving the window, reducing the time complexity to a single pass (`O(n)`).

---

## Core Variations & Algorithmic Strategies

The Sliding Window pattern changes based on whether the size of the subarray is fixed or determined by a dynamic condition.

### 1. Fixed Size Window
* **Algorithm:** The distance between the `left` and `right` pointers is always exactly `k`. First, calculate the state (sum/average) of the first `k` elements. Then, slide the window by moving both pointers one step at a time: add the new element at `right` to the state, and subtract the element at `left - 1` that just left the window.
* **When to use it:** When the problem explicitly asks for a contiguous subarray or substring of a specific length (e.g., "maximum sum of any contiguous subarray of size k").
* **Repository Examples:**
  * [0643-Maximum Average Subarray I](./0643-Maximum%20Average%20Subarray%20I)
  * [1343-Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](./1343-Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold)

### 2. Dynamic Size Window (Shrinkable)
* **Algorithm:** The window size expands and contracts based on a target condition. The `right` pointer moves forward in a `for` loop to expand the window. Whenever the window's state violates the problem's condition (or satisfies it, depending on the goal), use a `while` loop to move the `left` pointer forward, shrinking the window until the condition is valid again.
* **When to use it:** When you need to find the longest/shortest contiguous subarray/substring that meets a certain criteria (e.g., "minimum length subarray with sum >= target").
* **Repository Examples:**
  * [0209-Minimum Size Subarray Sum](./0209-Minimum%20Size%20Subarray%20Sum)
  * [0003-Longest Substring Without Repeating Characters](./0003-Longest%20Substring%20Without%20Repeating%20Characters)

### 3. Dynamic Window with Auxiliary Data Structure (Hash Map/Set)
* **Algorithm:** Same as the dynamic window, but it utilizes a Hash Map, Set, or frequency array to track the internal state of the window (like character frequencies or unique element counts). As `right` expands, update the map. As `left` shrinks, decrement counts and remove keys if they hit zero.
* **When to use it:** String manipulation problems where the condition depends on character frequency, repeating characters, or finding anagrams.
* **Repository Examples:**
  * [0424-Longest Repeating Character Replacement](./0424-Longest%20Repeating%20Character%20Replacement)
  * [0438-Find All Anagrams in a String](./0438-Find%20All%20Anagrams%20in%20a%20String)

---

## 💡 Professional Details & Edge Cases

* **State Synchronization:** The most common bug in Sliding Window algorithms is forgetting to update the running state (sum, count, hash map) *before* moving the `left` pointer. Always remove `nums[left]` from your state tracker before `left += 1`.
* **Two Pointers vs. Sliding Window:** Use Two Pointers when the elements can be independent or paired from anywhere in the array. Use Sliding Window **strictly** when the problem asks for a **contiguous** subarray or substring.
* **Condition Logic:** Pay close attention to the `while` loop condition for the `left` pointer. You must decide whether the loop should run while the condition is *valid* (to find minimums) or *invalid* (to restore validity for finding maximums).