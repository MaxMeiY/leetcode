# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mapping = {}
        def f(node):
            if node == None:
                return 0
            left = f(node.left)
            right = f(node.right)
            sum_val = node.val + left + right
            mapping[sum_val] = mapping.get(sum_val, 0) + 1
            return sum_val
        f(root)
        if len(mapping) == 0:
            return []
        frequent = max(mapping.values())
        return [x for x in mapping if mapping[x] == frequent]