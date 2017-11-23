# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def f(nums, start, end):
            if start > end:  # no equal
                return None
            mid = (end + start) // 2
            root = TreeNode(nums[mid])
            root.left = f(nums, start, mid-1)
            root.right = f(nums, mid+1, end)
            return root

        return f(nums, 0, len(nums)-1) # length - 1