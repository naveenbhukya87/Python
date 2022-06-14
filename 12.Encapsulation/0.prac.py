class __A:
    a,b=10,2
    print(a*b)                  #30
    def a1(self,c,d):
        print(c*d)              #8
class B(__A):
    def b1(self,e,f):
        print(e*f)
objB=B()
objB.a1(10,3)
objB.b1(10,4)
objA=__A()
objA.a1(10,5)
