# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

def reverse(s):
   return s[::-1]
print(reverse("I am a string"))
'gnirts a ma I'

reverse = lambda s: s[::-1]
print(reverse("I am a string"))


# 'gnirts a ma I'

def multi(x):
    x = x * 2
    return x

print(multi(64))

add = lambda x: x * 2
print(add(66))

# multiply = lambda x, y: x * y
# print(multiply(5,2))

# add = lambda x, y, z: x + y + z
# print(add(1,2,3))

# full_name = lambda first_name, last_name: first_name+" "+last_name
# print(full_name("Tech","Field"))

# age_check = lambda age: True if age >= 18 else False
# print(age_check(18))
