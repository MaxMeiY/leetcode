class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        diff = []
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                diff.append(prices[i] - prices[i-1])
        return sum(diff) if sum(diff) > 0 else 0

#-one-line-python-GREAT
# of course, I didn't think of it.haha
class Solution2:
    def maxProfit(self,prices):
        return sum(max(prices[i+1] - prices[i], 0)
                   for i in range(len(prices) -1))
    
