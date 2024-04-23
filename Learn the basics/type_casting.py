# # Python Implicit Casting
# In implicit type casting, a Python object with lesser byte size is upgraded
# to match the bigger byte size of other object in the operation. 
# For example, a Boolean object is first upgraded to int and then to float, 
# before the addition with a floating point object. In the following example, 
# we try to add a Boolean object in a float, pleae note that True is equal to 
# 1, and False is equal to 0.

a = True
b = 10.5
c = a + b
print (c)

# # Python Explicit Casting
# Although automatic or implicit casting is limited to int to float conversion,
# you can use Python's built-in functions int(), float() and str() to perform 
# the explicit conversions