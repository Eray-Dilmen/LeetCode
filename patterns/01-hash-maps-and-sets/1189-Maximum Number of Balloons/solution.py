# 1. Hash Map Approach (Optimal)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}

        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2,
            letters.get('o', 0) // 2,
            letters.get('n', 0)
        )