# # Stacks 
print("""A stack is a linear data structure that stores items in a Last-In/First-Out
      (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added 
      at one end and an element is removed from that end only. """)

print("""The functions associated with stacks are :\n· empty() – Returns whether the stack is empty – Time Complexity: O(1)
\n· size() – Returns the size of the stack – Time Complexity: O(1)
\n· top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
\n· push(a) – Inserts the element at the top of the stack – Time Complexity: O(1)
\n· pop() – Deletes the topmost element of the stack – Time Complexity: O(1)""")

print("""Advantages of Stack:\n
· Stacks are simple data structures with a well-defined set of operations, 
which makes them easy to understand and use.\n
· Stacks are efficient for adding and removing elements, as these operations 
have a time complexity of O(1).\n
· In order to reverse the order of elements we use the stack data structure.\n
· Stacks can be used to implement undo/redo functions in applications.""")

print("""Drawbacks of Stack:\n
· Restriction of size in Stack is a drawback and if they are full, you cannot 
add any more elements to the stack.\n
· Stacks do not provide fast access to elements other than the top element.\n
· Stacks do not support efficient searching, as you have to pop elements one 
by one until you find the element you are looking for.""")

# # Implementation using list
class Stack:
    stack = []
    
    def __init__(self, elements:list = []) -> None:
        print("Stack initializing.")
        self.stack = elements
    
    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False
    
    def size(self) -> int:
        return len(self.stack)
    
    def top(self) -> any:
        return self.stack[-1]
    
    def bottom(self) -> any:
        return self.stack[0]
    
    def push(self, element) -> any:
        self.stack.append(element)
        return self.stack
    
    def pop(self) -> any:
        self.stack.pop()
        return self.stack
    
    def display(self) -> None:
        print(self.stack)

my_stack = Stack()
print(my_stack)
print(my_stack.push('B'))
print(my_stack.push('I'))
print(my_stack.push('L'))
print(my_stack.push('M'))
print("Size: ", my_stack.size())
print("Is empty: ", my_stack.empty())
print(my_stack.pop())
print("Last element (in the top): ", my_stack.top())
print("First element (in the bottom): ", my_stack.bottom())

# # Implementation using deque
print("""Python stack can be implemented using the deque class from the 
      collections module. Deque is preferred over the list in the cases 
      where we need quicker append and pop operations from both the ends of
      the container, as deque provides an O(1) time complexity for append 
      and pop operations as compared to list which provides O(n) time
      complexity. """)

class StackDeque:
    
    stack = None
    
    def __init__(self) -> None:
        from collections import deque
        print("Initializing...")
        self.stack = deque()
        print(self.stack)
    
    def push(self, element):
        self.stack.append(element)
        return self.stack
    
    def pop(self):
        self.stack.pop()
        return self.stack

my_deque_stack = StackDeque()
my_deque_stack.push(element='a')
my_deque_stack.push('b')
my_deque_stack.push('c')
print('Initial stack:')
print(my_deque_stack.stack)
print('\nElements popped from stack:')
print(my_deque_stack.pop())
print(my_deque_stack.pop())
print(my_deque_stack.pop())
print('\nStack after elements are popped:')
print(my_deque_stack.stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


# Python program to
# demonstrate stack implementation
# using queue module

# # Implementation using queue module
print("""Queue module also has a LIFO Queue, which is basically a Stack.
      Data is inserted into Queue using the put() function and get() takes 
      data out from the Queue.""")

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

