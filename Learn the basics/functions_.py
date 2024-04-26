# # Functions – How to Define and Call a Function
def PowNum(num1):
    return pow(num1, 8)

result = PowNum(8)
print(result)

# # Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function_1(*kids):
  print("The youngest child is " + kids[2])

my_function_1("Emil", "Tobias", "Linus")

# # Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function_2(child3, child2, child1):
  print("The youngest child is " + child3)

my_function_2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# # Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function_3(**kid):
  print("His last name is " + kid["lname"])

my_function_3(fname = "Tobias", lname = "Refsnes")

# # Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value

# # The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition
# with no content, put in the pass statement to avoid getting an error.

# # Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add < , / > after the arguments:
def my_function_4(x, /):
  print(x)

my_function_4(3)
# my_function_4(x = 3) # will generate error.

