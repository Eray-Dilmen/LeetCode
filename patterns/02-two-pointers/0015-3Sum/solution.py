# 1. Two Pointers Approach (Optimal)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = set()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    l.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return list(l)


# 2. Brute Force Approach (Time Limit Exceeded)
class SolutionBruteForce:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l.add((nums[i], nums[j], nums[k]))

        return list(l)