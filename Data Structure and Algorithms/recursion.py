print("""The process in which a function calls itself directly or indirectly is called 
recursion and the corresponding function is called a recursive function. Using 
a recursive algorithm, certain problems can be solved quite easily. Examples of
such problems are Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, 
DFS of Graph, etc. A recursive function solves a particular problem by calling a 
copy of itself and solving smaller subproblems of the original problems. Many
more recursive calls can be generated as and when required. It is essential to know
that we should provide a certain case in order to terminate this recursion process.
So we can say that every time the function calls itself with a simpler version of 
the original problem.""")

print("""How are recursive functions stored in memory?
Recursion uses more memory, because the recursive function adds to the stack with
each recursive call, and keeps the values there until the call is finished. The 
recursive function uses LIFO (LAST IN FIRST OUT) Structure just like the stack data
structure.""")

print("""What is the base condition in recursion? 
In the recursive program, the solution to the base case is provided and the solution
to the bigger problem is expressed in terms of smaller problems. """)

print("""Why Stack Overflow error occurs in recursion? 
If the base case is not reached or not defined, then the stack overflow problem may 
arise. Let us take an example to understand this.""")

print("""What is the difference between direct and indirect recursion? 
A function fun is called direct recursive if it calls the same function fun.
A function fun is called indirect recursive if it calls another function say fun_new 
and fun_new calls fun directly or indirectly.""")

print("""What is the difference between tailed and non-tailed recursion? 
A recursive function is tail recursive when a recursive call is the last thing executed
by the function.""")

print("""How memory is allocated to different function calls in recursion? 
When any function is called from main(), the memory is allocated to it on the stack.
A recursive function calls itself, the memory for a called function is allocated on top 
of memory allocated to the calling function and a different copy of local variables is
created for each function call. When the base case is reached, the function returns its
value to the function by whom it is called and memory is de-allocated and the process 
continues.""")

