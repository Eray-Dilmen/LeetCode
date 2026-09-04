from collections import Counter


# 1. Single Hash Map Approach (Optimal)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True


# 2. Two Hash Maps Approach (Alternative)
class SolutionTwoMaps:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        st = {}

        for l in s:
            if l in sm:
                sm[l] += 1
            else:
                sm[l] = 1

        for l in t:
            if l in st:
                st[l] += 1
            else:
                st[l] = 1

        return sm == st


# 3. Built-in Counter Approach (Alternative)
class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict


# 4. Sorting Approach (Brute Force)
class SolutionBruteForce:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)