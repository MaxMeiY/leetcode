class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [False] * len(nums)
        ans, step = 0, 0
        for i in range(len(nums)):
            while not seen[i]:
                seen[i] = True
                step, i = step + 1, nums[i]
            ans = max(step, ans)
            step = 0
        return ans