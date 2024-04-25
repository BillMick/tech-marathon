# # if Statement
x,y =8, 8
if(x < y):
    st= "x is less than y"	
elif (x == y):
    st= "x is same as y"	
else:
    st="x is greater than y"
print(st)

# # How to execute conditional statement with minimal code (Ternary Operator)
# A If B else C
# <expr1> if <conditional_expr> else <expr2>
x,y = 1, 8
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(st)

# # One-Line if Statements
# if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
if 'f' in 'foo': print('1'); print('2'); print('3')
if 'z' in 'foo': print('1'); print('2'); print('3')

# # Switch Case Statement in Python
# What is Switch statement?
# A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case statements.
# Python language doesn’t have a switch statement.
# Python uses dictionary mapping to implement Switch Case in Python
argument = 1
switcher = {
    0: " This is Case Zero ",
    1: " This is Case One ",
    2: " This is Case Two ",
}
a = switcher.get(argument, "nothing")
print(a)

# # Using a lengthy if/elif/else series can be a little inelegant, especially when 
# the actions are simple statements like print(). In many cases, there may be a more 
# Pythonic way to accomplish the same thing.
# Here’s one possible alternative to the example above using the dict.get() method:
names = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))

# # The match case Statement
command = 'Hello, World!'
match command:
    case 'Hello, World!':
        print('Hello to you too!')
    case 'Goodbye, World!':
        print('See you later')
    case other:
        print('No match found')

match command.split():
    case ['show']:
        print('List all files and directories: ')
        # code to list files
    case ['remove', *files]:
        print('Removing files: {}'.format(files))
        # code to remove files
    case _:
        print('Command not recognized')