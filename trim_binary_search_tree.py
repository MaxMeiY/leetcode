# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        haha
        """
        if root is None:
            return None
        if root.val < L:
            # I once wrote return root.right WRONG!!
            return self.trimBST(root.right, L, R)
        if root.val > R:
            # I once wrote return root.left WRONG!
            return self.trimBST(root.left, L, R)
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root