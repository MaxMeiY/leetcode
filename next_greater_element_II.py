class Solution:
    def next_greater_ele(self, nums):
        '''
        :type list[int]
        :rtype list[int]
        '''
        stack, res = [], [-1 for _ in range(len(nums))]
        for i in range(2):  # Two rounds, cause circular
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
                stack.append(i)
        return res


# see Leetcode 503 Discuss section!