class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        res = 0
        middle = False
        for char in s:
            record[char] = 1 + record.get(char, 0)
        for val in record.values():
            if val % 2 == 0:
                res += val
            elif val > 2:
                res += val - 1
                middle = True
            elif val == 1:
                middle = True
        return res + 1 if middle else res
