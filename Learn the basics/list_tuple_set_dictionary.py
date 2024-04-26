# Lists
l = []
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Set
s = set() 
# Adding element into set
s.add(5)
s.add(10)
print("Adding 5 and 10 in set", s)
# Removing element from set
s.remove(5)
print("Removing 5 from set", s)
print()

# Tuple
t = tuple(l) 
# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
d = {} 
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
# Removing key-value pair
del d[10]
print("Dictionary", d)

# 
# It depends on what you are intending to do with it.

# Sets are significantly faster when it comes to determining if an object is present 
# in the set (as in x in s), but its elements are not ordered so you cannot access 
# items by index as you would in a list. Sets are also somewhat slower to iterate 
# over in practice.
# You can use the timeit module to see which is faster for your situation.
# Iterating #
#####################################################################################################################
# def iter_test(iterable):
#     for i in iterable:
#         pass
# from timeit import timeit
# for_set = timeit(
#     "iter_test(iterable)",
#     setup="from __main__ import iter_test; iterable = set(range(10000))",
#     number=100000)
# for_list = timeit(
#     "iter_test(iterable)",
#     setup="from __main__ import iter_test; iterable = list(range(10000))",
#     number=100000)
# for_tuple = timeit(
#     "iter_test(iterable)",
#     setup="from __main__ import iter_test; iterable = tuple(range(10000))",
#     number=100000)
# print("### Iterating ###", f"for_set = {for_set}", f"for_list = {for_list}", f"for_tuple = {for_tuple}", sep = "\n")
#####################################################################################################################

# Determine if an object is present #
#####################################################################################################################
# def in_test(iterable):
#     for i in range(1000):
#         if i in iterable:
#             pass
# for_set = timeit(
#     "in_test(iterable)",
#     setup="from __main__ import in_test; iterable = set(range(1000))",
#     number=10000)
# for_list = timeit(
#     "in_test(iterable)",
#     setup="from __main__ import in_test; iterable = list(range(1000))",
#     number=10000)
# for_tuple = timeit(
#     "in_test(iterable)",
#     setup="from __main__ import in_test; iterable = tuple(range(1000))",
#     number=10000)
# print("### Iterating ###", f"for_set = {for_set}", f"for_list = {for_list}", f"for_tuple = {for_tuple}", sep = "\n")
#####################################################################################################################

# # Print list in column format
#Import the Pandas framework, defined as pd
import pandas as pd
 
#Define our color variable as a list
color = ['blue','green','red','yellow']
#Define our fruit variable as a list
fruit = ['blueberry','apple','cherry','banana']
 
#Define the df variable as formatted columns for color and fruit
df=pd.DataFrame(columns=['color', 'fruit'])
#Label our columns as color and fruit
df['color'],df['fruit']=color,fruit
 
#Print everything
print(df)