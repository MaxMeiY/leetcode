class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        def f(res, target, start):
            if target < 0:
                return
            if target == 0:
                ans.append(res)
                return
            for i in range(start, len(candidates)):
                f(res+[candidates[i]], target-candidates[i], i)
        f([], target, 0)
        return ans