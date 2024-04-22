# # Python String Data Type
# Python string is a sequence of one or more Unicode characters, 
# enclosed in single, double or triple quotation marks (also called inverted commas).
# Python strings are immutable which means when you perform an operation on strings, 
# you always produce a new string object of the same type, rather than mutating an existing string.
# As long as the same sequence of characters is enclosed, single or double or triple quotes don't 
# matter. Hence, following string representations are equivalent.

# # Example of String Data Type
str = 'Hello World!'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string