# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        ha
        """
        diff = []
        def f(root):
            if root is None:
                return float('inf')
            left = f(root.left)
            node_value = root.val
            diff.append(node_value)
            right = f(root.right)

        f(root)
        ans = float('inf')
        for i in range(1, len(diff)):
            if diff[i] - diff[i-1] < ans:
                ans = diff[i] - diff[i-1]
        return ans
