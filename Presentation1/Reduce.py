### Reduce function
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

# ex.1 - Run the code
import functools

letters = ["P", "E", "A", "C", "E"]
word = functools.reduce(lambda x, y: x + y, letters)
print(word)
# The goal is to reduce all this commulative values into a single commulative value.

# ex.2
# factorBy = [5,4,3,2,1] ## The lambda fun multiplies the first 2 numbers and continues with the rest.
# result = functools.reduce(lambda x, y,:x * y,factorBy)
# print(result)
