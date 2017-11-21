class Solution:
    def findContentChildren(self, g, s):
        """
        greedy algorithm
        
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_sort = sorted(g)
        s_sort = sorted(s)
        res = 0
        child_index = 0
        cookie_index = 0
        while child_index < len(g_sort) and cookie_index < len(s_sort):
            if g_sort[child_index] <= s_sort[cookie_index]:
                res += 1
                child_index += 1
                cookie_index += 1
            elif g_sort[child_index] > s_sort[cookie_index]:
                cookie_index += 1
        return res

