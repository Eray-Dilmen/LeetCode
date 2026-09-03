# 1. Hash Set Approach (Optimal)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0

        for stone in stones:
            if stone in s:
                count += 1

        return count


# 2. Brute Force Approach
class SolutionBruteForce:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for stone in stones:
            if stone in jewels:
                count += 1

        return count