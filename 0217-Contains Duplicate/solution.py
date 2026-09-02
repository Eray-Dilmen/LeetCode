# Optimum Solution: Hash Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()

        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)

        return False


# Alternative Solution (My Code): Hash Map (Frequency Count)

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


# Brute Force Solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
