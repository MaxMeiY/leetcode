class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '11'
        length = 1
        s_next = []
        while n > 2:
            for i in range(1,len(s)):
                if s[i-1] == s[i]:
                    length +=1
                else:
                    s_next.append(str(length))
                    s_next.append(s[i-1])
                    length = 1
            s = ''.join(s_next) + str(length) + s[i]
            print(s)
            n -= 1
            length = 1
            s_next = []
        return s