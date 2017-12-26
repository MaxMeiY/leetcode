'''
 Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations. 
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        count = collections.Counter(nums)
        avoid = using = 0
        prev = None
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k*count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*count[k] + avoid
        return max(avoid, using)