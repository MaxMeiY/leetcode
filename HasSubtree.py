'''
binary tree A, B, if A is part of B.
define: empty tree is never part of any tree
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def hasSubtree(self, A, B):
        if not A or not B:
            return False
        return self.is_sub(A,B) or self.hasSubtree(A,B.left) or self.hasSubtree(A,B.right)

    def is_sub(self, A, B):
        if not A:
            return True
        if not B or A.val != B.val:
            return False
        return self.is_sub(A.left, B.left) and self.is_sub(A.right, B.right)

