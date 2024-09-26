# Super() keyword can be used in following 3 ways:

# 1) To invoke Parent class's methods from methods of sub class:
# print("To invoke Parent class's methods from methods of sub class")
# class A:                                  #Parent class
#     def mA(self):
#         print("Method mA from Class A")
# class B(A):                               #Child or sub class of A
#     def mB(self):
#         print("Method mB from Class B")
#         super().mA()                      #invoking "A" Parent class's method "mA" from method "mB" of sub class "B":
# b=B()
# b.mB()
# Method mB from Class B
# Method mA from Class A


# 1) To invoke Parent class's variables from methods of sub class:
##### Variables having different names#########
print("To invoke Parent class's Variables having different names from methods of sub class")


class A:  # Parent class
    a, b = 10, 2


class B(A):  # Child or sub class of A
    p, q = 10, 3

    def mB(self, x, y):
        print(x*y)
        print(self.p*self.q)
        # invoking "A" Parent class's variables "a,b" from method "
        print(self.a*self.b)

        # mB" of sub class "B":
b = B()
b.mB(10, 4)
# To invoke Parent class's Variables having different names from methods of sub class
# 40
# 30
# 20

##### Variables having same names#########
print("To invoke Parent class's Variables having same names from methods of sub class")
a, b = 10, 1


class A:  # Parent class
    a, b = 10, 2


class B(A):  # Child or sub class of A
    a, b = 10, 3

    def mB(self, a, b):
        print(a*b)
        print(self.a*self.b)
        # invoking "A" Parent class's variables "a,b" from method "mB" of sub class "B":
        print(super().a*super().b)
        print(globals()['a']*globals()['b'])


obB = B()
obB.mB(10, 4)
# To invoke Parent class's Variables having same names from methods of sub class
# 40
# 30
# 20
# 10


# 3) To invoke parent class's constructor from sub class:
######## To invoke parent class's constructor from sub class######
# print("To invoke parent class's constructor from sub class")
# class A():
#     def __init__(self):
#         print("This is parent class A's constructor and invoked from sub class B")
# class B(A):
#     pass
# obB=B()
# # To invoke parent class's constructor from sub class
# # This is parent class A's constructor and invoked from sub class B

######## To invoke parent class's constructor from sub class also having constructor######
print("*************************************************************************************")
print("To invoke parent class's constructor from sub class also having constructor")


class A():
    def __init__(self):
        print("This is parent class A's constructor and invoked from sub class B")


class B(A):
    def __init__(self):
        print("This is sub class B's constructor")
        super().__init__()  # APPROACH____1 NOTE: no need of """"self""""
        A.__init__(self)  # APPROACH____2 NOTE: Need of """""self"""""


obbB = B()

# *************************************************************************************
# To invoke parent class's constructor from sub class also having constructor
# This is sub class B's constructor
# This is parent class A's constructor and invoked from sub class B
# This is parent class A's constructor and invoked from sub class B
