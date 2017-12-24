class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        '''
        Explain:
        1 + 2 --> 3,
        1 + 3 -->2,
        2 + 3 -->1
        ? + ? --> None (e.g. 1 + 1 --> None)
        when n > 2 and m >= 3
        there're only 8 cases
        all_on, 1, 2, 3, 4, 1+4,2+4,3+4
        '''
        if n == 0: return 0
        if m == 0: return 1
        if n == 1: return 2
        if n == 2:
            if m == 1: return 3
            return 4
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8