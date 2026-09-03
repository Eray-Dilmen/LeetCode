# 1. Hash Map Approach (Optimal)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}

        for index, num in enumerate(nums):
            if (target - num) in mapping:
                return [mapping[target - num], index]
            mapping[num] = index


# 2. Brute Force Approach
class SolutionBruteForce:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]