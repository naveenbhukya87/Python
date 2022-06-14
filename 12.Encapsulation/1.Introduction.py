#Encapsulation:
        #In OOP, encapsulation helps in prevent the data like "methods","variables" from being modification
        #by restricting access to them.
        #It can be achived by using "private methods" and "private variables"
        #In other languages, keyword "private" is specified, but in python "__" (i.e underscore) is used

#Public methods and public variables are accessed from anywhere.
#Private methods are accessed only in own class
#Private variables are accessed only either in their own class or by a method if defined.


#Examples:
#1)Private variable:
# class A:
#     a=100
#     b=200
#     __c=300
#     print(a,b)    #100 200
#     print(__c)    #300
# obj=A()
#
# print(A().a,A().b) #100 200
# print(A().__c)     #AttributeError: 'A' object has no attribute '__c' i.e access to variable '__c' is denied

#2)Accessing private variables from outside of the class indirectly:
class B:
    __p=10
    def b1(self,q):
        self.__p=q
        print(self.__p)
    def b2(self):
        print(self.__p)
objB=B()
objB.b1(20)       #20
objB.b2()         #20      i.e private variable is reassigned with another value


#3) Private method:
class A():
    def __pvt(self):
        print("This is private")
    def pub(self):
        print("This is public")
        self.__pvt()
objA=A()
objA.pub()       #This is public
                 #This is private [for "self.__pvt()"]
"""objA.__pvt()"""     #AttributeError: 'A' object has no attribute '__pvt'. Did you mean: '_A__pvt'?
                       #It shows that private methods can't be called from outside of particular class having
                       #private methods or classes.





