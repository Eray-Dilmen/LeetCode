# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

## Problem Description
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

## Approach 1: Hash Set (Optimal Solution)

### Intuition
Instead of using two nested loops to check every pair[cite: 3], we can optimize the problem by converting our `jewels` string into a Hash Set. As we iterate through our `stones` array, we just need to check if the current stone exists in our set[cite: 3]. Searching in a Hash Set takes constant time, which drastically improves performance.

### Algorithm
1. Initialize a hash set `jews` to store the unique characters from the `jewels` string.
2. Initialize a `count` variable to `0` to keep track of the matches.
3. Iterate through each character (`stone`) in the `stones` string.
4. Check if the `stone` exists in the `jews` hash set:
   - **If yes:** Increment the `count` by 1.
5. Return the final `count`.

### Complexity
- **Time complexity:** $\mathcal{O}(J + S)$ — We traverse the `jewels` string (length $J$) once to build the set, and the `stones` string (length $S$) once to count. Hash set lookups take $\mathcal{O}(1)$ average time[cite: 3].
- **Space complexity:** $\mathcal{O}(J)$ — In the worst case, the hash set stores up to $J$ unique characters from the `jewels` string[cite: 3].

### Code
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jews = set(jewels)
        count = 0
        for stone in stones:
            if stone in jews:
                count += 1
        return count
``` 

## Approach 2: Brute Force

### Intuition
The brute force approach simply tests every possible pair[cite: 3] of stones and jewels to see if there is a match.

### Algorithm
1. Initialize a `count` variable to `0`.
2. Use an outer loop to select each character `stone` in `stones`[cite: 3].
3. Use an inner loop to select each character `jewel` in `jewels`[cite: 3].
4. Check if `stone == jewel`[cite: 3].
5. If a matching pair is found, increment the `count` and break the inner loop.
6. Return the `count`.

### Complexity
- **Time complexity:** $\mathcal{O}(J \times S)$ — For $S$ stones, we try matching against all $J$ jewels, resulting in $J \times S$ comparisons[cite: 3].
- **Space complexity:** $\mathcal{O}(1)$ — No extra space is required as we only use pointers[cite: 3] and a counter variable.

### Code
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
                    break 
        return count
```