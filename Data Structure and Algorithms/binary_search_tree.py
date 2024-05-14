print('################## Binary Search Tree ##################')
print("""A binary search tree, or BST for short, is a tree where each node is a value greater 
      than all of its left child nodes and less than all of its right child nodes.""")
print("""Binary trees are useful for storing data in an organized manner so that it can 
      be quickly retrieved, inserted, updated, and deleted. This arrangement of nodes 
      allows each comparison to skip about half of the rest of the tree, so each operation 
      as a whole is lightning fast.\n
      To be precise, binary search trees provide an average Big-O complexity of O(log(n)) 
      for search, insert, update, and delete operations. log(n) is much faster than the 
      linear O(n) time required to find elements in an unsorted array. Many popular 
      production databases such as PostgreSQL and MySQL use binary trees under the 
      hood to speed up CRUD operations.""")
print("""CONS OF A BST
· Slow for a brute-force search. If you need to iterate over each node, you might have 
more success with an array.
· When the tree becomes unbalanced, all fast O(log(n)) operations quickly degrade to O(n).
· Since pointers to whole objects are typically involved, a BST can require quite a bit 
more memory than an array, although this depends on the implementation.""")