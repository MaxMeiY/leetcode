# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = []
        s2 = []
        h1 = l1
        h2 = l2
        while h1:
            s1.append(str(h1.val))
            h1 = h1.next
        while h2:
            s2.append(str(h2.val))
            h2 = h2.next
        s = str(int(''.join(s1)) + int(''.join(s2)))
        def f(string):
            if not string:
                return None
            head = ListNode(int(string[0]))
            head.next = f(string[1:])
            return head
        return f(s)
