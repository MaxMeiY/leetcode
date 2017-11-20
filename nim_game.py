class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool

        My original idea.
        but it's too dumb
        """
        if n == 4:
            return False
        elif n < 4:
            return True
        else:
            min_1 = self.canWinNim(n-1-1) and self.canWinNim(n-1-2) and self.canWinNim(n-1-3)
            min_2 = self.canWinNim(n-2-1) and self.canWinNim(n-2-2) and self.canWinNim(n-2-3) 
            min_3 = self.canWinNim(n-3-1) and self.canWinNim(n-3-2) and self.canWinNim(n-3-3)
            return min_1 or min_2 or min_3


# There is a clever idea
# see the login behind the code
#https://discuss.leetcode.com/topic/27109/one-line-o-1-solution-and-explanation
def solution(n):
    return n % 4 != 0