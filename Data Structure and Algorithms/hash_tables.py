print("""Hash Table, Map, HashMap, Dictionary or Associative are all the names
      of the same data structure. It is a data structure that implements a 
      set abstract data type, a structure that can map keys to values.""")

print("""In computer science, a Hash table or a Hashmap is a type of data
      structure that maps keys to its value pairs (implement abstract array
      data types). It basically makes use of a function that computes an
      index value that in turn holds the elements to be searched, inserted,
      removed, etc. This makes it easy and fast to access data. In general,
      hash tables store key-value pairs and the key is generated using a 
      hash function.""")

print('Hash Table                  Vs    Hashmap')
print('Synchronized                ->    Non-Synchronized')
print('Fast                        ->    Slow')
print('Allows one null key and           Does not allows null')
print('more than one null values   ->    keys or values')

print("""Accessing Values:
The values of a dictionary can be accessed in many ways such as:\n
· Using key values\n
· Using functions\n
· Implementing the for loop""")
my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
print(f"Using key values: {my_dict['Dave']}")
print("""Using functions: There are a number of built-in 
      functions that can be used such as get(), keys(), values(), etc.""")
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('Dave'))

print("""Implementing the for loop: The for loop allows you to access the 
      key-value pairs of a dictionary easily by iterating over them.""")
print("All keys")
for x in my_dict:
    print(x)       #prints the keys
print("All values")
for x in my_dict.values():
    print(x)       #prints values
print("All keys and values")
for x,y in my_dict.items():
    print(x, ":" , y)       #prints keys and values


print("""Deleting items from a dictionary:\n
There a number of functions that allow you to delete items from a dictionary
such as del(), pop(), popitem(), clear(), etc.""")
my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
del my_dict['Dave']  #removes key-value pair of 'Dave'
my_dict.pop('Ava')   #removes the value of 'Ava'
my_dict.popitem()    #removes the last inserted item
print(my_dict)

print("Converting Dictionary into a dataframe.")
import pandas as pd
emp_details = {'Employee': {'Dave': {'ID': '001',
                                     'Salary': 2000,
                                     'Designation':'Python Developer'},
                            'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                            'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}
df = pd.DataFrame(emp_details['Employee'])
print("####################################################################")
print(df)
print("####################################################################")
# import string
# print(string.ascii_letters)

print('Understand the Hash Function.')
