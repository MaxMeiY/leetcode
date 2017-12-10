# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = self.largestValues(root.left)
        right = self.largestValues(root.right)
        return [root.val] + list(map(max, left, right))

    def v2_largestValues(self,root):
        if root == None:
            return []

        ans = []
        rows = [root]
        while rows:
            ans.append(max(node.val for node in rows))
            rows = [kid for node in rows for kid in (node.lef, node.right) if kid]
        return ans
