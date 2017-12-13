class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        middle = nums[len(nums)// 2]
        ans = 0
        for item in nums:
            ans += abs(middle - item)

        return ans