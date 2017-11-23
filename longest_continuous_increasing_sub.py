class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        maximum = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                if temp > maximum:
                    maximum = temp
                temp = 1
        return max(temp, maximum)
