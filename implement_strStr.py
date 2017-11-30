class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        ha
        """
        if haystack == '' and needle == '':
            return 0
        if haystack == '':
            return -1
        if needle == '':
            return 0
        l_needle = len(needle)
        l_haystack = len(haystack)
        for i in range(0, l_haystack-l_needle+1):
            if haystack[i:i+l_needle] == needle:
                return i
        return -1