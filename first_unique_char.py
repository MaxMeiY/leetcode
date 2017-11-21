class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections

        s_c = collections.Counter(s)
        for i in range(len(s)):
            if s_c[s[i]] == 1:
                return i
        return -1
