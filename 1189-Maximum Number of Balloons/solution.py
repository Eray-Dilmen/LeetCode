# Optimum Solution: Hash Map (Frequency Count)
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


# Alternative Solution: Multiple Passes (Built-in Count)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2,
            text.count('o') // 2,
            text.count('n')
        )