# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'----------------recursion-----------------'
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            t = TreeNode(v)
            t.left = root
            return t
        self.f(root, 1, v, d)
        return root
    
    def f(self, root, cur, v, d):
        if root == None:
            return None
        if cur == d -1:
            temp_left = root.left
            root.left = TreeNode(v)
            root.left.left = temp_left
            temp_right = root.right
            root.right = TreeNode(v)
            root.right.right = temp_right
        else:
            self.f(root.left, cur+1, v, d)
            self.f(root.right, cur+1, v, d)
    
'-------------------end------------------------'

class Solution2:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            t = TreeNode(v)
            t.left = root
            return t
        rows = [root]
        cur = 1
        while rows:
            if cur == d - 1:
                for node in rows:
                    temp_left = node.left
                    temp_right = node.right
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = temp_left
                    node.right.right = temp_right
                break
            temp = []
            for node in rows:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            cur += 1
            rows = temp
        return root