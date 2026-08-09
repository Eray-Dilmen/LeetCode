# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

---

# Intuition
A number is a palindrome if it reads the same backward as forward. Converting the integer into a string allows us to easily reverse it using slicing and check if the original representation matches the reversed string.

# Approach
1. Convert the integer `x` into its string representation `s`.
2. Reverse the string `s` using Python string slicing (`s[::-1]`) and store it in `x_reverse`.
3. Compare `s` with `x_reverse`:
   - If they are equal, return `True`.
   - Otherwise, return `False`.

---

# Complexity
- **Time complexity:** $\mathcal{O}(N)$ where $N$ is the number of digits in the integer $x$. String conversion and slicing both process each character/digit once.
- **Space complexity:** $\mathcal{O}(N)$ since string conversion creates a new string object of length $N$ to store the reversed representation.

---

# Code

```python
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        x_reverse = s[::-1]
        if s == x_reverse:
            return True
        else:
            return False