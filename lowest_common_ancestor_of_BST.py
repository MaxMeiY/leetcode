# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestor_of_p = []
        ancestor_of_q = []
        def f(root, val, container):
            if root == None:
                return
            container.append(root)
            if root.val < val:
                return f(root.right, val, container)
            elif root.val > val:
                return f(root.left, val, container)
            else:
                return

        f(root, p.val, ancestor_of_p)
        f(root, q.val, ancestor_of_q)
        i = 0
        while i < len(ancestor_of_p) and i < len(ancestor_of_q):
            if ancestor_of_p[i] == ancestor_of_q[j]:
                res = ancestor_of_p[i]
                i += 1
            else:
                break
        return res

    def other(self, root, p, q):
        if root == None:
            return None
        if p.val > q.val: # make sure q.val > p.val
            p, q = q, p
        return self.helper(root, p, q)

    def helper(self, node, p, q):
        if node.val == p.val or node.val == q.val:
            return node
        if p.val < node.val and q.val > node.val:
            return node
        if p.val > node.val and q.val > node.val:
            return self.helper(node.left, p, q)
        return self.helper(node.right, p, q)