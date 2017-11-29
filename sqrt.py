''' This solution doesn't AC.
    Don't know why
'''

class Solution(object):
    def mySqrt(self, x):
        '''
        :type x: int
        :rtype: int
        '''
        def iter_sqrt(x, guess):
            return guess if good_enough(x, guess) else iter_sqrt(x, improve(x, guess))

        def good_enough(x, guess, fixed=0.1):
            return abs((guess * guess // x) - 1) <= fixed

        def improve(x, guess):
            return ((x / guess) + guess) / 2

        return int(iter_sqrt(x, 1.0))


#-----------------------------------------
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 1
        r = x
        while 1:
            middle = l + (r - l) / 2
            if middle * middle > x:
                r = middle - 1
            else:
                if (middle + 1) * (middle+1) > x:
                    return middle
                l = middle + 1
        