class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def f(s):
            temp = {}
            res = []
            for i, x in enumerate(s):
                if not x in temp:
                    temp[x] = i
                res.append(temp[x])
            return res

        return f(pattern) == f(str.split())
    