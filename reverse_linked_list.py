# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        haha
        """
        temp = None
        current_head = head
        while current_head != None:
            next_head = current_head.next
            current_head.next = temp
            temp = current_head
            current_head = next_head
        return temp

    