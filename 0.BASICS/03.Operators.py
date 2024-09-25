# Arithmetic operators: Returning outputs will be in integers or decimals
# Operators are: +,-,*,/,//,%,**
a = 9
b = 2
print(a+b)  # Addition, Output:11
print(a-b)  # Subtraction, Output: 7
print(a*b)  # Multiplication, Output: 18
print(a/b)  # Division, Output: 4.5 (float)
print(a//b)  # Division, Output: Quotient i.e 4(int)
print(a % b)  # Mod, Output: Remainder: 1
print(a**b)  # Exponential, Output: 9x9=81
print(a**3)  # Exponential, Output: 9x9x9=729
# Relational or comparison operators: Returning outputs will be in True or False
# operators are: <,<=,>,>=,!=,==
a = 9
b = 2
print(a < b)  # Output: False
print(a > b)  # Output: True
print(a <= b)  # Output: False
# Output: True , Program Logic: first compiler checks for > and if its true, then prints True.
print(a >= b)
print(a != b)  # Output: True
print(a == b)  # output: False
a = 20
b = 20
print(a >= b)  # True #Program Logic: first compiler checks for > and its false and it goes for = and if condition is true and returns true

# Logical operators: Returning outputs will be in True or False
# Operators: 'and', 'or', 'not' . They are bit wise operators.
# Note:Logical Operators in PYTHON are keywords but not symbols like in other programs
a = True
b = False
print(a and b)  # output: False
print(a or b)  # Output: True
print(not a)  # Output: False


a = 30
b = 6
print(a == b)     # False
print(~5)       # -6
print(23 | 56)    # 63
print(23 & 56)    # 16
print(23 ^ 56)    # 47
print(56 >> 2)    # 14
print(56 << 3)    # 448
