# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        original = sum
        def f(root, sum, tag):
            if root == None:
                return 0
            num = 1 if root.val == sum else 0
            if tag:
                return f(root.left, sum-root.val, True) + f(root.right, sum-root.val,True) + num
            else:
                return f(root.left, original,False) + f(root.right, original,False) + f(root.left, sum-root.val,True) + f(root.right, sum-root.val,True) + num
        return f(root, sum, False)

#--------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def path_from(root, sum):
            if root == None:
                return 0
            num = 1 if root.val == sum else 0
            return num + path_from(root.left, sum-root.val) + path_from(root.right, sum-root.val)

        if root == None:
            return 0
        return path_from(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)