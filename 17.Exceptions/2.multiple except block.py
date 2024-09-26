#       ||     TRY    ||  Except        ||   Else       || Finally
# Case-1 || No error   || No execution   || Executed     || Executed
# Case-2 ||  Error     || Execution      ||No Executed   || Executed

# Case-1
# print("Hai")
# try:                            #Throws no error
#     print(10/5)                 #2.0
# except SyntaxError:             #No execution
#     print("type error is pass")
# except ZeroDivisionError:
#     print("ZeroDivisionError Pass")
# else:                           #Executed
#     print("No errors")
# finally:                        #Executed
#     print("Prog done")

# Case-2
print("Hai")
try:  # Throws error
    print(10/0)  # ZeroDivisionError
except SyntaxError:  # Exception Handled
    print("type error is pass")
except ZeroDivisionError:
    print("ZeroDivisionError Pass")
else:  # Not Executed
    print("No errors")
finally:  # Executed
    print("Prog done")
