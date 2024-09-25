# Here we convert type casting or conversion of data type of number from int to float or vice-versa
x = 10
print(type(x))  # OUTPUT: int
float(x)
print(float(x))  # OUTPUT: ==> 10.0
print(type(float(x)))  # OUTPUT:float

x = 22
print(x, type(x))  # 22 int
print(float(x), type(float(x)))  # 22.0 float

x = 10.5
print(type(x))  # OUTPUT: float
int(x)
print(int(x))  # OUTPUT: ==> 10
print(type(int(x)))  # OUTPUT: input

x = True
print(type(x))  # bool
float(x)
print(float(x))  # 1.0
print(type(float(x)))  # Float

x = False
print(type(x))  # bool
float(x)
print(float(x))  # 0.0
print(type(float(x)))  # float

x = 10.5
print(type(x))  # float
bool(x)
print(bool(x))  # True
print(type(bool(x)))  # bool


x = 0
print(type(x))  # int
bool(x)
print(bool(x))  # False
print(type(bool(x)))  # bool
