class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def f(k, n, start, res):
            if k == 0 and n == 0:
                ans.append(list(res)) # be careful! list() casue res will be [], and the res in ans will be [] too
            else:
                # from num 1 to 9. so 9 + 1
                for i in range(start, 9+1):
                    res.append(i)  # add this item
                    f(k-1,n-i, i+1,res)
                    res.pop()   # don't add this item

        f(k, n, 1, [])
        return ans