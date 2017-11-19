class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        haha
        """
        return ' '.join([x[::-1] for x in s.split(' ')])