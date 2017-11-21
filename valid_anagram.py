class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        haha
        """
        if len(s) != len(t):
            return False
        temp = {}
        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1
        print(temp)

        for j in range(len(t)):
            if t[j] not in temp:
                return False
            temp[t[j]] -= 1

            if temp[t[j]] < 0:
                return False
        return True