class Solution(object):
    def reverse(self, x):
        is_negative = x < 0
        result = int(str(abs(x))[::-1])
        if is_negative:
            result = -result

        if result < -2**31 or result > 2**31-1:
            return 0
        return result