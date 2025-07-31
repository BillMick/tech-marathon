""" Lambda Calculus (https://realpython.com/python-lambda/)
Lambda expressions in Python and other programming languages have their roots in 
lambda calculus, a model of computation invented by Alonzo Church. """

""" Lambda calculus can encode any computation. It is Turing complete, but contrary
to the concept of a Turing machine, it is pure and does not keep any state. """

""" The imperative style consists of programming with statements, driving the flow 
of the program step by step with detailed instructions. This approach promotes 
mutation and requires managing state. """

""" The separation in both families presents some nuances, as some functional 
languages incorporate imperative features, like OCaml, while functional features 
have been permeating the imperative family of languages in particular with the 
introduction of lambda functions in Java, or Python.

Python is not inherently a functional language, but it adopted some functional 
concepts early on. In January 1994, map(), filter(), reduce(), and the lambda 
operator were added to the language. """

# A lambda expression has three parts: keyword (lambda), a bound variable 
# (as argument) and a body (instructions).
lambda x: x # identity function

# You can apply the function above to an argument by surrounding the function 
# and its argument with parentheses:
(lambda x: x*x)(7)

# Because a lambda function is an expression, it can be named:
sqrt_it = lambda x: x*x
print(f"8 au carré = {sqrt_it(8)}")

# Multi-argument functions (functions that take more than one argument) are 
# expressed in Python lambdas by listing arguments and separating them with 
# a comma (,) but without surrounding them with parentheses:
fullname = lambda first, last: f"Full name: {first.title()} {last.title()}"
print("Full Name:", fullname('Bill', 'Mick'))

""" Anonymous Functions """
""" Taken literally, an anonymous function is a function without a name. In Python, 
an anonymous function is created with the lambda keyword. More loosely, it may or 
not be assigned a name. """

# lambda x, y: x + y
# Other than providing you with the feedback that Python is perfectly fine with this 
# form, it doesn’t lead to any practical use. You could invoke the function in the 
# Python interpreter:
# _(1, 2)
""" The example commented above is taking advantage of the interactive interpreter-only feature provided via the underscore (_)
https://dbader.org/blog/meaning-of-underscores-in-python """

# Another pattern used in other languages like JavaScript is to immediately execute 
# a Python lambda function. This is known as an Immediately Invoked Function 
# Expression (IIFE, pronounce “iffy”). Here’s an example:
(lambda x, y: x + y) (7, 8)
""" Python does not encourage using immediately invoked lambda expressions. It 
simply results from a lambda expression being callable, unlike the body of a 
normal function. """

""" Lambda functions are frequently used with higher-order functions, which take one 
or more functions as arguments or return one or more functions.
A lambda function can be a higher-order function by taking a function (normal or 
lambda) as an argument like in the following contrived example: """
high_ord_func = lambda x, func: x + func(x)
print(f"HOF: {high_ord_func(2, lambda x: x * x)}")
