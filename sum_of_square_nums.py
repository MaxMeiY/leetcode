class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        i = int(math.sqrt(c))
        j = 0
        while j <= i:
            if i * i + j * j > c:
                i -= 1
            elif i * i + j * j < c:
                j += 1
            else:
                return True
        return False