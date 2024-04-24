# # Errors and Exceptions¶
# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

# Syntax Errors¶
# Syntax errors, also known as parsing errors, are perhaps the most common kind
# of complaint you get while you are still learning Python

# Exceptions
# Errors detected during execution are called exceptions and are not unconditionally fatal.

# Python Built-in Exceptions
# We can view all the built-in exceptions using the built-in local() function as follows:
print(f"Python Built-in : {dir(locals()['__builtins__'])}")
# Here, locals()['__builtins__'] will return a module of built-in exceptions, functions,
# and attributes and dir allows us to list these attributes as strings.

