class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(nums, start, end):
            if end == start:
                return nums[start]
            if end < start:
                return 0
            if end - start == 1:
                return max(nums[start], nums[end])
            for i in range(start, end+1):
                maximum = max(nums[start]+f(nums, start+2, end), f(nums, start+1, end))
            return maximum
        return  f(nums, 0, len(nums)-1)

    def other(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        d = [0 for i in range(len(nums)+1)]
        d[1] = nums[0]
        d[2] = max(nums[0], nums[1])
        for i in range(3, len(nums)+1):
            d[i] = max(nums[i-1]+d[i-2], d[i-1])
        return d[len(nums)]
        