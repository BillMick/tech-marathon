# # Arrays and Linked lists

# # Arrays
# Arrays store elements in contiguous memory locations, resulting in easily
# calculable addresses for the elements stored and this allows faster access 
# to an element at a specific index.
# As mentioned in the section above, arrays store only items that are of the 
# same single data type.
# Do not misunderstand arrays and lists. Lists store items that are of various data types. 
# Lists are built into the Python programming language, whereas arrays aren't. 
# Arrays are not a built-in data structure, and therefore need to be imported via the 
# array module in order to be used.
# They are also more compact and take up less memory and space which makes 
# them more size efficient compared to lists.
# To import : import array
# Syntax : variable_name = array(typecode,[elements])
import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers) # print the array
print(len(numbers)) # gets the length
print(numbers[1]) # gets the 2nd element
# With negative indexing, the last element would have an index of -1, the 
# second to last element would have an index of -2, and so on.
print(numbers[-1]) #gets last item

# # How to Search Through an Array in Python
#search for the index of the value 10
print(numbers.index(10))
# If there is more than one element with the same value, the index 
# of the first instance of the value will be returned
# How to Add a New Value to an Array
# To add one single value at the end of an array, use the append() method:
numbers.append(40)
print(numbers)
# Use the extend() method, which takes an iterable (such as a list of items)
# as an argument. Again, make sure that the new items are all the same data type.
numbers.extend([40,50,60])
print(numbers)
# And what if you don't want to add an item to the end of an array? Use the 
# insert() method, to add an item at a specific position.
numbers.insert(0, 17)
print(numbers)
# To remove an element from an array, use the remove() method and include the 
# value as an argument to the method. With remove(), only the first instance of
# the value you pass as an argument will be removed.
numbers.remove(40)
print(numbers)
# You can also use the pop() method, and specify the position of the element to be removed:
numbers.pop(0)
print(numbers)



# # Linked lists
# Linked lists are less rigid in their storage structure and elements are 
# usually not stored in contiguous locations, hence they need to be stored
# with additional tags giving a reference to the next element.
# Each element of a linked list is called a node, and every node has two different fields:
# * Data contains the value to be stored in the node.
# * Next contains a reference to the next node on the list.
# A linked list is a collection of nodes. The first node is called the head, 
# and it’s used as the starting point for any iteration through the list. 
# The last node must have its next reference pointing to None to determine the 
# end of the list.

# # Introducing collections.deque
# There’s a specific object in the collections module that you can use for linked lists called 
# deque (pronounced “deck”), which stands for double-ended queue.
# collections.deque uses an implementation of a linked list in which you can access, insert, or
# remove elements from the beginning or end of a list with constant O(1) performance.

# # How to Use collections.deque
print("How to Use collections.deque")
from collections import deque
list_1 = deque()
print(list_1)
# If you want to populate it at creation, then you can give it an iterable as input:
list_2 = deque(['1', '2', '3'])
print(list_2)
list_3 = deque('abc')
print(list_3)
list_4 = deque([{'data': 'a'}, {'data': 'b'}], maxlen = 10)
print(list_4)
print("Append '4' to list 2 :")
list_2.append('4')
print(list_2)
print("Pop '4' from list 2 :")
list_2.pop()
print(list_2)
# Both append() and pop() add or remove elements from the right side of the linked list.
# However, you can also use deque to quickly add or remove elements from the left side, 
# or head, of the list.
print("Append left '5' to list 2 :")
list_2.appendleft('5')
print(list_2)
print("Pop '5' from list 2 :")
list_2.popleft()
print(list_2)
print("Remove all elements from list 3.")
print(f"list_3 = {list_3}")
print(f"list_3 = {list_3.clear()}")
print("Extend the right side of the deque.")
list_2.extend(list_4)
print(list_2)
print("Extend the left side of the deque.")
list_2.extendleft(list_4)
print(list_2)
print("Remove the first occurrence of value. If not found, raises a ValueError.")
list_2.remove({'data': 'b'})
print(list_2)
print("Reverse the elements of the deque in-place and then return None.")
list_2.reverse()
print(list_2)
print("Rotate the deque n steps to the right. If n is negative, rotate to the left.")
print("When the deque is not empty, rotating one step to the right is equivalent to \nd.appendleft(d.pop()), and rotating one step to the left is equivalent to d.append(d.popleft())")
list_2.rotate(1)
print(list_2)
list_2.rotate(-1)
print(list_2)
print("Maximum size of a deque or None if unbounded.")
print(f"list_2 maxlen = {list_2.maxlen}")
print(f"list_4 maxlen = {list_4.maxlen}")
print("Count the number of deque elements equal to x.")
print(list_2.count('0'))

# # How to Implement Queues and Stacks
# Queues
# With queues, you want to add values to a list (enqueue), 
# and when the timing is right, you want to remove the element
# that has been on the list the longest (dequeue).
print('Queue concept : FIFO')
queue = deque()
queue.extend(['Michael', 'Mick', 'Mike'])
print(f"queue = {queue}")
print("Then, to mimic a real life queue, you should use 'popleft' and 'append'.")

# Stacks
# The only difference is that the stack uses the LIFO approach, meaning that
# the last element to be inserted in the stack should be the first to be removed.
print("Then, to mimic a real life stack, you should use 'pop' and 'append' OR 'popleft' and 'appendleft'.")

# # Implementing Your Own Linked List
print("\nImplementing Your Own Linked List.")
class Linked_List:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(element)
                node = node.next
        
    def __representation__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __representation__(self):
        return self.data

head_node = Node("first")
linked_list = Linked_List()
linked_list.head = head_node
print(linked_list.__representation__())
second_node = Node("second")
third_node = Node("third")
fourth_node = Node("fourth")
head_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
print(linked_list.__representation__())

print("Linked list creation more faster.")
linked_list_2 = Linked_List(queue)
print(linked_list_2)
