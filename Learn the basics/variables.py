# # Memory Addresses
# Python's built-in id() function returns the address where the object is stored.
a = 17
print(f"ID of a = {id(a)}")
print(f"ID of 20 = {id(20)}")
# Once the data is stored in the memory, it should be accessed repeatedly for performing
# a certain process. Obviously, fetching the data from its ID is cumbersome. 
# High level languages like Python make it possible to give a suitable alias or a label 
# to refer to the memory location.
# Python uses the assignment operator (=) to bind an object with the label (named variable).

# # Deleting Python Variables
counter = 100
print(counter)
del counter
# print(counter) # will generate an error

# # Getting Type of a Variable
z =  10.10
print(f"z Type : {type(z)}")

# # Python Variables - Multiple Assignment
b = c = d = 3
print(f"b = {b}, c = {c}, d = {d}")
b = c = d = 3, 4, "Coq"
print(f"b = {b}, c = {c}, d = {d}")
print(f"b type = {type(b)}")
b, c, d = 3, 4, 5
print(f"b = {b}, c = {c}, d = {d}")

# # Python Local Variables
# Python Local Variables are defined inside a function. We can not access variable outside the function.

# # Python Global Variables
# Any variable created outside a function can be accessed within any function and so they have global scope.

# # Constants in Python
# Python doesn't have any formally defined constants, However you can indicate a variable to be treated 
# as a constant by using all-caps names with underscores. For example, the name PI_VALUE indicates that 
# you don't want the variable redefined or changed in any way.

# # Python vs C/C++ Variables
# The concept of variable works differently in Python than in C/C++. In C/C++, a variable is a named memory location. If a=10 and also b=10, both are two different memory locations. Let us assume their memory address is 100 and 200 respectively.
# If a different value is assigned to "a" - say 50, 10 in the address 100 is overwritten.
# A Python variable refers to the object and not the memory location. An object is stored in 
# memory only once. Multiple variables are really the multiple labels to the same object.
b = 3
print(f"id(b) = {id(b)}, id(c) = {id(c)}")
# The statement a=50 creates a new int object 50 in the memory at some other location, leaving the object 10 referred by "b".
# Further, if you assign some other value to b, the object 10 remains unreferred.
# Python's garbage collector mechanism releases the memory occupied by any unreferred object.

# Python's identity operator "is" returns True if both the operands have same id() value.
a = b = 10
print(f"a is b ?= {a is b}")

print(f"id(a) = {id(a)}, id(b) = {id(b)}")