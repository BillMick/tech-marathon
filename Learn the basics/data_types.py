# # Python String Data Type
# Python string is a sequence of one or more Unicode characters, 
# enclosed in single, double or triple quotation marks (also called inverted commas).
# Python strings are immutable which means when you perform an operation on strings, 
# you always produce a new string object of the same type, rather than mutating an existing string.
# As long as the same sequence of characters is enclosed, single or double or triple quotes don't 
# matter. Hence, following string representations are equivalent.

# # Example of String Data Type
str_chain = 'Hello World! '
print (str_chain)          # Prints complete string
print (str_chain[0])       # Prints first character of the string
print (str_chain[2:5])     # Prints characters starting from 3rd to 5th
print (str_chain[2:])      # Prints string starting from 3rd character
print (str_chain * 5)      # Prints string fives times
print (str_chain + "TEST") # Prints concatenated string

# # Python List Data Type
# An item in the list may be of any data type. It means that a list object 
# can also be an item in another list. In that case, it becomes a nested list.
nested_list = [['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]
print(f"nested_list = {nested_list}")

# # Example of List Data Type
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)            # Prints complete list
print(list[0])         # Prints first element of the list
print(list[1:3])       # Prints elements starting from 2nd till 3rd 
print(list[2:])        # Prints elements starting from 3rd element
print(tinylist * 2)    # Prints list two times
print(list + tinylist) # Prints concatenated lists

# # Python Tuple Data Type
# To form a tuple, use of parentheses is optional. Data items 
# separated by comma without any enclosing symbols are treated as a tuple by default.
test = 15, 17, "a"
print(f"test_type = {type(test)}")

# List are mutable and Tuple are not (Tuples can be thought of as read-only lists).

# # Python Range Data Type
# A Python range is an immutable sequence of numbers which is typically used to iterate
# through a specific number of items.
# range(start, stop, step)

# # Python Binary Sequence Data Types
# Python provides three different ways to represent binary data. They are as follows −
# bytes, bytearray, memoryview

# # Python Bytes Data Type
# We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b.
b1 = bytes([65, 66, 67, 68, 69])  
print(b1, type(b1))  
b2 = b'Hello'
print(b2, type(b2))

# # Python Bytearray Data Type
# The bytearray data type in Python is quite similar to the bytes data type, but with
# one key difference: it is mutable, meaning you can modify the values stored in it after it is created.
# You can create a bytearray using various methods, including by passing an iterable of integers representing
# byte values, by encoding a string, or by converting an existing bytes or bytearray object.
value1 = bytearray([72, 101, 108, 108, 111])
print(value1, type(value1))
value2 = bytearray("Hello", 'utf-8')
print(value2, type(value2))

# # Python Memoryview Data Type
# In Python, a memoryview is a built-in object that provides a view into the memory of the original object,
# generally objects that support the buffer protocol, such as byte arrays (bytearray) and bytes (bytes).
# It allows you to access the underlying data of the original object without copying it, providing efficient
# memory access for large datasets.
# You can create a memoryview using various methods. These methods include using the memoryview() constructor,
# slicing bytes or bytearray objects, extracting from array objects, or using built-in functions like open()
# when reading from files.
# The supported objects generally include byte arrays (bytearray), bytes (bytes), and other objects that
# support the buffer protocol −
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)
# If you have an array object, you can create a memoryview using the buffer interface as shown below.
import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

# # Example of Dictionary Data Type
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# # Python Set Data Type
# Set is a Python implementation of set as defined in Mathematics. A set in Python is a collection,
# but is not an indexed or ordered collection as string, list or tuple. An object cannot appear more
# than once in a set, whereas in List and Tuple, same object can appear more than once.
# Comma separated items in a set are put inside curly brackets or braces {}. Items in the set
# collection can be of different data types.
# Note that items in the set collection may not follow the same order in which they are entered.
# The position of items is optimized by Python to perform operations over set as defined in mathematics.
set_variable = {2023, "Python", 3.11, 5+6j, 1.23E-4}
print(set_variable, type(set_variable))
# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
# If you try to put a list or a dictionary in the set collection, Python raises a TypeError.
# Hashing is a mechanism in computer science which enables quicker searching of objects in computer's
# memory. Only immutable objects are hashable.
# Even if a set doesn't allow mutable items, the set itself is mutable. Hence, add/delete/update 
# operations are permitted on a set object, using the methods in built-in set class. Python also
# has a set of operators to perform set manipulation.

# # Example of Boolean Data Type
# Returns false as a is not equal to b
a, b = 2, 4
print(bool(a==b))
# Following also prints the same
print(a==b)
# Returns False as a is None
a = None
print(bool(a))
# Returns false as a is an empty sequence
a = ()
print(bool(a))
# Returns false as a is 0
a = 0.0
print(bool(a))
# Returns true
a = 10
print(bool(a))

# # Python Data Type Conversion
# To convert data between different Python data types, you simply use the type name as a function.
print("Conversion to integer data type")
a, b, c = int(1), int(2.2), int(float("3.3")) # a will be 1 # b will be 2 # c will be 3 but convert it to float first
print (a, b, c)
print("Conversion to floating point number")
a, b, c = float(1), float(2.2), float("3.3") # c will be 3.3 # b will be 2.2 # a will be 1.0
print (a, b, c)
print("Conversion to string")
a, b, c = str(1), str(2.2), str("3.3") # c will be "3.3"# b will be "2.2" # a will be "1" 
print (a, b, c)

