class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            if not s[i] in map1:
                map1[s[i]] = t[i]
            if not t[i] in map2:
                map2[t[i]] = s[i]
            if map1[s[i]] != t[i] or map2[t[i]] != s[i]:
                return False
        return True
                