# x=True
# print(type(x))
# float(x)
# print(float(x))
# print(type(float(x)))

# OUTPUT
# <class 'bool'>
# 1.0
# <class 'float'>

# x=False
# print(type(x))
# float(x)
# print(float(x))
# print(type(float(x)))

# x=10.5
# print(type(x))
# bool(x)
# print(bool(x))
# print(type(bool(x)))
# OUTPUT: float  True    bool

# x=0
# print(type(x))
# bool(x)
# print(bool(x))
# print(type(bool(x)))

# OUTPUT: int    False   bool

# x=-12
# print(type(x))
# bool(x)
# print(bool(x))
# print(type(bool(x)))

# OUTPUT: int    True    bool

a = [1, 2, 3, 4, 5, 10, 10, 3]
print(max(a))
print(min(a))
print(len(a))
print(type(a))


# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2:"))
# num3=int(input("enter the number3:"))
# if num1>num2>num3:
#     print("num1 is larger")
# elif num2>num3>num1:
#     print("num2 is larger")
# elif num3>num2>num1:
#     print("num3 is larger")
# else:
#     print("N/A")
# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2:"))
# num3=int(input("enter the number3:"))
# if num1>num2 and num1>num3:
#     print("num1 is larger")
# elif num2>num3 and num2>num1:
#     print("num2 is larger")
# elif num3>num2 and num3>num1:
#     print("num3 is larger")
# else:
#     print("N/A")

# OPERATORS

# ARITHMETIC
# a=35
# b=2
# print(a+b) #37
# print(a-b) #33
# print(a*b) #70
# print(a/b) #17.5
# print(a//b) #17
# print(a%b) #1
# print(a**3) #1225


# RELATIONAL OPERATORS:
# a=10
# b=20
# c=30
# print(a<b<c) #True
# print(a<b) #True
# print(a>=b) #False
# print(a<=b) #True
# print(a!=b) #True
# print(a==b)

# LOGICAL: and or not
# a=0
# b=0
# print(a and b)
# print(not a)
# print(a or b)

# STRINGS


'''
AND: 
    - operator returns the first falsy value it encounters, or the last value if none are falsy.
    - print(-1 and 0):
        - returns 0 because it is falsy
    - print(4 and 5):
        - returns 5 because 4 and 5 are true only and now "AND" operator returns the last value.

OR: 
    - operator returns the first truthy value it encounters, or the last value if none are truthy.
    - print(-1 and 0):
        - returns -1 because it is true.
NOT: 
    - returns negation value 
    - NOT 5: False
    - NOT 0: True
'''
