# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        haha
        """
        def f(node, r):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                if r == sum:
                    return 1
                else:
                    return -1
            left = f(node.left, r+node.val)
            right = f(node.right, r+node.val)

            return max(left,right)
        return f(root, 0) == 1