# # Errors and Exceptions¶
# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

# Syntax Errors¶
# Syntax errors, also known as parsing errors, are perhaps the most common kind
# of complaint you get while you are still learning Python

# Exceptions
# Errors detected during execution are called exceptions and are not unconditionally fatal.

# Python Built-in Exceptions
# We can view all the built-in exceptions using the built-in local() function as follows:
####################################################################
# print(f"Python Built-in : {dir(locals()['__builtins__'])}")
####################################################################
# Here, locals()['__builtins__'] will return a module of built-in exceptions, functions,
# and attributes and dir allows us to list these attributes as strings.

# # Catching Specific Exceptions in Python
# For each try block, there can be zero or more except blocks.
# Multiple except blocks allow us to handle each exception differently.
# The argument type of each except block indicates the type of exception that can be handled by it.
####################################################################
# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except ZeroDivisionError:
#     print("Denominator cannot be 0.")
# except IndexError:
#     print("Index Out of Bound, right ?")
####################################################################

# # Python try with else clause
# In some situations, we might want to run a certain block of code if the code block
# inside try runs without any errors.
# For these cases, you can use the optional else keyword with the try statement.
####################################################################
# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(f"reciprocal = {reciprocal}")
####################################################################
# Here, the assert statement in the code checks that num is an even number;
# if num is odd, it raises an AssertionError, triggering the except block.
# Note: Exceptions in the else clause are not handled by the preceding except clauses.

# # Python try...finally
# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.
####################################################################
# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator

#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")
    
# finally:
#     print("This is finally block.")
####################################################################"
    
# # Defining Custom Exceptions
# In Python, we can define custom exceptions by creating a new class that
# is derived from the built-in Exception class.
####################################################################""
# class CustomError(Exception):
#     ...
#     pass

# try:
#    ...

# except CustomError:
#     ...
####################################################################

# Example: Python User-Defined Exception
####################################################################
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass
# # you need to guess this number
# number = 18
# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age. Number not guessed.")
####################################################################

# # Customizing Exception Classes
# We can further customize this class to accept other arguments as per our needs.
# To learn about customizing the Exception classes, you need to have the basic 
# knowledge of Object-Oriented programming.
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message = "Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# Here, we have overridden the constructor of the Exception class to accept 
# our own custom arguments salary and message.
# Then, the constructor of the parent Exception class is called manually 
# with the self.message argument using super().
# The custom self.salary attribute is defined to be used later.
# The inherited __str__ method of the Exception class is then used to 
# display the corresponding message when SalaryNotInRangeError is raised.
