# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def f(l, r):
            if l > r:
                return None
            index, maximum = self.find_max(nums, l, r)
    
            node = TreeNode(maximum)
            node.left = f(l, index-1)
            node.right = f(index+1, r)
            return node
        return f(0, len(nums)-1)
        
        
    def find_max(self, nums, l, r):
        maximum = float('-inf')
        index = None
        for i in range(l, r+1):
            if nums[i] > maximum:
                maximum = nums[i]
                index = i
        return (index, maximum)
