class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        haha
        """
        new_nums = sorted(nums)
        n = len(new_nums)
        first = new_nums[0]
        if first != 0:
            return 0
        i = 1
        while i < n:
            if new_nums[i] - new_nums[i-1] != 1:
                return new_nums[i] - 1
            i += 1
        return n
