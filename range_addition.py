'''
 STUPID IDEA!
 but correct
 very slow!!


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        M = [[0 for _ in xrange(n)] for _ in xrange(m)]
        res = {}
        for op in ops:
            for row in range(op[0]):
                for col in range(op[1]):
                    M[row][col] += 1
                    res[M[row][col]] = res[M[row][col]] + 1 if M[row][col] in res else 1

        print(res)
        if res != {}:

            key = max(res.keys())
            return res[key]
        return m * n
'''


class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        x,y = zip(*ops)
        return min(x) * min(y)
        