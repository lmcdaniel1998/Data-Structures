class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Linked List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.head is None:
            return True
        return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if self.size() == self.capacity:
            return True
        return False

    def push(self, item):
        """If stack is not full, pushes item on stack.
        If stack is full when push is attempted, raises IndexError"""
        if self.is_full() is False:
            temp = Node(item)
            temp.next = self.head
            self.head = temp
            self.num_items += 1
        else:
            raise IndexError

    def pop(self):
        """If stack is not empty, pops item from stack and returns item.
        If stack is empty when pop is attempted, raises IndexError"""
        if self.is_empty() is False:
            pop_item = self.head
            self.head = pop_item.next
            pop_item.next = None
            self.num_items -= 1
            return pop_item.data

        else:
            raise IndexError

    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
        If stack is empty, raises IndexError"""
        if self.is_empty() is False:
            pop_item = self.head
            return pop_item.data
        else:
            raise IndexError

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
        '''current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count'''


