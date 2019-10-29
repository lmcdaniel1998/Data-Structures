
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''

        if Queue.is_full(self) is False:

            # create new node containing data
            temp = Node(item)
            temp.set_next(None)

            # check if item is the first item in queue
            if Queue.is_empty(self) is True:
                self.head = temp
                self.tail = temp
                self.num_items += 1

            else:
                self.tail.set_next(temp)
                self.tail = temp
                self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if Queue.is_empty(self) is False:

            item = self.head.item
            self.head = self.head.next
            self.num_items -= 1
            return item
        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
