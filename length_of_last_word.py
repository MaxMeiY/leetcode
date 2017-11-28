class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = s.split()
        return len(last[-1]) if last else 0
        