# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

## Approach: Vertical Scanning (Character-by-Character)

### Intuition
To find the longest common prefix, we can use the first string in the array as a reference. We iterate through each character of this reference string and compare it against the characters at the exact same index in all other strings. As long as the characters match across all strings, we append it to our result. The moment we encounter a mismatch or reach the end of any string, the common prefix ends.

### Algorithm
1. Initialize an empty string `cm_pref` to build the common prefix.
2. Iterate through each character index `i` of the first string (`strs[0]`).
3. Set a boolean flag `is_common = True` for the current index.
4. Use an inner loop to check adjacent string pairs (`strs[j]` and `strs[j+1]`) in the array.
5. In the inner loop, verify two conditions:
   - Index `i` is within the bounds of both `strs[j]` and `strs[j+1]`.
   - The characters at index `i` for both strings match.
6. If the conditions are met, continue checking. If not, set `is_common = False` and break the inner loop.
7. After the inner loop, if `is_common` is true, append `strs[0][i]` to `cm_pref`. If false, break the outer loop entirely.
8. Return `cm_pref`.

### Complexity
- **Time complexity:** $\mathcal{O}(N \times M)$ — Where $N$ is the number of strings in the array and $M$ is the length of the first string. In the worst case, we check the character at index `i` for all $N$ strings.
- **Space complexity:** $\mathcal{O}(M)$ — To store the resulting prefix string `cm_pref`, which can be at most the length of the first string.

### Code
```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        cm_pref = ''
        for i in range(len(strs[0])): 
            is_common = True
            for j in range(len(strs)-1): 
                if i < len(strs[j]) and i < len(strs[j+1]) and strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    is_common = False
                    break
                      
            if is_common:
                cm_pref += strs[0][i]
            else:
                break    
        
        return cm_pref
```