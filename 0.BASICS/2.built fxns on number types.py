#Built-in function number type helps in printing maximum and minimum values in given arguments
#max(): returns maximum values in given arguments
#min(): returns minimum values in given arguments

large=max(10,20,300,400)
small=min(10,20,30,500,1222)
print(large) #OUTPUT: 400
print(small) #OUTPUT: 10

#These can also be written as following
print(max(10,20,300,400)) #OUTPUT:400
print(min(10,20,30,500,1222)) #OUTPUT:10
print(max(-4,-5,-1,-99,-200)) #OUTPUT:-1
print(min(-3.999999,-9.9999999999999,+40,88)) #OUTPUT: -9.9999999999999

a=1,2,3,4 
#(1,2,3,4)==TUPLE
"""
Here what's the output?
  a) Tuple(1, 2, 3, 4)     b)set{1, 2, 3, 4}      c)dictionary{'1', '2', '3', '4'}       d)List [1, 2, 3, 4]
     ANSWER: TUPLE
"""
print(max(a)) #4
print(min(a)) #1
print(len(a)) #4


x=1,4,6,7,4334,46,4,3,2,[1,2,3]
print(x)
print(type(x))
print(len(x))

# (1, 4, 6, 7, 4334, 46, 4, 3, 2, [1, 2, 3])
# <class 'tuple'>
# 10


