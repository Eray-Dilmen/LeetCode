# Optimal Solution (Hash Set)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jews = set(jewels)
        count = 0
        for stone in stones:
            if stone in jews:
                count += 1
        return count


# Brute Force Solution
class SolutionBruteForce:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    count += 1
                    break
        return count