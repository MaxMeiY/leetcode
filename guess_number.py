# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            middle = (end + start) // 2
            response = guess(middle)
            if response == 0:
                return middle
            elif response < 0:
                end = middle -1
            else:
                start = middle + 1