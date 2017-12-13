# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = 0
        curr_node = root
        # calculate len of ListNode
        while curr_node != None:
            l, curr_node = l+1, curr_node.next

        chunk_size, num_longer_size = l // k, l % k
        # tow parts by more than 1 diff
        # why use chunk_size inside, see following
        res = [chunk_size+1]*num_longer_size + [chunk_size]*(k-num_longer_size)

        prev = None
        curr_node = root
        # Now you see why?
        for index, num_of_chunk_size_for_this_part in enumerate(res):
            # to escape root node
            if prev:
                prev.next = None
            res[index] = curr_node
            # skip the following part in chunk,
            # only include the head
            for i in range(num_of_chunk_size_for_this_part):
                prev, curr_node = curr_node, curr_node.next
        return res