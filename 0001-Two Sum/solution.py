class Solution(object):
    # Approach 1: Hash Map Solution - O(n) Time Complexity
    def twoSum(self, nums, target):
        mapping = {}

        for index, num in enumerate(nums):
            if (target - num) in mapping:
                return [mapping[target - num], index]
            else:
                mapping[num] = index

    # Approach 2: Brute Force Solution - O(n^2) Time Complexity
    def twoSum_bruteForce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]