# Constructor: It helps to initialize(assign values) to the data memebers of the class when an object of class is created.
# TYPES:
# 1) DEFAULT Constructor: doesn't accept any arguments except 'self' which is a reference to the "instance being constructed"
# 2) Parameterized Constructor: 1st paramter is 'self' which is a reference to the "instance being constructed" and rest
# are input from user

# NOTE## Variables in Constructor are also treated as "LOCAL VARIABLES"
# class myclass():
#     def mymeth(self):
#         print("This is instance method")
#     def __init__(self):              #Dafault constructor
#         print("this is constructor")
# obj=myclass()
# obj.mymeth()
# this is constructor
# This is instance method

# PROGRAM LOGIC: By default, while creation of object, constructor is invoked and it needs no separate object.

# In normal class and methods, parameters are input through respective methods but
# in constructor, we give input in class while creating object and it will be used by other methods
# class sum():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def inp(self):
#         print(self.a+self.b)
# obj=sum(10,20)                     #Here values are assigned during creation of object
# obj.inp()

# In normal class and methods, parameters are input through respective methods
# class sum():
#     def inp(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
# obj=sum()
# obj.inp(10,20)                   #Here values are assigned during invokation of method
