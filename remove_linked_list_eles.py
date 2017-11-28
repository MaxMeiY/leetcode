# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        new_head = head
        prev = None
        while head != None:
            if head.val == val:
                if prev == None:
                    head = head.next
                    new_head = head
                else:
                    prev.next = head.next
                    head = head.next
            else:
                prev = head
                head = head.next
        return new_head