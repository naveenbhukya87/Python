# Exception is an abnormal condition i.e disrupts from the normal flow or user input of the program.
# Exceptions are thrown as error in python.
# 50/0==>zero division error

# In general:
# print("welcome")
# print(10/0)
# print("Hello")
########## OUTPUT##########
# ZeroDivisionError: division by zero
# welcome

# Exception_handling: (try-except)
# print("welcome")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("exception done")
# print("Hello")
# Output
# welcome
# exception done
# Hello

# If try block throws no error, except block doesn't get executed:
# print("Hai")
# try:
#     print(10/5)
# except ZeroDivisionError:
#     print("Pass")
# print("try block throws no error, except block doesn't get executed")
# OUTPUT
# Hai
# 2.0
# try block throws no error, except block doesn't get executed


# If except block doesn't mention correct error, then error is thrown but if exception mentions multiple errors then
# error is not thrown
print("Hai")
try:
    print(10/0)
except SyntaxError:
    print("type error is pass")
except ZeroDivisionError:
    print("ZeroDivisionError Pass")
