# Function:
# set of statements or set of instructions to perform a task
# def govi():   #initialization of function by def(definition)
#     print("hello")
# govi() #hello  #invoking or calling a function


# def govi(name): #name is argument or parameter
#     print("name is:",name)
# govi("Govind") #name is: Govind

# def govi(name,sex): #name is argument or parameter
#     print("name is:",name,"sex is:",sex)
# govi("Govind","male") #name is: Govind sex is: male

# def govi():
#     return
# print(govi()) #None

# def govi():
#     i=10
#     return
# print(govi())  #None

# x=25
# def govi():
#     x=35
#     print(x**2)
# govi()    #35x35=1225


# Here Global value is not changed because syntax "global x" is not mentioned inside the method
# x=25
# def govi():
#     x=35
#     print(x**2)  #1225 i.e 35x35
# govi()
# print(x)  #25

# def sum(start,end):
#     result=0
#     for i in range(start,end+1):
#         result=result+1
#         print(result,end=" ") # 1 2 3 4
#     #print(result)
# sum(2,5)

# t=1
# def loc():
#     global t
#     print(t)    #1
# loc()

class A:
    a = 10
    __b = 20

    def be(self):
        print(self.a)  # 10
        print(self.__b)  # 20


obj = A()
obj.be()
print(A.a)  # 10
print(A.__b)  # error
