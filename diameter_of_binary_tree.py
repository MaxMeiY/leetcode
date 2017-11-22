# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def f(node):
            if node == None:
                return 0
            left, right = f(node.left), f(node.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        f(root)
        return self.res