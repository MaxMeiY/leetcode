# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left != None and (root.left.left == None and root.left.right == None):
            left_leaf = root.left.val
        else:
            left_leaf = 0

        left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right + left_leaf

'''
More intuitive

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None:
            return self.sumOfLeftLeaves(root.right)
        elif (root.left.left is None) & (root.left.right is None):
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
'''