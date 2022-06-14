#how to find the type of a variable
#let's say
x=10
print(type(x))
#output is 'int'

y=10.4
print(type(y))
#output is 'float'

s="w"  #characters and strings(words) can be inserted in either "" or ''
print(type(s))
#output is 'str'

a=True
print(type(a))
# output 'bool'

"""variable data type can be changed in the same program many times. 
This feature is not available in other programming languages
let's see the example"""
x=100
print(type(x))
x=10.8
print(type(x))
x='A'
print(type(x))
x="well"
print(type(x))
x=True
print(type(x))
#output is
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'str'>
# <class 'bool'>
#imp: float includes integer also but integer never holds float values
