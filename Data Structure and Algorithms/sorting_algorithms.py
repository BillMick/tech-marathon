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

print("""\n############################# The Significance of Time Complexity #############################""")
"""Two different ways to measure the runtime of sorting algorithms:
· For a practical point of view, you’ll measure the runtime of the implementations using the timeit module.
· For a more theoretical perspective, you’ll measure the runtime complexity of the algorithms using Big O notation."""

print("""Timing Your Code""")
print("""When comparing two sorting algorithms in Python, it’s always informative to look at how long each one takes 
to run. The specific time each algorithm takes will be partly determined by your hardware, but you can still 
use the proportional time between executions to help you decide which implementation is more time efficient.""")

from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print('With timeit module', f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
run_sorting_algorithm('sorted', unordered_array)

print("""Measuring Efficiency With Big O Notation""")
print("""This tutorial covers the Big O runtime complexity of each of the sorting algorithms discussed.
It also includes a brief explanation of how to determine the runtime on each particular case.""")

print("""The Bubble Sort Algorithm in Python""")
print("""Bubble Sort is one of the most straightforward sorting algorithms. Its name comes from the 
      way the algorithm works: With every new pass, the largest element in the list “bubbles up”
      toward its correct position.
Bubble sort consists of making multiple passes through a list, comparing elements one by one,
and swapping adjacent items that are out of order.""")

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True
        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]
                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False
        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break
    return array

print('With Bubble sort algorithm: ', bubble_sort(unordered_array))

print("""Measuring Bubble Sort’s Big O Runtime Complexity""")
print("""Your implementation of bubble sort consists of two nested for loops in which the algorithm performs n - 1 comparisons, then n - 2 comparisons, and so on until the final comparison is done. This comes at a total of (n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2 comparisons, which can also be written as ½n2 - ½n.
You learned earlier that Big O focuses on how the runtime grows in comparison to the size of the input. That means that, in order to turn the above equation into the Big O complexity of the algorithm, you need to remove the constants because they don’t change with the input size.
Doing so simplifies the notation to n2 - n. Since n2 grows much faster than n, this last term can be dropped as well, leaving bubble sort with an average- and worst-case complexity of O(n2).
In cases where the algorithm receives an array that’s already sorted—and assuming the implementation includes the already_sorted flag optimization explained before—the runtime complexity will come down to a much better O(n) because the algorithm will not need to visit any element more than once.
O(n), then, is the best-case runtime complexity of bubble sort. But keep in mind that best cases are an exception, and you should focus on the average case when comparing different algorithms.""")

print("""Timing Your Bubble Sort Implementation""")
ARRAY_LENGTH = 10000
# Generate an array of `ARRAY_LENGTH` items consisting
# of random integer values between 0 and 999
array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

# Call the function using the name of the sorting algorithm
# and the array you just created
run_sorting_algorithm(algorithm="bubble_sort", array=array)
