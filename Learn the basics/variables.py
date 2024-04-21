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