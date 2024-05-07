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
        return self.stack[0]
    
    def bottom(self) -> any:
        return self.stack[-1]
    
    def push(self, element) -> any:
        self.stack.append(element)
        return self.stack
    
    def pop(self) -> any:
        self.stack.pop()
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
print("Last element (in the top): ", my_stack.top())
print("First element (in the bottom): ", my_stack.bottom())

print("""""")

print("""""")

print("""""")

print("""""")

print("""""")