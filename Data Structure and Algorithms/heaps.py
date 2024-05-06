# # Heaps 
print("""The purpose of a min-heap is to store objects that have a partial
      order on them. It has a fast (O(log n)) method for removing the 
      minimum object from the heap. Min-heaps are useful for calculations 
      where you have multiple minimum computations to perform.\nThere is 
      an analogous structure called a max-heap, which extracts the maximum 
      value from the heap.\nA heap is either a max-heap or a min-heap - 
      it can't be both. Given an implementation of a min-heap, a max-heap 
      can be implemented by reversing the comparison between elements.\n""")

print("""Crucial Terms\n· key: The values that determine the order. The key 
      is the data field that we're comparing by.\n· extract_min: The method 
      of (quickly) being able to extract the minimum element from the min-heap.\n""")

print("""Strengths and Weaknesses\n· Strengths : a min-heap is able to quickly 
      extract the minimum value on the heap. Repeated extractions from a 
      min-heap into an array will yield a sorted array.\n· Weaknesses: There's 
      no convenient way of searching for a particular key value in a heap. 
      Entries are only partially ordered; clever use of the heap property can
      allow for some pruning of searches.\n""")

print("""In Interviews, Use Heaps When ...\nHeaps are designed to do one specific
      thing well, so the answer to when you should use a heap is repetitive: 
      You use one when you have to do repeated minimum (or maximum) extractions.\n
      Examples of usage:\n
      · Finding the minimum distance between two nodes in a 
      graph: the standard approach to this problem is to use Dijkstra's algorithm.
      One of the key steps in Dijkstra's algorithm is to select the node closest 
      to a node that you have already completed, which is a minimum calculation.\n
      · Getting the next event that is scheduled to occur: storing events in a 
      heap with a timestamp as the key gives you a fast way to extract the 
      next event (the event with the smallest timestamp will occur next).\n
      · Keep track of the median value while streaming: this is the running 
      median problem, where two heaps are maintained: a max-heap for values
      below the current median and a min-heap for values above the current 
      median. When a new value is inserted, it is placed in the low or high 
      pile as appropriate (and the maximum of the low values or minimum of
      the low values are extracted as necessary to keep the two heaps 
      sizes' different by at most one element).\n
      · Find the first k non-repeating characters in a string in a single 
      traversal.""")

print("""There are other ways of constructing heaps (such as binomial 
      heaps and Fibonacci heaps) that can improve the asymptotic run time 
      slightly, but that support the same operations.""")