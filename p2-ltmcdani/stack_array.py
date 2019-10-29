class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0

    def is_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if self.num_items == self.capacity:
            return True
        return False

    def push(self, item):
        """If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError"""
        if Stack.is_full(self) is not True:
            if Stack.is_empty(self) is True:
                self.items[0] = item
                self.num_items += 1

            else:
                self.items[self.size()] = item
                self.num_items += 1
        else:
            raise IndexError

    def pop(self):
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError"""
        if Stack.is_empty(self) is False:
            if Stack.size(self) == 1:
                pop_value = self.items[0]
                self.items[0] = None
                self.num_items = 0
            else:
                pop_value = self.items[self.size() - 1]
                self.items[self.size() - 1] = None
                self.num_items -= 1

            return pop_value
        else:
            raise IndexError

    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError"""
        if Stack.is_empty(self) is False:
            if Stack.size(self) == 1:
                peek_value = self.items[0]
            else:
                peek_value = self.items[self.size() - 1]

            return peek_value
        else:
            raise IndexError

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
