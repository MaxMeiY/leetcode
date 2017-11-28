# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        stack = [head.val]
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        to_pop = True if fast.next == None else False
        if to_pop:
            stack.pop()
        slow = slow.next
        i = -1
        while slow != None:
            if stack[i] != slow.val:
                return False
            slow = slow.next
            i -= 1

        return True
