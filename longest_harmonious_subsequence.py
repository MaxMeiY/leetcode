class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        for i in nums:
            temp[i] = temp.get(i, 0) + 1
        ans = 0

        for i in temp:
            if i + 1 in temp:
                ans = max(ans, temp[i] + temp[i+1])
        return ans