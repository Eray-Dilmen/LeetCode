> 📌 **Guide:** This directory serves as a Concept Map for the **Prefix Sum** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0303-Range Sum Query - Immutable`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Prefix Sum Pattern?

* **Definition:** An algorithmic technique that creates a precomputed array where each element at index `i` represents the sum (or product) of all elements from the start of the original array up to index `i`.
* **The Core Superpower:** When you need to calculate the sum of a specific subarray from index `left` to `right`, recalculating it using a loop takes `O(n)` time. By precomputing a prefix sum array once in `O(n)` time, you can answer any subarray sum query in `O(1)` (constant time) using the formula: `Sum = prefix[right] - prefix[left - 1]`.

---

## Core Variations & Algorithmic Strategies

The Prefix Sum pattern is a fundamental building block. It is often combined with other data structures like Hash Maps to solve complex problems.

### 1. Static Subarray Queries
* **Algorithm:** Create a `prefix` array of the same size (or `size + 1` to handle edge cases cleanly). Iterate through the input array, keeping a running total, and store it in the `prefix` array. To find the sum of any subarray between indices `i` and `j`, return `prefix[j] - prefix[i - 1]`.
* **When to use it:** When a problem requires you to repeatedly query the sum of different subarrays on an array that does not change (immutable).
* **Repository Examples:**
  * [0303-Range Sum Query - Immutable](./0303-Range%20Sum%20Query%20-%20Immutable)
  * [0724-Find Pivot Index](./0724-Find%20Pivot%20Index)

### 2. Prefix Sum + Hash Map (Dynamic Subarray Matching)
* **Algorithm:** Instead of checking all subarrays, keep a running `prefix_sum` as you iterate. To find a subarray that sums to a specific `target`, use the mathematical logic: `prefix_sum - target = required_previous_sum`. Check if `required_previous_sum` exists in a Hash Map that tracks the frequencies of all previous prefix sums.
* **When to use it:** When you need to find the *count* or *maximum length* of contiguous subarrays that sum to a specific value (`k`), especially when the array contains negative numbers (which breaks the Sliding Window pattern).
* **Repository Examples:**
  * [0560-Subarray Sum Equals K](./0560-Subarray%20Sum%20Equals%20K)
  * [0525-Contiguous Array](./0525-Contiguous%20Array)

### 3. Bidirectional Arrays (Prefix & Suffix)
* **Algorithm:** Some problems require knowing what is to the left AND right of a specific element without including the element itself. Create two arrays: a `prefix` array building up from the left, and a `suffix` (or postfix) array building up from the right. The result for index `i` is usually `prefix[i - 1] * suffix[i + 1]`.
* **When to use it:** When calculating products or sums for every element *except* `nums[i]`, and division is prohibited or zeroes are present.
* **Repository Examples:**
  * [0238-Product of Array Except Self](./0238-Product%20of%20Array%20Except%20Self)

---

## 💡 Professional Details & Edge Cases

* **The Dummy Zero / Base Case:** When using the Prefix Sum + Hash Map variation, always initialize your map with `{0: 1}` (meaning a sum of 0 has been seen once). This ensures that if a valid subarray starts from index `0`, the formula `prefix_sum - target == 0` is successfully caught.
* **Negative Numbers & Sliding Window:** If a problem asks for a subarray sum and the array contains negative numbers, **do not** use Sliding Window. A sliding window relies on the assumption that adding elements increases the sum and removing decreases it. Negative numbers destroy this logic. You must use Prefix Sum + Hash Map instead.
* **Space Optimization:** For Bidirectional variations (like Product of Array Except Self), you do not strictly need two separate `O(n)` arrays. You can compute the prefix directly into the output array, and then use a single integer variable to track the running suffix on a second reverse pass, reducing extra memory to `O(1)`.