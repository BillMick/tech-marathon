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
