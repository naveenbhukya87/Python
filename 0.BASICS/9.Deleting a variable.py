# here we assign a value to a variable and again that variable will be deleted by using 'del function'
x = 20
print(x)  # output is 20
del x
print(x)  # output: NameError: name 'x' is not defined
x = 30
print(x)  # 30
