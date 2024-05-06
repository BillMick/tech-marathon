# # Stacks 
print("""A stack is a linear data structure that stores items in a Last-In/First-Out
      (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added 
      at one end and an element is removed from that end only. """)

print("""The functions associated with stacks are :\n· empty() – Returns whether the stack is empty – Time Complexity: O(1)
\n· size() – Returns the size of the stack – Time Complexity: O(1)
\n· top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
\n· push(a) – Inserts the element at the top of the stack – Time Complexity: O(1)
\n· pop() – Deletes the topmost element of the stack – Time Complexity: O(1)""")

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