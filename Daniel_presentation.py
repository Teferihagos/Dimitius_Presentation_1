# What is Decorators in Python?
# What is

# # def add(x, y):
# #     return x + y
# # #Decorator function
# # def square_args(func):
# #     def inner(x, y):
# #         return func(x * x, y * y)
# #         return inner
# #     add = square_args(add)
#
#         print(add(2, 3))

# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         # storing time before function execution
#         begin = time.time()
#
#         result = func(*args, **kwargs)
#
#         # storing time after function execution
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
#         return result
#     return inner1
# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):
#
#     # sleep 2 seconds because it takes very less time
#     # so that you can see the actual difference
#     time.sleep(2)
#     print(math.factorial(num))
#
# factorial(10)

def log(func):
    def wrap(*args, **kwargs):
        # Log the function name and arguments
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        print(f"{func.__name__} returned: {result}")

        # Return the result
        return result
    return wrap

# Example usage
@log
def multiply_numbers(x, y):
    return x * y
# Call the decorated function
result = multiply_numbers(10, 20)

print("Result:", result)

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 10

print(num())

## Generators (Generator Basics)
# Creating generators

# def gen_func(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
# result = gen_func(6)
# print(type(result))
#
# for item in result:
#     print(item)
#
# #Lazy evaluation
# print(next(result))
#
# print(next(result))
#
# print(next(result))
#
# print(next(result))

# list_result = [2 * num for num in range(10) if num % 2 == 0]
#
# print(list_result)
#
# gen_result = (2 * num for num in range(10) if num % 2 == 0)
#
# print(gen_result)
#
# for item in gen_result:
#     print(item)

#args and kwargs:

# kwargs
def print_all(**kwargs):
    #print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)

print_all(name = "Dan", location = "Atlanta", state = "Georgia")

# combining args and kwargs
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both args ,*kwargs
# to pass arguments to this function :
myFun('Danny', 'Atlanta', 'Georgia', name="Mike", city="Raleigh", state="North Carolina")`