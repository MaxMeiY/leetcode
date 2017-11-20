class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        haha
        """
        result = set(candies)
        return min(len(result), len(candies)//2)