class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        import math
        res = 0
        for i in range(1, int(math.sqrt(num)+1)):
            if num % i == 0:
                res += i
                if i * i != num:
                    res += num / i

        return res - num == num