from collections import defaultdict


# 1. Frequency Tuple & Hash Map Approach (Optimal)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())


# 2. Sorting & Hash Map Approach (Alternative)
class SolutionSorting:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            anagrams_dict[sorted_word].append(s)

        return list(anagrams_dict.values())