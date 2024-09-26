# 1) Single level Inheritence
print("Single level Inheritence")


class A:
    a, b = 10, 20
    print(a+b)  # 30

    def a1(self, c, d):
        print(c*d)  # 8


class B(A):
    def b1(self, e, f):
        print(e+f)  # 3


obB = B()
# Named objects and called a1 and b1 from class B
obB.b1(1, 2)
obB.a1(2, 4)
# Named objects and called only a1 but not b1 from class A
obA = A()
obA.a1(2, 5)
# Nameless objects
A().a1(2, 5)
B().a1(9, 2)
B().b1(9, 2)

# 2)Multi-level Inheritence

print("Multi-level Inheritence")


class A:
    a, b = 10, 2
    print(a*b)  # 30

    def a1(self, c, d):
        print(c*d)  # 8


class B(A):
    def b1(self, e, f):
        print(e*f)


class C(B):
    def c1(self, p, q):
        print(p*q)


obC = C()
obC.a1(10, 3)
obC.b1(10, 4)
obC.c1(10, 5)

# Multi-level Inheritence
# 20
# 30
# 40
# 50

# 3) Hierarchial Inheritence
print("Hierarchial Inheritence")


class A:
    a, b = 10, 2
    print(a*b)  # 30

    def a1(self, c, d):
        print(c*d)  # 8


class B(A):
    def b1(self, e, f):
        print(e*f)


class C(A):
    def c1(self, p, q):
        print(p*q)


obC = C()
obB = B()
# Invoking A through C
obC.a1(10, 3)  # 30
obC.c1(10, 4)  # 40
# Invoking A through B
obB.a1(10, 3)  # 30
obB.b1(10, 4)  # 30

# 4)Multiple Inheritence
print("Multiple Inheritence")


class A():
    a, b = 10, 2
    print(a*b)  # 30

    def a1(self, c, d):
        print(c*d)  # 8


class B():
    def b1(self, e, f):
        print(e*f)


class C(A, B):
    def c1(self, p, q):
        print(p*q)


obC = C()
obC.a1(10, 3)
obC.b1(10, 4)
obC.c1(10, 5)
# Multiple Inheritence
# 20
# 30
# 40
# 50

# Hybrid Inheritence: It's combination of both """Hierarchial""" and """Multiple""" inheritences
print("Hybrid Inheritence")


class A:
    a, b = 10, 2
    print(a*b)  # 30

    def a1(self, c, d):
        print(c*d)  # 8


class B(A):
    def b1(self, e, f):
        print(e*f)


class C(A):
    def c1(self, p, q):
        print(p*q)


class D(B, C):
    def d1(self, x, y):
        print(x*y)


obD = D()
obD.a1(10, 3)
obD.b1(10, 4)
obD.c1(10, 5)
obD.d1(10, 6)
# Hybrid Inheritence
# 20
# 30
# 40
# 50
# 60
