# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        ha
        """
        def f(node, depth):
            if node == None:
                return (float('-inf'), None)
            if node.left == None and node.right == None:
                return (depth, node.val)
            if node.left == None:
                return f(node.right, depth+1)
            if node.right == None:
                return f(node.left, depth+1)
            left_dp, left_val = f(node.left, depth+1)
            right_dp, right_val = f(node.right,depth+1)
            return (left_dp, left_val) if left_dp >= right_dp else (right_dp, right_val)
        dp, val = f(root, 0)
        return val
        