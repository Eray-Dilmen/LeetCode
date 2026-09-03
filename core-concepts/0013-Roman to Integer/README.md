# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Problem Description
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`. Given a roman numeral, convert it to an integer.

## Approach: Left-to-Right Pass

### Intuition
Roman numerals are typically written from largest to smallest, left to right. However, the numeral for four is not `IIII`, but `IV`. Because the one is before the five, we subtract it making four. The same principle applies to the number nine, which is written as `IX`. Therefore, if a smaller numeral appears before a larger numeral, it implies subtraction. Otherwise, it implies addition.

### Algorithm
1. Initialize a hash map `roman_map` mapping each Roman numeral character to its integer value.
2. Initialize a `result` variable to `0`.
3. Iterate through the string `s` using an index `i`.
4. For each character, check if there is a next character (`i < len(s) - 1`) and if the current character's value is strictly less than the next character's value.
   - **If yes:** Subtract the current character's value from `result`.
   - **If no:** Add the current character's value to `result`.
5. Return the final `result`.

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We iterate through the string of length $n$ exactly once. Hash map lookups take $\mathcal{O}(1)$ time.
- **Space complexity:** $\mathcal{O}(1)$ — The hash map requires constant space since there are only 7 symbols. No dynamically growing data structures are used.

### Code
```python
class Solution(object):
    def romanToInt(self, s):
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i in range(len(s)):
            if i < len(s)-1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result