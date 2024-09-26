# converting local variables into class variables
# class govi():
#     def mygo(self,a,b):
#         print(a)  #local variable
#         print(b)  #local variable
#         self.a=a  #converting local variables into class variables
#         self.b=b  #converting local variables into class variables
#         print(self.a+self.b)
# obj=govi()
# obj.mygo(10,20)   #30

# calling local variables from another function: it is not possible to use one methods's variables in another method
class govi():
    def add(self, a, b):
        print(a+b)

    def multi(self, a, b):
        print(a*b)


obj = govi()
obj.add(10, 20)  # 30
'''obj.multi()'''  # govi.multi() missing 2 required positional arguments: 'a' and 'b'
obj.multi(100, 200)  # 20000

# calling local variables from another function: it is not possible to use one methods's variables in another method
# but can be accessed through indirect method: local variables--->class variables (in one method)
# class variables--->local variables (in another method)


class govi():
    def add(self, a, b):
        print(a+b)  # 30
        self.a = a
        self.b = b

    def multi(self):
        a = self.a
        b = self.b
        print(a*b)  # 200


obj = govi()
obj.add(10, 20)
obj.multi()
