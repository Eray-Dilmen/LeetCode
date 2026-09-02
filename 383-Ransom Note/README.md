# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

## Problem Description
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:
> **Input:** `ransomNote = "a"`, `magazine = "b"`
> **Output:** `false`

### Example 2:
> **Input:** `ransomNote = "aa"`, `magazine = "ab"`
> **Output:** `false`

### Example 3:
> **Input:** `ransomNote = "aa"`, `magazine = "aab"`
> **Output:** `true`

---

## Approach 1: Hash Map (Optimal Solution)

### Intuition
To determine if we can build the ransom note, we need to know if the magazine has enough of each required letter. Instead of repeatedly searching through the string, we can use a Hash Map (dictionary) to count the frequency of each character available in the `magazine`. Then, as we process the `ransomNote`, we deduct the used characters from our map.

### Algorithm
1. Initialize an empty hash map `guide` to store the character frequencies.
2. Iterate through each `letter` in the `magazine`. If it exists in the map, increment its count. Otherwise, add it with a count of 1.
3. Iterate through each `char` in the `ransomNote`.
4. Check if the `char` exists in the `guide` and if its count is greater than 0:
   - **If no:** Return `False` immediately (we lack the required letter).
   - **If yes:** Decrement the count of that character in the map by 1.
5. If the loop completes without failing, return `True`.

### Complexity
- **Time complexity:** $\mathcal{O}(m + n)$ — We iterate through the `magazine` (length $m$) once and the `ransomNote` (length $n$) once. Hash map insertions and lookups take $\mathcal{O}(1)$ time.
- **Space complexity:** $\mathcal{O}(1)$ — The hash map `guide` stores at most 26 lowercase English letters. Since the maximum size is strictly bounded by 26 regardless of the input size, it requires constant extra space.

### Code
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        guide = {}
        for index, letter in enumerate(magazine):
            if letter in guide:
                guide[letter] += 1
            else:
                guide[letter] = 1
                
        for char in ransomNote:
            if char not in guide or guide[char] == 0:
                return False
            guide[char] -= 1
            
        return True
```

---

## Approach 2: Brute Force

### Intuition
The brute force approach checks each letter of the `ransomNote` against the `magazine`. Since strings are immutable in Python, we convert the `magazine` into a list so we can physically remove characters as they are "used" to prevent reusing the same letter.

### Algorithm
1. Convert the `magazine` string into a list of characters `mag_list`.
2. Iterate through each `char` in `ransomNote`.
3. Check if `char` exists in `mag_list`.
4. If it does, remove that specific character from `mag_list` using the `.remove()` method.
5. If it doesn't exist, return `False`.
6. Return `True` if all characters are successfully found and removed.

### Complexity
- **Time complexity:** $\mathcal{O}(n \times m)$ — For each of the $n$ characters in `ransomNote`, we potentially scan the entire `mag_list` of size $m$ to find and remove the character.
- **Space complexity:** $\mathcal{O}(m)$ — We create a new list `mag_list` which takes space proportional to the length of the `magazine` string.

### Code
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)
        
        for char in ransomNote:
            if char in mag_list:
                mag_list.remove(char)
            else:
                return False
                
        return True
```