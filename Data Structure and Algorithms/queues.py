print("""queue is a linear data structure that stores items in a First In First
      Out (FIFO) manner. With a queue, the least recently added item is removed
      first.""")

print("""Operations associated with queue are: \n
· Enqueue: Adds an item to the queue. If the queue is full, then it is said 
to be an Overflow condition – Time Complexity : O(1)\n
· Dequeue: Removes an item from the queue. The items are popped in the same 
order in which they are pushed. If the queue is empty, then it is said to be
an Underflow condition – Time Complexity : O(1)\n
· Front: Get the front item from queue – Time Complexity : O(1)\n
· Rear: Get the last item from queue – Time Complexity : O(1)""")


# # Implementation using list
class Queue:
    stack = []
    
    def __init__(self, elements:list = []) -> None:
        print("Stack initializing.")
        self.stack = elements
    
    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False
    
    def size(self) -> int:
        return len(self.stack)
    
    def top(self) -> any:
        return self.stack[0] # first in.
    
    def bottom(self) -> any:
        return self.stack[-1] # last in.
    
    def push(self, element) -> any:
        self.stack.append(element)
        return self.stack
    
    def pop(self) -> any:
        self.stack.pop(0)
        return self.stack
    
    def display(self) -> None:
        print(self.stack)

my_stack = Queue()
print(my_stack)
print(my_stack.push('B'))
print(my_stack.push('I'))
print(my_stack.push('L'))
print(my_stack.push('M'))
print("Size: ", my_stack.size())
print("Is empty: ", my_stack.empty())
print(my_stack.pop())
print("Last element in (in the top): ", my_stack.top())
print("First element in (in the bottom): ", my_stack.bottom())

# # Implementation using collections.deque
print("""Queue in Python can be implemented using deque class from the
      collections module. Deque is preferred over list in the cases where
      we need quicker append and pop operations from both the ends of
      container, as deque provides an O(1) time complexity for append and
      pop operations as compared to list which provides O(n) time complexity.
      Instead of enqueue and deque, append() and popleft() functions are used.""")

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# # Implementation using queue.Queue
print("""Queue is built-in module of Python which is used to implement
      a queue. queue.Queue(maxsize) initializes a variable to a maximum
      size of maxsize. A maxsize of zero '0' means a infinite queue.
      This Queue follows FIFO rule.""")

from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
