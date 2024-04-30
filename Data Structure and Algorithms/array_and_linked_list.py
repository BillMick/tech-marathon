# # Arrays and Linked lists

# # Arrays
# Arrays store elements in contiguous memory locations, resulting in easily
# calculable addresses for the elements stored and this allows faster access 
# to an element at a specific index.
# As mentioned in the section above, arrays store only items that are of the 
# same single data type.
# Do not misunderstand arrays and lists. Lists store items that are of various data types. 
# Lists are built into the Python programming language, whereas arrays aren't. 
# Arrays are not a built-in data structure, and therefore need to be imported via the 
# array module in order to be used.
# They are also more compact and take up less memory and space which makes 
# them more size efficient compared to lists.
# To import : import array
# Syntax : variable_name = array(typecode,[elements])
import array as arr 
numbers = arr.array('i',[10,20,30])
print(numbers)
print(len(numbers)) # gets the length
print(numbers[1]) # gets the 2nd element

# # Linked lists
# Linked lists are less rigid in their storage structure and elements are 
# usually not stored in contiguous locations, hence they need to be stored
# with additional tags giving a reference to the next element. 