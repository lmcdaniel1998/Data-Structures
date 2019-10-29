
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.capacity = capacity
        self.heap = [0] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        """inserts item into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full() is False:
            if self.is_empty() is True:
                self.heap[1] = item
                self.size += 1
                return True
            else:
                self.heap[self.size + 1] = item
                self.perc_up(self.size + 1)
                self.size += 1
                return True
        else:
            return False

    def peek(self):
        """returns max without changing the heap"""
        if self.is_empty() is False:
            return self.heap[1]
        else:
            return None

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property"""
        if self.is_empty() is False:
            max_heap = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap[self.size] = 0
            self.perc_down(1)
            self.size -= 1
            return max_heap
        else:
            return None

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap[1:self.size+1]

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        if len(alist) > self.capacity:
            self.capacity = len(alist)

        self.size = len(alist)              # update number of items in heap
        self.heap[1:self.size] = alist      # add alist to heap

        last_parent = self.size // 2
        while last_parent > 0:
            self.perc_down(last_parent)
            last_parent -= 1
        return True

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.size == self.capacity:
            return True
        else:
            return False

    def capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.capacity
    
    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

    def get_max_child(self, i):
        """Where the parameter i is an index in the heap
        finds the smallest child of the entry and returns its index in the heap."""
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i * 2 <= self.size:
            max_child = self.get_max_child(i)
            if self.heap[i] < self.heap[max_child]:
                temp = self.heap[i]
                self.heap[i] = self.heap[max_child]
                self.heap[max_child] = temp
            i = max_child
        
    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        sorted_list = []
        self.heap = [0] * self.capacity
        for item in alist:
            self.enqueue(item)
        for item in range(1, self.size + 1):
            sorted_list = [self.dequeue()] + sorted_list
        return sorted_list
