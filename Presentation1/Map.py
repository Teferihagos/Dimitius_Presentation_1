# Map
# Ex.1
# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)

# Run the code
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16, 25]
# print(squared_numbers)

# Ex.2 - run
# def reverse(s):
#     return s[::-1]
# print(reverse("I am a string"))
# 'gnirts a ma I')

# iterator = map(reverse, animals)
# for i in iterator:
#     print(i)

# Fix the code below
# animals = ["cat", "dog", "cow", "sheep"]
# iterator = map(reverse, animals)
#  print(iterator)
# #<map object at 0x7fd3558cbef0>
#
# # As List
# iterator = map(reverse, animals)
# print(list(iterator))
# ['tac', 'god', 'gohegdeh', 'okceg']

# Run the code
# animals = ["cat", "dog", "cow", "sheep"]
# iterator = map(lambda s: s[::-1], animals)
# print(list(iterator))
# ['tac', 'god', 'gohegdeh', 'okceg']

# >>> # Combining it all into one line:
# >>> list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))
# ['tac', 'god', 'gohegdeh', 'okceg']

# Calling map() With Multiple Iterables
# There’s another form of map() that takes more than one iterable argument:
def f(a, b, c):
    return a + b + c


sum_lists = list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))

print(sum_lists)
# [111, 222, 333]

myfun = (lambda a, b, c: a + b + c)

expression = list(map(myfun,
                      [1, 2, 3],
                      [10, 20, 30],
                      [100, 200, 300])
                  )

print(expression)
