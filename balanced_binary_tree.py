# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_balanced(node):
            if node == None:
                return True
            left = self.height(node.left)
            right = self.height(node.right)
            if abs(left - right) <= 1 and is_balanced(node.left) and is_balanced(node.right):
                return True
            else:
                return False
        return is_balanced(root)
    
    
    def height(self, node):
        if node == None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

#-----------------------------------------------------------------
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(node):
            if node == None:
                return 0
            left = f(node.left)
            right = f(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return f(root) != -1
            