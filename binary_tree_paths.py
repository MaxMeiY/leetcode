# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def f(root, path):
            if not root.left and not root.right:
                ans.append(path+str(root.val))
            if root.left:
                f(root.left, path+str(root.val) + '->')
            if root.right:
                f(root.right, path+str(root.val) + '->')
        if root == None:
            return ans
        f(root, '')
        return ans
