# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        seen = [root]
        ans = []
        while seen:
            node = seen.pop()
            ans.append(node.val)
            if node.right:
                seen.append(node.right)
            if node.left:
                seen.append(node.left)
        return ans