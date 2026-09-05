# 1. Hash Set Approach (Optimal)
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1

                while next_num in s:
                    length += 1
                    next_num += 1

                longest = max(longest, length)

        return longest


# 2. Sorting Approach (Alternative / Slower)
class SolutionSorting:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest = max(longest, current_streak)
                    current_streak = 1

        return max(longest, current_streak)