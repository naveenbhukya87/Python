#VARIABLES: a container which stores the values
#3 type of variables in python: viz
#1)Global variables: these are declared outside of both class and function
#2)Class variables: these are declared in class
#3)local variables: these are declared in function

#Accessing all variables
# a,b=1,2                  #GLOBAL VARIABLES
# class mygov():           #class
#     a,b=3,4              #CLASS VARIABLES
#     def govi(self):      #function
#         a,b=5,6          #LOCAL VARIABLES
#         print(a+b)                             #ACCESSING: LOCAL VARIABLES         #O/P:11
#         print(self.a+self.b)                   #ACCESSING: CLASS VARIABLES         #O/P:7
#         print(globals()['a']+globals()['b'])   #ACCESSING: GLOBAL VARIABLES        #O/P:3
# obj=mygov()
# obj.govi()

######Using global variables in local variable
# x=20
# print(x)          #20
# def mymeth():
#     global x      #correct syntax and syntax like global x=20 (X)
#     print(x**2)   #400
# mymeth()          #Here function is called directly as it's not a method.
# print(x)          #20

######Using global variables in local variable and updating value
# x=20
# print(x)          #20
# def mymeth():
#     global x      #correct syntax and syntax like global x=12 (X)
#     x=35
#     print(x**2)   #1225
# mymeth()
# print(x)          #35

#Using global variables directly in local variables by using "globals()[] syntax
# x=20
# print(x)          #20
# def mymeth():
#     print(globals()['x']**2)    #20*20=400
# mymeth()
# print(x)          #20




