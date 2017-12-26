class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = [0]
        def f(nums, target, res):
            if res > target:
                return 0
            if target == res:
                ans[0] += 1
                return 0
            for i in nums:
                f(nums, target, res+i)
            return res
        f(nums, target, 0)
        return ans[0]

    def f(self, nums, target):
        nums, com = sorted(nums), [1] + [0] * target
        for i in range(target+1):
            for num in nums:
                if num > i: break
                elif num == target: com[i] += 1
                else:
                    com[i] = com[i] + com[i - num]
        return com[target]