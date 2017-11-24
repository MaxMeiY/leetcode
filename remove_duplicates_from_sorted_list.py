# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        haha
        """
        if head == None or head.next == None:
            return head
        ans = head
        prev = head
        current = head.next
        while current != None:
            if prev.val == current.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head