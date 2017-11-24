# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l2 == None else l2

        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1
        prev = None
        while l1 and l2:
            if l1.val <= l2.val:
                prev = l1
                l1 = l1.next
            else:
                temp = l2.next
                prev.next = l2
                l2.next = l1
                l2 = temp
                prev = prev.next
        if not l1:
            prev.next = l2
        return head
                