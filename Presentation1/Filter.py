"""
Filter the list from the vowels
"""

# Defining functions in Python
# def function_name(input1, input2, ..., input-n)

my_vowels = ['a', 'e', 'i', 'o', 'u']


def check_vowels(ipeace):
    for i in ipeace:
        if i in my_vowels:
            print(f"{i} is a vowel")
        else:
            print(f"{i} is not a vowel")


# using filter function
filtered = filter(check_vowels, "Shalom")
print(filtered)

print('The filtered letters are:')
for s in filtered:
    print(s)

# check_vowels("i peace")