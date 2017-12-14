class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p,n = 1, len(nums)
        res = []
        for i in range(n):
            res.append(p)
            p = p * nums[i]

        p = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * p
            p = p * nums[j]
        return res
