'''
This is correct. just for coding and testing.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def has_left(self):
        return self.left != None

    def has_right(self):
        return self.right != None
    def has_child(self):
        return self.has_left() or self.has_right()


def solution(t):
    if t is None:
        print('()',end='')
        return
    print(t.val,end='')
    if t.has_left():
        print('(', end='')
        solution(t.left)
        print(')', end='')
    if t.has_right():
        if not t.has_left():
            print('()', end='')
        print('(', end='')
        solution(t.right)
        print(')', end='')

if __name__ == '__main__':
    t = Node(1)
    t.left = Node(2)
    t.left.left = Node(4)
    t.right = Node(3)
    s = Node(1)
    s.left = Node(2)
    s.right = Node(3)
    s.left.right = Node(4)
'''

#-------------Answer here---------------------
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        res = []
        def f(t):
            if t == None:
                return
            res.append(str(t.val))
            if t.left != None:
                res.append('(')
                f(t.left)
                res.append(')')
            if t.right != None:
                if t.left == None:
                    res.append('()')
                res.append('(')
                f(t.right)
                res.append(')')
            return res
        result_str = f(t)
        print(result_str)
        if result_str == None:
            return ''
        return ''.join(result_str)
