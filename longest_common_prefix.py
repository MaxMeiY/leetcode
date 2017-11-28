class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        longest_prefix = strs[0]
        for i in range(1, len(strs)):
            s, j = 0, min(len(longest_prefix), len(strs[i]))
            while s < j and longest_prefix[s] == strs[i][s]:
                s += 1
            longest_prefix = longest_prefix[:s]
            if longest_prefix == '':
                return ''
        return longest_prefix
