class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        haha
        """
        if numRows == 0:
            return []
        ans = [[1]]
        if numRows == 1:
            return ans
        for row in range(1, numRows):
            ans.append([])
            for col in range(row+1):
                entry = ans[row-1][col-1] + ans[row-1][col] if col != 0 and col != row else 1
                ans[row].append(entry)
        return ans
