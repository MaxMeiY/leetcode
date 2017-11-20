class Solution:
    def moveZeros(self, nums):
        '''
        :type nums: List[int]
        :rtype: void
        '''
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1