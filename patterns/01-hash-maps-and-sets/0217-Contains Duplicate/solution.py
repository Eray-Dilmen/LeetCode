# 1. Hash Set Approach (Optimal)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = set()

        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)

        return False


# 2. Frequency Map Approach (Alternative)
class SolutionFrequencyMap:
    def containsDuplicate(self, nums: list[int]) -> bool:
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


# 3. Brute Force Approach
class SolutionBruteForce:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False