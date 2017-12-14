
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def DFS(M, i):
            for j in range(0, len(M[0])):
                if seen[j]:
                    continue
                if M[i][j] == 1:
                    seen[i] = True
                    seen[j] = True
                    DFS(M, j)
        seen = [False] * len(M[0])
        ans = 0
        for i in range(len(M[0])):
            if seen[i]:
                continue
            DFS(M,i)
            ans += 1
        return ans