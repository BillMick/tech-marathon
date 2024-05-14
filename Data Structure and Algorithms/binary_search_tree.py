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

print('IMPLEMENTING A B-TREE IN PYTHON')
# print('STEP 1 - BSTNODE CLASS')
print("""Our implementation won’t use a Tree class, but instead just a Node class. Binary 
      trees are really just a pointer to a root node that in turn connects to each child 
      node, so we’ll run with that idea.""")

print("""There are many applications of binary search trees in real life, and one of the most
common use cases is storing indexes and keys in a database.""")
print("Other common uses include:")
print("""· Pathfinding algorithms in video games (A*) use BSTs
· File compression using a Huffman encoding scheme uses a binary search tree
· Rendering calculations - Doom (1993) was famously the first game to use a BST
· Compilers for low-level coding languages parse syntax using a BST
· Almost every database in existence uses BSTs for key lookups""")

print("""WHAT’S THE DIFFERENCE BETWEEN A BINARY TREE AND A LINKED LIST?
While binary trees and linked lists both use pointers to keep track of nodes, 
binary trees are more efficient for searching. In fact, linked lists are O(n) 
when used to search for a specific element - that’s pretty bad! Linked lists 
excel at removing and inserting elements quickly in the middle of the list.""")

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def exists(self, val):
        if val == self.val:
            return True
        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)
        if self.right == None:
            return False
        return self.right.exists(val)
    
    def delete(self, val):
        if self == None:
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")
    print("postorder:")
    print(bst.postorder([]))
    print("#")
    print("inorder:")
    print(bst.inorder([]))
    print("#")
    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")
    print("4 exists:")
    print(bst.exists(4))
    print("6 exists:")
    print(bst.exists(6))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))
    print("#")
    print("inorder:")
    print(bst.inorder([]))

main()