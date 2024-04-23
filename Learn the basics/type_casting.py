# # Python Implicit Casting
# In implicit type casting, a Python object with lesser byte size is upgraded
# to match the bigger byte size of other object in the operation. 
# For example, a Boolean object is first upgraded to int and then to float, 
# before the addition with a floating point object. In the following example, 
# we try to add a Boolean object in a float, pleae note that True is equal to 
# 1, and False is equal to 0.
print("Python Implicit Casting")
a = True
b = 10.5
c = a + b
print (c)

# # Python Explicit Casting
# Although automatic or implicit casting is limited to int to float conversion,
# you can use Python's built-in functions int(), float() and str() to perform 
# the explicit conversions

# Binary String to Integer
# The string should be made up of 1 and 0 only, and the base should be 2.
a = int("110011", 2)
print("Binary String", f"a = {a}", sep="\n")

# Octal String to Integer
# The string should only contain 0 to 7 digits, and the base should be 8.
a = int("20", 8)
print("Octal String", f"a = {a}", sep="\n")

# Hexa-Decimal String to Integer
# The string should contain only the Hexadecimal symbols i.e., 0-9 and A, B, C, D, E or F.
# Base should be 16.
a = int("2A9", 16)
print("Hexa-Decimal String", f"a = {a}", sep="\n")

# # Conversion of Sequence Types
print("Conversion of Sequence Types")
a = [1,2,3,4,5]   # List Object
b = (1,2,3,4,5)   # Tupple Object
c = "Hello"       # String Object

### list() separates each character in the string and builds the list
obj = list(c)
print("list() separates each character in the string and builds the list", obj, sep="\n")

### The parentheses of tuple are replaced by square brackets.
obj=list(b)
print("The parentheses of tuple are replaced by square brackets.", obj, sep="\n")

### tuple() separates each character from string and builds a tuple of characters.
obj=tuple(c)
print("tuple() separates each character from string and builds a tuple of characters.", obj, sep="\n")

### square brackets of list are replaced by parentheses.
obj=tuple(a)
print("square brackets of list are replaced by parentheses.", obj, sep="\n")

### str() function puts the list and tuple inside the quote symbols.
obj=str(a)
print("str() function puts the list inside the quote symbols.", type(obj), sep="\n")

obj=str(b)
print("str() function puts the tuple inside the quote symbols.", type(obj), sep="\n")
