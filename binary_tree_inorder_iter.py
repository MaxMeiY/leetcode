# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = [root]
        if root == None:
            return []
        while stack:
            node = stack.pop()
            if type(node) == type(0):
                ans.append(node)
            elif node.left:
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)
                stack.append(node.left)
            else:
                if node.right:
                    stack.append(node.right)
                ans.append(node.val)

        return ans
