# Abstract classes are such classes which contain one or more "abstract methods".
# Abstract method is a method i.e declared but contains "no implementation".
# Abstract classes "can't be instantiated(i.e unnoticed)" & require subclasses for implementation for abstract methods.
# Subclasses of an abstract classes in Python are not required to implement abstract methods of parent class.

# USES: We know the requirement but don't know the design part, then
# we create abstract classes and methods
# Later subclasses are created to access these.
# 'ABC' is predefined 'abstract class'i.e to create an abstract class "ABC" is extended compulsorily.
# ABC====> Abstract Base Classes

########################## Without Abstract method#####################
# class A():                                                          #
#     def govi(self):                                                 #
#         print("A's Govi")                                           #
# class B(A):                                                         #
#     def govi(self):                                                 #
#         print("B's Govi")                                           #
# obj=B()                                                             #
# obj.govi()           #B's Govi                                      #
#######################################################################

# Ex1):
# from abc import ABC,abstractmethod
#     #Here
#         # abc==>module,
#         # ABC==>Class,
#         # abstractmethod==>method
# class A(ABC):
#     @abstractmethod        #Qualifier
#     def govi(self):
#         None               #i.e. no implementation
# class B(A):
#     def govi(self):
#         print("Hello")
# obj=B()
# obj.govi()      #Hello

# Ex2):
# from abc import *          #ABC,abstractmethod can also be replaced by "*" and * imports all packages
# class A(ABC):
#     @abstractmethod        #Qualifier
#     def a(self):
#         pass               #i.e. no implementation
#     @abstractmethod
#     def b(self):
#         pass
# class B(A):
#     def a(self):
#         print("Hello")
# obj=B()
# obj.a()      #TypeError: Can't instantiate abstract class B with abstract method b
# This is because class-A has 2 abstract methods and B has 1 method and is
# not implementing method-b. Thus Class-B is also abstract class and thus object can't be assigned.
# This situation can be tackled by 2 ways:
# Approach__1: by creating another method in class B to implement the 2nd method frm class A

# from abc import *
# class A(ABC):
#     @abstractmethod        #Qualifier
#     def a(self):
#         pass               #i.e. no implementation
#     @abstractmethod
#     def b(self):
#         pass
# class B(A):
#     def a(self):
#         print("Hello")
#     def b(self):
#         print("All")
# obj=B()
# obj.a()            #Hello
# obj.b()            #All


# Approach__2: by creating another method by creating another class C to implement the 2nd method frm class A

# from abc import *
# class A(ABC):
#     @abstractmethod        #Qualifier
#     def a(self):
#         pass               #i.e. no implementation
#     @abstractmethod
#     def b(self):
#         pass
# class B(A):
#     def a(self):
#         print("Hello")
# class C(B):                 #Its C(B) but not C(A)
#     def b(self):
#         print("All")
# """objB=B()               #TypeError:Can't instantiate abstract class B with abstract method b
# objB.a()                  #Because class B is also abstract class                           """
# objC=C()
# objC.a()            #Hello
# objC.b()            #All


# Abstract class containing construction method:
from abc import *


class A(ABC):
    def __init__(self, a):
        self.a = a

    def m1(self):
        pass

    def m2(self):
        pass


class B(A):
    def m1(self):
        print(self.a+100)

    def m2(self):
        print(self.a+10)


# Here Class B is not abstract since it defines all methods of class A
objB = B(100)
objB.m1()  # 200
objB.m2()  # 110
