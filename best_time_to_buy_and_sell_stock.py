class Solution:
    def maxProfit(self, prices):
        '''
        :type List(int)
        :rtype int
        '''
        if len(prices) <= 1:
            return 0

        max_profit = 0
        minimum = prices[0]

        for i in range(1, len(prices)):
            minimum = min(prices[i], minimum)
            max_profit = max(max_profit, prices[i]-minimum)
        return max_profit