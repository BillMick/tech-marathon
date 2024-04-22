# # Python String Data Type
# Python string is a sequence of one or more Unicode characters, 
# enclosed in single, double or triple quotation marks (also called inverted commas).
# Python strings are immutable which means when you perform an operation on strings, 
# you always produce a new string object of the same type, rather than mutating an existing string.
# As long as the same sequence of characters is enclosed, single or double or triple quotes don't 
# matter. Hence, following string representations are equivalent.

# # Example of String Data Type
str = 'Hello World! '
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 5)      # Prints string fives times
print (str + "TEST") # Prints concatenated string

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

