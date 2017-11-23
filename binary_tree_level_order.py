# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        res = []
        temp = collections.deque([(root, 0)])
        def bfs():
            while temp:
                node, i = temp.popleft()
                if node:
                    if len(res) < i+1:
                        res.insert(0, [])
                    res[-i-1].append(node.val)
                    temp.append((node.left, i+1))
                    temp.append((node.right, i+1))

        bfs()
        return res
