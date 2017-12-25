class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # two base case.
        # cause we assume the ans will be greater than itself.
        # but it's not the case for n == 2, 3
        # beyond those two nums it's correct
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*dp[i-j])
        return dp[n]