class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        min_num = nums[0]
        for i in nums:
            sum += i
            if i < min_num:
                min_num = i
        return sum - min_num * len(nums)
