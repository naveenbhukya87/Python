# A function with no name is called 'lambda function'.
# It is also known as 'anonymous function'
# It can take any number of parameters but can have only one function.
# syntax:  function=lambda arguments:expression
#         print(fun(values))

# Passing single variables
def x(a): return a+10


# here x=function, a=argument, a+10=expression
print(x(10))  # 20

# In functions, this can be written as:
print("Function method")


def x(a):
    a = a+10
    print(a)


x(10)  # 20      #Lambda function simplied just as above


def y(b): return b**2


print(y(5))  # 25


# Passing multiple variables:

def z(p, q, r, s): return p*q*r*s


print(z(1, 2, 3, 4))  # 24
