class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return []
        ans = [[1]]
        for row in range(1, rowIndex+1):
            ans.append([1 for _ in range(row+1)])
            for col in range(1,row):
                ans[row][col] = ans[row-1][col-1] + \
                                ans[row-1][col]

        return ans[rowIndex]