class Solution(object):
    def twoSum(self, nums, target):
        mapping = {}

        for index, num in enumerate(nums):
            if (target-num) in mapping:
                return [mapping[target - num], index]
            else:
                mapping[num] = index