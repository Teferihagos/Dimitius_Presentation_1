## Immutability:
# Can not reassign
t = "Techconsulting"
print(type(t))  ## class 'str'

 t[0] = "M"
"""TypeError: 'str' object does not support item assignment"""
## We can further verify this by checking the memory location address of the position of
# of the letters of the string.

# We can further verify this by checking the memory location
# address of the position of the letters of the string.

x = 'banana'

for idx in range(0, 5):
print(x[idx], "=", id(x[idx]))

b = 140726842529592
a = 140726842529536
n = 140726842530264
a = 140726842529536
n = 140726842530264
