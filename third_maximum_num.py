class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = [float('-inf'), float('-inf'), float('-inf')]
        for i in nums:
            if i not in v:
                if i > v[0]:
                    v[2] = v[1]
                    v[1] = v[0]
                    v[0] = i
                elif i > v[1]:
                    v[2] = v[1]
                    v[1] = i
                elif i > v[2]:
                    v[2] = i
        return v[2] if v[2] != float('-inf') else v[0]
                