class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0:
            return False
        while n:
            temp = n % 2
            n = n // 2
            if temp % 2 != 0:
                return False
            if n == 1:
                return True
