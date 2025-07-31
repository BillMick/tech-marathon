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

""" A lambda expression has three parts: keyword (lambda), a bound variable 
(as argument) and a body (instructions). """
lambda x: x # identity function

# You can apply the function above to an argument by surrounding the function 
# and its argument with parentheses:
(lambda x: x*x)(7)

# Because a lambda function is an expression, it can be named:
sqrt_it = lambda x: x*x



