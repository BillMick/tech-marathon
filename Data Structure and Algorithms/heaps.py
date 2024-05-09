# # Heaps 
print("""The purpose of a min-heap is to store objects that have a partial
      order on them. It has a fast (O(log n)) method for removing the 
      minimum object from the heap. Min-heaps are useful for calculations 
      where you have multiple minimum computations to perform.\nThere is 
      an analogous structure called a max-heap, which extracts the maximum 
      value from the heap.\nA heap is either a max-heap or a min-heap - 
      it can't be both. Given an implementation of a min-heap, a max-heap 
      can be implemented by reversing the comparison between elements.\n""")

print("""Crucial Terms\n· key: The values that determine the order. The key 
      is the data field that we're comparing by.\n· extract_min: The method 
      of (quickly) being able to extract the minimum element from the min-heap.\n""")

print("""Strengths and Weaknesses\n· Strengths : a min-heap is able to quickly 
      extract the minimum value on the heap. Repeated extractions from a 
      min-heap into an array will yield a sorted array.\n· Weaknesses: There's 
      no convenient way of searching for a particular key value in a heap. 
      Entries are only partially ordered; clever use of the heap property can
      allow for some pruning of searches.\n""")

print("""In Interviews, Use Heaps When ...\nHeaps are designed to do one specific
      thing well, so the answer to when you should use a heap is repetitive: 
      You use one when you have to do repeated minimum (or maximum) extractions.\n
      Examples of usage:\n
      · Finding the minimum distance between two nodes in a 
      graph: the standard approach to this problem is to use Dijkstra's algorithm.
      One of the key steps in Dijkstra's algorithm is to select the node closest 
      to a node that you have already completed, which is a minimum calculation.\n
      · Getting the next event that is scheduled to occur: storing events in a 
      heap with a timestamp as the key gives you a fast way to extract the 
      next event (the event with the smallest timestamp will occur next).\n
      · Keep track of the median value while streaming: this is the running 
      median problem, where two heaps are maintained: a max-heap for values
      below the current median and a min-heap for values above the current 
      median. When a new value is inserted, it is placed in the low or high 
      pile as appropriate (and the maximum of the low values or minimum of
      the low values are extracted as necessary to keep the two heaps 
      sizes' different by at most one element).\n
      · Find the first k non-repeating characters in a string in a single 
      traversal.""")

print("""There are other ways of constructing heaps (such as binomial 
      heaps and Fibonacci heaps) that can improve the asymptotic run time 
      slightly, but that support the same operations.""")

"""
Min Heap Implementation in Python
"""
class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        Stop = False
        while (i // 2 > 0) and Stop == False:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                Stop = True
            # Move the index to the parent to keep the properties
            i = i // 2
 
    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]
 
        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]
 
        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list
 
        # Decrease the size of the heap
        self.current_size -= 1
 
        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)
 
        # Return the min value of the heap
        return root
"""
Driver program
"""
# Same tree as above example.
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(9)
my_heap.insert(13)
my_heap.insert(11)
my_heap.insert(10)

print(my_heap.delete_min()) # removing min node i.e 5 
print(my_heap.heap_list)

 