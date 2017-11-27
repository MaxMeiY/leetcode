class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        pcounter = Counter(p)
        scounter = Counter(s[:len(p)-1])
        res = []
        for i in range(len(p)-1, len(s)):
            scounter[s[i]] += 1
            if scounter == pcounter:
                res.append(i-len(p)+1)
            scounter[s[i-len(p)+1]] -= 1
            if scounter[s[i-len(p)+1]] == 0:
                del scounter[s[i-len(p)+1]]
        return res
