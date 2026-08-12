# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Approach: String Conversion and Slicing

### Intuition
The straightforward approach is to convert the integer to a string to easily manipulate its digits. By taking the absolute value, casting it to a string, and reversing it using slicing, we can flip the digits. Finally, we convert it back to an integer, reapply the original sign, and verify it doesn't exceed the 32-bit integer limits.

### Algorithm
1. Check if `x` is negative and store this state in `is_negative`.
2. Get the absolute value of `x`, convert it to a string, and reverse it using `[::-1]`.
3. Cast the reversed string back into an integer and assign it to `result`.
4. If the original number was negative, negate `result`.
5. Check if `result` falls outside the 32-bit signed integer limits (`[-2**31, 2**31 - 1]`). If it overflows, return `0`.
6. Return `result`.

### Complexity
- **Time complexity:** $\mathcal{O}(\log(x))$ — The number of digits in $x$ is roughly $\log_{10}(x)$. String conversion and reversing take time proportional to the number of digits.
- **Space complexity:** $\mathcal{O}(\log(x))$ — We use extra space to store the string representation of the reversed digits.

### Code
```python
class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        result = int(str(abs(x))[::-1])
        if is_negative:
            result = -result
            
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
```