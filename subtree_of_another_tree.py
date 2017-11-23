# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def find_node(s, t):
            if s == None:
                return False
            if s.val == t.val and compare(s, t):
                return True
            return find_node(s.left,t) or find_node(s.right, t)

        def compare(subtree, t):
            if subtree == None and t == None:
                return True
            if subtree == None or t == None:
                return False
            if subtree.val != t.val:
                return False
            return compare(subtree.left, t.left) and compare(subtree.right, t.right)

        return find_node(s, t)