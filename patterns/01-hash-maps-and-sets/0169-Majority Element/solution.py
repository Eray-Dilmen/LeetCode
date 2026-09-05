# 1. Boyer-Moore Voting Algorithm Approach (Optimal)
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ans = 0
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if ans == num:
                count += 1
            else:
                count -= 1

        return ans


# 2. Hash Map Approach (Alternative)
class SolutionHashMap:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i] += 1

        for i in d:
            if d[i] > (len(nums) / 2):
                return i


# 3. Sorting Approach (Brute Force)
class SolutionSorting:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]