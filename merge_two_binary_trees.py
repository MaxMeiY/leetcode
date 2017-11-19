class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        haha
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        value = TreeNode(t1.val + t2.val)
        value.left = self.mergeTrees(t1.left, t2.left)
        value.right = self.mergeTrees(t1.right, t2.right)

        return value