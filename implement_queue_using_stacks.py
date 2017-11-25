class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0



class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inn = Stack()
        self.out = Stack()
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inn.push(x)
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.out.is_empty():
            while not self.inn.is_empty():
                self.out.push(self.inn.pop())
        return self.out.pop()
        
        
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.out.is_empty():
            return self.out.peek()
        while not self.inn.is_empty():
            self.out.push(self.inn.pop())
        return self.out.peek()
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.inn.is_empty() and self.out.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()