#Overriding
    #Overriding means having 2 methods with same names but performing different tasks
    # i.e one method overrides over another.

#Method_Overriding:
    #If parent and sub-classes have variables with same names, then by executing sub class, sub-class's
    #name overrides parent class's name

#Eg:1
# class A:
#     name="govi___A"
# class B(A):
#     pass
# obB=B()
# print(obB.name)
#govi___A


# class A:
#     name="govi___A"
# class B(A):
#     name="govi___B"
# obB=B()
# print(obB.name)   #govi___B
    #variable, name with value "govi___A" got overirided with value "govi___B"


#Eg:2
# class A:
#     def Aa(self):
#         return 0
# class B(A):
#     pass
# obB=B()
# print(obB)         #<__main__.B object at 0x01FA94F0>



# class A:
#     def Aa(self):
#         return 0
# class B(A):
#     def Bb(self):
#         return 10
# obB=B()
# print(obB.Bb())       #10




