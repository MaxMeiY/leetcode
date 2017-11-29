class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        new_nums = sorted(nums)
        l = len(nums)
        r = 0
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                l = min(l, i)
                r = max(r, i)
        return r - l + 1if r - l > 0 else 0