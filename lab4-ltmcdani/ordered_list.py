class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    """A doubly-linked ordered list of integers, from lowest (head of list) to highest (tail of list)"""

    def __init__(self):
        """Use only a sentinel node
           ***No other instance variables***
           Do not have an attribute to keep track of size"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        """Returns back True if OrderedList is empty"""
        if (self.sentinel.next == self.sentinel) and (self.sentinel.prev == self.sentinel):
            return True
        else:
            return False

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           Can assume that item is not already in list (no duplicate items)"""
        new_node = Node(item)
        if self.sentinel.next == self.sentinel:
            self.sentinel.next = new_node
            self.sentinel.prev = new_node
            new_node.next = self.sentinel
            new_node.prev = self.sentinel

        else:
            current_node = self.sentinel
            while (current_node.next is not self.sentinel) and (current_node.next.item < new_node.item):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False"""
        if self.sentinel.next.item == item:         # checks if item is first in list
            self.sentinel.next = self.sentinel.next.next
            return True

        prev_node = self.sentinel
        current_node = prev_node.next

        while current_node.next is not self.sentinel:           # stops searching for value when end of list is reached
            if item == current_node.item:
                if current_node.next == self.sentinel:          # checks if item is last in list
                    prev_node.next = self.sentinel
                prev_node.next = current_node.next          # removes node and returns true
                current_node.next.prev = prev_node
                return True
            prev_node = current_node            # cycle through list
            current_node = current_node.next
        return False

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None"""
        current_node = self.sentinel.next
        return self.recursion_for_index(current_node, item, 0)

    def recursion_for_index(self, node, item, counter):
        if node == self.sentinel:
            return None
        elif node.item == item:
            return counter
        return self.recursion_for_index(node.next, item, counter + 1)

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError"""
        if (self.is_empty() is True) or (index < 0) or (index > self.size()):
            raise IndexError
        elif index == 0:
            pop_node = self.sentinel.next
            self.sentinel.next.next.prev = self.sentinel
            self.sentinel.next = self.sentinel.next.next
            return pop_node.item
        else:

            current_node = self.sentinel
            while (current_node.next is not self.sentinel) and (self.index(current_node) != index):
                current_node = current_node.next
            pop_node = current_node.item
            print(pop_node)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            return pop_node

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list"""

        current_node = self.sentinel.next
        return self.recursion_for_search(current_node, item)

    def recursion_for_search(self, current_node, item):
        if current_node == self.sentinel:
            return False
        elif current_node.item == item:
            return True
        else:
            return self.recursion_for_search(current_node.next, item)

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        if self.is_empty() is True:
            raise IndexError
        elif self.size() == 1:
            return [self.sentinel.next.item]

        python_list = []
        current_node = self.sentinel.next
        while current_node != self.sentinel:
            python_list.append(current_node.item)
            current_node = current_node.next
        return python_list

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list"""
        if self.is_empty() is True:
            raise IndexError

        reverse_list = []
        if self.sentinel.next == self.sentinel:
            return []
        elif self.sentinel.next.next == self.sentinel:
            reverse_list.append(self.sentinel.next.item)
            return reverse_list
        else:
            forward_list = self.python_list()
            current = len(forward_list) - 1
            return self.recursive_reverse(forward_list, current)

    def recursive_reverse(self, pythonlist, current_val):
        if current_val >= 0:
            return [pythonlist[current_val] + self.recursive_reverse(pythonlist[0:current_val], current_val)]

    def size(self):
        """Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list"""
        current_node = self.sentinel
        length = 0
        length += self.node_in_size(current_node)
        return length

    def node_in_size(self, current_node):
        if current_node.next == self.sentinel:
            return 0
        return 1 + self.node_in_size(current_node.next)
