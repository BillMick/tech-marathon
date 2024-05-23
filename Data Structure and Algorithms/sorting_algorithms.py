print("""Sorting is a basic building block that many other algorithms are built upon.""")

print("""\n############################# The Importance of Sorting Algorithms in Python #############################""")

print("""Sorting is one of the most thoroughly studied algorithms in computer science. 
There are dozens of different sorting implementations and applications that you 
can use to make your code more efficient and effective.
You can use sorting to solve a wide range of problems:
· Searching: Searching for an item on a list works much faster if the list is sorted.
· Selection: Selecting items from a list based on their relationship to the rest of the items is easier with sorted data. For example, finding the kth-largest or smallest value, or finding the median value of the list, is much easier when the values are in ascending or descending order.
· Duplicates: Finding duplicate values on a list can be done very quickly when the list is sorted.
· Distribution: Analyzing the frequency distribution of items on a list is very fast if the list is sorted. For example, finding the element that appears most or least often is relatively straightforward with a sorted list.
From commercial applications to academic research and everywhere in between, there are countless ways you can use sorting to save yourself time and effort.""")

print("""\n############################# Python’s Built-In Sorting Algorithm #############################""")
unordered_array = [8, 2, 6, 4, 5]
ordered_array = sorted(unordered_array)
print(f"Unordered array: {unordered_array}", f"Ordered array: {ordered_array}", sep="\n")

