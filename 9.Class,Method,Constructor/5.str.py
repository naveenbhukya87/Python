# __str__
# executes automatically when you print reference variable
# 1)
# class govi():
#     pass
# obj=govi()
# print(obj)             #<__main__.govi object at 0x017D9550>  This is memory location and is returned by __str__
# print(type(obj))       #string

# 2)
# class A:
#     def __str__(self):
#         pass
# ob=A()
# print(ob.__str__())          #None


# 3)OVER_RIDING OF __STR__
class ovr():
    def __str__(self):
        print("welcome")


ob = ovr()
print(ob)  # __str__ returned non-string (type NoneType)
# welcome
