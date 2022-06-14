#In functions in brackets, whatever the values we assign are called as 'arguments or parameters' and
# they are of 2 types:
#1) Positional arguments or parameters
# def govi(a,b):
#     print(a+b)
#     print(a-b)
#govi(100,200)
#300
#-100            i.e, here a=100, b=200
#govi(200,100)
#300
#100             i.e, here a=200, b=100

#2) KEYWORD arguments or parameters
# def govi(a,b):
#     print(a+b)
#     print(a-b)
# govi(a=10,b=20)
#30
#-10            i.e, here a=20, b=10
#govi(b=10,a=20)
#30
#-10            i.e, here a=20, b=10

#KEYWORD & POSITIONAL arguments
# def govi(a,b,c):
#     print(a+b+c)
#     print(a-b+c)
# govi(10,20,30)        #a=10,b=20,c=30, #O/P: 60||20
# govi(10,b=20,c=30)    #a=10,b=20,c=30, #O/P: 60||20
# govi(10,20,c=30)      #a=10,b=20,c=30, #O/P: 60||20
#govi(10,b=20,30)       #SyntaxError: positional argument follows keyword argument
#NOTE: Positional argument comes first and then keyword argument comes later
#govi(10,30,b=20)     #govi() got multiple values for argument 'b'
#NOTE:Here Positional argument is followed by keyword argument but argument b gets input by both positional and keyword argument and thus it is an error.





















