# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        val = []
        def preorder(node):
            if node:
                val.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return self.build_tree(preorder, inorder)

    def build_tree(self, preorder, inorder):
        def build(node,inorder):
            if node:
                root = TreeNode(node[0])
                index = inorder.index(node[0])
                root.left = build(node[1:index+1],inorder[:index])
                root.right = build(node[index+1:],inorder[index+1:])
                return root
        return build(preorder,inorder)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))