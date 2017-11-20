# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = {}
        result = []
        def DFS(node, deep):
            if node is None:
                return deep
            levels.setdefault(deep, []).append(float(node.val))
            DFS(node.left, deep+1)
            DFS(node.right, deep+1)
        DFS(root, 0)
        deep = max(levels.keys())
        for i in range(deep+1):
            result.append(sum(levels[i]) / len(levels[i]))
        return result