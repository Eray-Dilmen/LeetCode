class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        x_reverse = s[::-1]
        if s == x_reverse:
            return True

        else:
            return False
