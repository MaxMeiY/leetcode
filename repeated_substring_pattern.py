class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = s[0]
        length = len(s)
        for i in range(1,length):
            if s[i] == start:
                if s[:i] * (length // i) == s:
                    return True
        return False


    def great_solution(self, s):
        '''
        same as above
        '''
        if not s:
            return False
        ss = s + s
        T = ss[1:-1]
        return T.find(s) != -1