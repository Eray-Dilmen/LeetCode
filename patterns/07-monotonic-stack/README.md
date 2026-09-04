> 📌 **Guide:** This directory serves as a Concept Map for the **Monotonic Stack** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0739-Daily Temperatures`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Monotonic Stack Pattern?

* **Definition:** A stack data structure where the elements are maintained in a strictly increasing or strictly decreasing order. If a new element violates this order, elements are popped from the stack until the monotonic condition is restored.
* **The Core Superpower:** The ultimate tool for finding the **"Next Greater Element"** or **"Next Smaller Element"**. Instead of using nested loops to search forward for a greater value (`O(n²)`), this pattern processes each element exactly twice (once pushed, once popped), resulting in a highly optimized `O(n)` time complexity.

---

## Core Variations & Algorithmic Strategies

The Monotonic Stack relies on the principle of "waiting." Elements in the stack are "unresolved" (waiting to find their next greater/smaller counterpart) until a suitable element arrives to resolve them.

### 1. Next Greater / Next Smaller Element
* **Algorithm:** To find the next *greater* element, maintain a **monotonically decreasing** stack. Iterate through the array. While the stack is not empty and the current element is *greater* than the element at the top of the stack, it means you have found the "next greater element" for the top item. Pop it, record the answer, and push the current element.
* **When to use it:** When a problem asks you to find the closest element to the right (or left) that is strictly larger or smaller than the current element (e.g., "How many days until a warmer temperature?").
* **Repository Examples:**
  * [0739-Daily Temperatures](./0739-Daily%20Temperatures)
  * [0496-Next Greater Element I](./0496-Next%20Greater%20Element%20I)

### 2. Circular Arrays (Next Greater Element II)
* **Algorithm:** The array wraps around (the last element connects back to the first). Instead of a single pass, iterate through the array twice by running the loop up to `2 * n` and using the modulo operator (`i % n`) to access elements. The Monotonic Stack logic remains exactly the same.
* **When to use it:** When searching for the next greater element in a circular structure.
* **Repository Examples:**
  * [0503-Next Greater Element II](./0503-Next%20Greater%20Element%20II)

### 3. Previous Boundary (Maximum/Minimum Area)
* **Algorithm:** Used to find the span or boundaries of an element. To find the previous smaller element, maintain an increasing stack. When you pop elements to maintain the order, the element that *remains* at the top of the stack just before pushing the current element is its "previous smaller" boundary.
* **When to use it:** Histogram problems, calculating maximum areas of rectangles, or trapping water scenarios.
* **Repository Examples:**
  * [0084-Largest Rectangle in Histogram](./0084-Largest%20Rectangle%20in%20Histogram)
  * [0901-Online Stock Span](./0901-Online%20Stock%20Span)

---

## 💡 Professional Details & Edge Cases

* **Store Indices, Not Values:** The most crucial professional standard in Monotonic Stack problems is pushing the **index** of the array into the stack, not the actual value. Storing the index allows you to easily calculate the distance (e.g., `current_index - popped_index`) and still access the value using `nums[index]`.
* **Strict vs. Non-Strict Monotonicity:** Pay attention to duplicates. If the problem asks for the next element that is *strictly* greater (`>`), pop when the current element is strictly greater. If it asks for greater or equal (`>=`), adjust your `while` loop condition accordingly.
* **Remaining Elements:** After the loop finishes, any indices left in the stack represent elements that *never* found a next greater/smaller element. You often need to initialize your result array with `-1` (or `0`) so these unresolved elements inherently have the correct default answer.