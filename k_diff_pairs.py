class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mapping = {}
        for i in nums:
            if i not in mapping:
                mapping[i] = 1
            else:
                mapping[i] = mapping[i] + 1
        ans = 0
        for i in mapping:
            if k == 0 and mapping[i] > 1 or k > 0 and i + k in mapping:
                ans += 1
        return ans