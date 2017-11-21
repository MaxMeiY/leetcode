class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        beat 95%
        I'm proud!
        """
        ranks = {}
        length = len(nums)
        sort_nums = sorted(nums)
        rank = 0
        for i in range(length-1, -1, -1):
            ranks[sort_nums[i]] = rank
            rank += 1

        res = []
        for i in nums:
            item = ranks[i]
            if item == 0:
                item = 'Gold Medal'
            elif item == 1:
                item = 'Silver Medal'
            elif item == 2:
                item = 'Bronze Medal'
            if type(item) is type(1):
                res.append(str(item+1))
            else:
                res.append(item)
        return res