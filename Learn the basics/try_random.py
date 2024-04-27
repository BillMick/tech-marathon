import random

# # Seed
# The seed() method is used to initialize the random number generator.
# The random number generator needs a number to start with (a seed value),
# to be able to generate a random number.
# Syntax : random.seed(a, version)
random.seed(3)
print(random.random())

# # GetState
# The getstate() method returns an object with the current state of the random number generator.
# print(random.getstate())

# # RandRange
# The randrange() method returns a randomly selected element from the specified range.
# Syntax : random.randrange(start, stop, step)
print(random.randrange(3, 9))

# # Randint
# Syntax : random.randint(start, stop)
print(random.randint(3, 9))

# # Choice
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# Syntax : random.choice(sequence)
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

# # Choices
# The choices() method returns a list with the randomly selected element from the specified sequence.
# You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
# Syntax : random.choices(sequence, weights=None, cum_weights=None, k=1)
print(random.choices(mylist, weights = [10, 1, 1], k = 14))