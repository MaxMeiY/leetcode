class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l < r:
            middle = l + (r-l) / 2
            if nums[middle] != nums[middle+1] and nums[middle] != nums[middle-1]:
                return nums[middle]
            elif nums[middle] == nums[middle-1] and middle % 2 == 0:
                r = middle - 1
            elif nums[middle] == nums[middle+1] and middle % 2 == 1:
                r = middle - 1
            else:
                l = middle + 1
        return nums[l]