#By default tuple is immutable but we can edit or modify through indirect way and i.e
#tuple is converted to list and values are modified and again converted to tuple
#i.e tuple==> list and modifications==> tuple

tup2=1,2,3,5,4,3,33,333,55754,1,2,3,4,"num",10.5,True
# tup2[0]=2
# print(tup2) #'tuple' object does not support item assignment
print(tup2)           #TUPLE:(1, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, 'num', 10.5, True)
listtuple=list(tup2)
print(listtuple)      #LIST: [1, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, 'num', 10.5, True]
listtuple[0]=2
print(listtuple)      #MODIFIED LIST:[2, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, 'num', 10.5, True]
tup2=tuple(listtuple)
print(tup2)         #MODIFIED TUPPLE:(2, 2, 3, 5, 4, 3, 33, 333, 55754, 1, 2, 3, 4, 'num', 10.5, True)


#COPYING ONE TUPLE INTO ANOTHER TUPLE
tup3=1,2,3,4,5,6
tup4=tup3
print(tup4) #(1, 2, 3, 4, 5, 6)
del tup3
# print(tup3) #name 'tup3' is not defined