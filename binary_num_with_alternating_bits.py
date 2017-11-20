class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        haha
        """
        string_n = format(n, 'b')
        first = string_n[0]
        for i in range(1, len(string_n)):
            if first == string_n[i]:
                return False
            first = string_n[i]
        return True
