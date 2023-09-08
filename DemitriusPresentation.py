# Errors in Python
# Println("This is a syntax error"); - this was supposed to be error.

# square 5 to get 25
# print(5 ** 3)

# Some code
# result = 10 / 5
# except ZeroDivisionError:
# print("Divided by zero!")
# else:
# print("No errors occurred!")

# Some code
# result = 10 / 0
# except ZeroDivisionError:
# print("Divided by zero!")
# finally:
# print("This will always be executed!")

# Context Manager basics with class creation

# from contextlib import contextmanager
#
# file_name = ''
#
#
# @contextmanager
# def csv_Manager(filename, mode):
#     try:
#         with open(filename, mode) as file:
#             lines = file.readlines()
#             yield lines
#             file.close()
#     finally:
#         print("Final clause finished.")
#
#
# # C:\Users\Consultant\Presentation_1
# with csv_Manager(r"C:\Users\Consultant\Presentation_1\Dimitrius_Pres.csv", 'r') as file:
#     for i in range(0, 2):
        #print(file[i])
