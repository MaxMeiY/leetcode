class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        haha
        """
        max_sum = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if temp > max_sum:
                    max_sum = temp
                temp = 0
            else:
                temp += 1
        return max(max_sum,temp)
