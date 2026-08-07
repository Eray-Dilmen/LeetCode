# 1. Two Sum

## Approach 1: Hash Map (Optimal Solution)

### Intuition
Instead of using two nested loops to check every pair, we can reformulate the problem as $x + y = \text{target}$, which means $y = \text{target} - x$. As we iterate through the array, we just need to check if the required complementary number ($y$) has already been seen.

### Algorithm
1. Initialize a hash map to store each number as the key and its index as the value (`{number: index}`).
2. Iterate through `nums` using `enumerate` to track both the current index and number.
3. For each number, calculate `complement = target - num`.
4. Check if `complement` exists in the hash map:
   - **If yes:** Return the saved index of `complement` (`mapping[target - num]`) and the current index (`index`).
   - **If no:** Add the current number and its index to the hash map (`mapping[num] = index`).

### Complexity
- **Time complexity:** $\mathcal{O}(n)$ — We traverse the list containing $n$ elements only once. Hash map lookups take $\mathcal{O}(1)$ average time.
- **Space complexity:** $\mathcal{O}(n)$ — In the worst case, the hash map stores up to $n$ elements.

### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, num in enumerate(nums): 
            if (target - num) in mapping:
                return [mapping[target - num], index]
            else:
                mapping[num] = index
``` 

## Approach 2: Brute Force

### Intuition
The brute force approach simply tests every possible pair of numbers in the array to see if their sum equals the target value.

### Algorithm
1. Use an outer loop to select the first element `nums[i]`.
2. Use an inner loop starting from index `i + 1` to select the second element `nums[j]`.
3. Check if `nums[i] + nums[j] == target`.
4. If a matching pair is found, return their indices `[i, j]`.

### Complexity
- **Time complexity:** $\mathcal{O}(n^2)$ — For $n$ elements, we try all possible pairs, resulting in $\frac{n(n-1)}{2}$ comparisons.
- **Space complexity:** $\mathcal{O}(1)$ — No extra space is required as we only use pointers.

### Code
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+ nums[j] == target):
                    return [i,j]
```