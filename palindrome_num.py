class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revert_num = 0
        while x > revert_num:
            revert_num = revert_num * 10 + x % 10
            x = x // 10
        return revert_num == x or revert_num// 10 == x
