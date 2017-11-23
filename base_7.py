class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        def f(num):
            if num < 7:
                return str(num)
            return f(num//7) + str(num%7)
        return '-' + f(abs(num)) if num < 0 else f(num)
        