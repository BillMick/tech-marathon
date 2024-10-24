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

# # Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add < *, > before the arguments:
def my_function_5(*, x):
  print(x)
my_function_5(x = 3)
# my_function_5(3) # will generate error.

# # Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

# # Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself.
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into 
# writing a function which never terminates, or one that uses excess amounts of memory or processor
# power. However, when written correctly recursion can be a very efficient and mathematically-elegant 
# approach to programming.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

# # Python Function with Parameters
# If you have experience in C/C++ or Java then you must be thinking about the return type 
# of the function and data type of arguments. That is possible in Python as well 
# (specifically for Python 3.5 and above).
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
    return num3
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# # Docstring
# The first string after the function is called the Document string or Docstring
# in short. This is used to describe the functionality of the function. The use
# of docstring in functions is optional but it is considered a good practice.
# The below syntax can be used to print out the docstring of a function.
# Syntax: print(function_name.__doc__)
def evenOdd(x):
    """Function to check if the number is even or odd."""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
print(f"DocString : {evenOdd.__doc__}")

# Python Function within Functions
# A function that is defined inside another function is known as the inner function 
# or nested function. Nested functions can access variables of the enclosing scope. 
# Inner functions are used so that they can be protected from everything happening 
# outside the function.

# # Anonymous Functions in Python
# In Python, an anonymous function means that a function is without a name.
# As we already know the def keyword is used to define the normal functions and the 
# lambda keyword is used to create anonymous functions.
def cube(x): return x*x*x
cube_v2 = lambda x : x**3
print(cube(7))
print(cube_v2(7))

# # Pass by Reference and Pass by Value
# One important thing to note is, in Python every variable name is a reference.
# When we pass a variable to a function Python, a new reference to the object is created. 
def myFun(x):
    x[0] = 20
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# When we pass a reference and change the received reference to something else, the connection 
# between the passed and received parameters is broken. For example, consider the below program as follows:
def myFun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)