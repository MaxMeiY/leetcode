class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = [0]
        visit = [False]*(N + 1)

        def f(pos):
            if pos > N:
                count[0] += 1
            else:
                for i in range(1, N+1):
                    if not visit[i] and (
                           i % pos == 0 or pos % i == 0):
                        visit[i] = True
                        f(pos+1)
                        visit[i] = False
        f(1)
        return count[0]

if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(15))