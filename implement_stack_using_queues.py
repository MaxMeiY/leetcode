class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        empty = self.queue1 if not self.queue1 else self.queue2
        has_item = self.queue1 if self.queue1 else self.queue2
        while len(has_item) != 1:
            empty.append(has_item.pop(0))
        return has_item.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        empty = self.queue1 if not self.queue1 else self.queue2
        has_item = self.queue1 if self.queue1 else self.queue2
        while len(has_item) != 1:
            empty.append(has_item.pop(0))
        item = has_item.pop(0)
        empty.append(item)
        return item


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0 and len(self.queue2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()