# # if Statement
x,y =8, 8
if(x < y):
    st= "x is less than y"	
elif (x == y):
    st= "x is same as y"	
else:
    st="x is greater than y"
print(st)

# # How to execute conditional statement with minimal code
# A If B else C
x,y = 1, 8
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(st)
