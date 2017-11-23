class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        haha
        """
        if n == 1:
            return 1
        a, b = 1, 0
        while n >= 0:
            a,b = a+b, a
            n -= 1
        return b
        