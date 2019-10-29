
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.front = 0
        self.rear = 0
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

            # check if item is first into queue
            if Queue.is_empty(self) is True:
                self.items[0] = item
                self.rear += 1
                self.num_items += 1

            else:
                if self.rear > self.capacity - 1:
                    self.rear -= self.capacity

                self.items[self.rear] = item
                self.rear += 1
                self.num_items += 1

        else:
            raise IndexError


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if Queue.is_empty(self) is False:

            my_first = self.front

            self.front += 1

            if self.front > self.capacity - 1:
                self.front -= self.capacity

            dequeue_val = self.items[my_first]
            self.items[my_first] = None
            self.num_items -= 1

            return dequeue_val

        else:
            raise IndexError

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
