class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] > timeSeries[i-1] + duration - 1:
                ans += duration
            elif timeSeries[i] == timeSeries[i-1] + duration - 1:
                ans += duration - 1
            else:
                ans += timeSeries[i] - timeSeries[i-1]
        return ans + duration if len(timeSeries) != 0 else 0
