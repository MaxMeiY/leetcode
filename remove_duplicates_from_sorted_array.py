class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        i = 1
        start = 1
        dupicate = False
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                if not dupicate:
                    start = j
                dupicate = True
            elif nums[j] != nums[j-1]:
                if dupicate:
                    nums[start] = nums[j]
                    start += 1
                i += 1
        return i



#-----------------------------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return 1

        ind = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[ind] = nums[i]
                ind += 1
        return ind

