class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maximum = float('-inf')
        k_nums_value = sum(nums[:k-1])
        i = k-1
        while i < len(nums):
            k_nums_value += nums[i]
            if k_nums_value > maximum:
                maximum = k_nums_value
            k_nums_value -= nums[i-k+1]
            i += 1
        return maximum / float(k)
        