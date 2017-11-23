class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        S = sum(nums)

        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i
            left_sum += x
        return -1
