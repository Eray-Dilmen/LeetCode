# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
> **Input:** `nums = [1,2,3,1]`  
> **Output:** `true`

### Example 2:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `false`

### Example 3:
> **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Output:** `true`

---

## Approach 1: Hash Set (Optimal Solution)

### Intuition
To determine if an array contains duplicates, we only need to know if we have seen a number before. Instead of storing the frequency of each number, we can use a Hash Set. As we iterate through the array, we check if the current number is already in the set. If it is, we found a duplicate and can return `True` immediately (early exit). If not, we add it to the set and continue.

### Algorithm
1. Initialize an empty hash set `numbers`.
2. Iterate through each `number` in `nums`.
3. Check if the `number` exists in the `numbers` set:
   - **If yes:** Return `True` immediately.
   - **If no:** Add the `number` to the `numbers` set.
4. If the loop completes without finding any duplicates, return `False`.

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We iterate through the array of length $n$ at most once. Hash set lookups and insertions take $\mathcal{O}(1)$ time on average.
- **Space complexity:** $\mathcal{O}(n)$ — In the worst-case scenario (where all elements are distinct), the hash set will store all $n$ elements.

### Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        
        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)
            
        return False
```

---

## Approach 2: Hash Map / Frequency Count (Alternative Solution)

### Intuition
This approach calculates the frequency of each number in the array using a Hash Map (dictionary). After populating the frequencies, we iterate over the map to check if any number has a count greater than 1. While this works and has a linear time complexity, it requires two separate passes (one to build the map, one to check it) and uses more memory to store both keys and values.

### Algorithm
1. Initialize an empty hash map `number_count`.
2. Iterate through `nums` to populate the map. If a number is not in the map, add it with a count of 1. Otherwise, increment its count.
3. Iterate through the populated `number_count` map.
4. If any number has a count strictly greater than 1, return `True`.
5. Return `False` if no duplicates are found.

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We iterate through the array once ($\mathcal{O}(n)$) and then iterate through the dictionary ($\mathcal{O}(n)$ worst-case). The total operations scale linearly with $n$.
- **Space complexity:** $\mathcal{O}(n)$ — We store up to $n$ unique numbers and their frequencies in the hash map.

### Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_count = {}
        
        for number in nums:
            if number not in number_count:
                number_count[number] = 1
            else:
                number_count[number] += 1
        
        for number in number_count:
            if number_count[number] > 1:
                return True
        
        return False
```

---

## Approach 3: Brute Force

### Intuition
The brute force approach compares every element in the array with every other element that comes after it using nested loops. If a match is found, a duplicate exists.

### Algorithm
1. Use an outer loop to pick a number at index `i`.
2. Use an inner loop starting from index `i + 1` to the end of the array.
3. Compare the number at `i` with the number at `j`. If they are equal, return `True`.
4. If all comparisons are completed without a match, return `False`.

### Complexity
- **Time complexity:** $\mathcal{O}(n^2)$ — The nested loops compare each element with the rest, resulting in $\approx \frac{n(n-1)}{2}$ operations, which results in a quadratic time complexity. This will likely cause a Time Limit Exceeded (TLE) error on large inputs.
- **Space complexity:** $\mathcal{O}(1)$ — No extra space is required as the comparison is done in place.

### Code

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                    
        return False
```