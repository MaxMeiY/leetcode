# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minPath(self, root):
        '''
        :type root: TreeNode
        :rtype: int
        '''
        def f(node):
            if node == None:
                return 0
            if not node.left and not node.right:
                return 1
            left = f(node.left) if node.left else float('inf')
            right = f(node.right) if node.right else float('inf')
            return 1 + min(left, right)
        return f(root)