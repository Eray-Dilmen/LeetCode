# 1. Hash Map Approach (Optimal)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        guide = {}

        for letter in magazine:
            if letter in guide:
                guide[letter] += 1
            else:
                guide[letter] = 1

        for char in ransomNote:
            if char not in guide or guide[char] == 0:
                return False
            guide[char] -= 1

        return True


# 2. Brute Force Approach
class SolutionBruteForce:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)

        for char in ransomNote:
            if char in mag_list:
                mag_list.remove(char)
            else:
                return False

        return True