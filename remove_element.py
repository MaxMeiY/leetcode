class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()
        done = False
        i = 0
        while i < len(nums) and not done:
            if nums[i] != val:
                i += 1
                continue
            while i < len(nums) and nums[i] == val:
                del nums[i]
            done = True
        return len(nums)