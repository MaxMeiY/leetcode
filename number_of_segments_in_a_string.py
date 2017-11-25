class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([x for x in s.split(' ') if x != ''])
        