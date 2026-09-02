# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

## Problem Description
Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

### Example 1:
> **Input:** `text = "nlaebolko"`  
> **Output:** `1`

### Example 2:
> **Input:** `text = "loonbalxballpoon"`  
> **Output:** `2`

### Example 3:
> **Input:** `text = "leetcode"`  
> **Output:** `0`

---

## Approach 1: Hash Map (Optimal Solution)

### Intuition
To form the word "balloon", we need specific amounts of certain characters: one 'b', one 'a', two 'l's, two 'o's, and one 'n'. We can count the frequencies of all characters in the given `text` using a Hash Map (dictionary). 

The maximum number of times we can form the word is bottlenecked by the character we have the least of (relative to the required amount). Thus, we can find the limiting character by taking the minimum of the available character counts.
* **Why use `.get(char, 0)`?** If a character (like 'b') doesn't exist in our dictionary, accessing `letters['b']` would raise a `KeyError`. Using `.get('b', 0)` safely returns `0` instead of crashing, accurately reflecting that we have zero 'b's.
* **Why use `min()`?** The `min()` function acts as our bottleneck finder. Even if we have 100 'b's, if we only have 1 'n', we can only make 1 "balloon". `min()` calculates this absolute limit based on the scarcest required resource.

### Algorithm
1. Initialize an empty hash map `letters` to store character frequencies.
2. Iterate through each `letter` in the `text`. If it exists in the map, increment its count. Otherwise, add it with a count of 1.
3. Use the `min()` function to determine the maximum possible instances of "balloon".
4. For 'l' and 'o', divide their counts by 2 (using integer division `// 2`) since they are needed twice per word.
5. Return the calculated minimum value.

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We iterate through the `text` of length $n$ exactly once to build the frequency map. Looking up values in the hash map takes $\mathcal{O}(1)$ time.
- **Space complexity:** $\mathcal{O}(1)$ — The hash map stores at most 26 lowercase English letters. Since the maximum size is strictly bounded by 26 regardless of the input size, it requires constant extra space.

### Code
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                
        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2,
            letters.get('o', 0) // 2,
            letters.get('n', 0)
        )
```

---

## Approach 2: Multiple Passes / Built-in Count (Alternative Solution)

### Intuition
Instead of building a frequency map manually, we can use Python's built-in `.count()` method directly on the string. We only care about the frequencies of 'b', 'a', 'l', 'o', and 'n'. While this is syntactically shorter, it scans the entire string multiple times (once for each character we count).

### Algorithm
1. Call `text.count()` for each of the characters 'b', 'a', 'l', 'o', and 'n'.
2. Divide the counts of 'l' and 'o' by 2.
3. Pass all these values into the `min()` function.
4. Return the result.

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We scan the string 5 separate times. Although $5n$ is technically $\mathcal{O}(n)$, it is slightly slower in practice than a single pass for very large strings.
- **Space complexity:** $\mathcal{O}(1)$ — No extra data structures are created.

### Code
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2,
            text.count('o') // 2,
            text.count('n')
        )
```