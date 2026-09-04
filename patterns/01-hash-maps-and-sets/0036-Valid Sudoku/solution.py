# 1. Hash Set Approach (Optimal)
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row validation
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # column validation
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # box validation
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]

        for i, j in starts:
            s = set()
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    item = board[row][column]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True


# 2. List Lookup Approach (Brute Force / Inefficient)
class SolutionBruteForce:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            l = []
            for j in range(9):
                item = board[i][j]
                if item in l:
                    return False
                elif item != '.':
                    l.append(item)

        return True