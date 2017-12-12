class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        nxt = [float('inf')] * 102
        for i in range(len(temperatures)-1, -1, -1):
            warm_index = min(nxt[j] for j in range(temperatures[i]+1,102))
            if warm_index < float('inf'):
                ans[i] = warm_index - i
            nxt[temperatures[i]] = i
        return ans