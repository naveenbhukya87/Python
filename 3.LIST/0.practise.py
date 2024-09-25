# list1=[1,2,3,4,6]
# list2=list()
# list3=[]
# list4=()
# list5=list("123456")
# # print(list1) #[1,2,3,4,6]
# # print(list2) #[]
# # print(list3) #[]
# # print(list4) #()
# # print(list1[0]) #1
# print(list5)
# print(type(list5))
# print(type(list1))
# list6=("123456")
# print(type(list6))

# list7=list["govind genious"]
# print(list7) #list['govind genious']
# print(type(list7))  #<class 'types.GenericAlias'>


# list=["govi",122,10.3,True,"True"]
# print(list)
# list[0:2]="govind","ram"
# print(list) #["govind","ram",10.3,True,"True"]


# li=["govind is good"] #['govind is good']
# lii=list("govind is good") #['g', 'o', 'v', 'i', 'n', 'd', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']
# liii=list["govind is good"] #list['govind is good']
# liiii=list[liii,lii,li] #list[list['govind is good'], ['g', 'o', 'v', 'i', 'n', 'd', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'], ['govind is good']]
# print(li)
# print(lii)
# print(liii)
# print(liiii)

# SLICING
# list=["govi","100",100]
# print(list[0:])
# print(len(list))
# #print(max(list)) #TypeError: '>' not supported between instances of 'int' and 'str'
# list2=[1,2,3,4]
# print(max(list2)) #4
# print(min(list2)) #1
# print(sum(list2)) #10
# print(list2.index(4)) #3

# Traversing
# list=[1,2,3,4,5,6,7]
# for i in list:
#     print(i,end=", ")

# .append()
# l=[1,2,3,4]
# li2=l.append(5)
# print(l)

# .count()
# list=[1,1,1,3,3,5,4,9,7,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
# print(list.count(6)) #14

# .extend()
# list1=[1,2,3]
# list2=[4,5,6]
# list2.extend(list2)
# print(list2)
# print(list2[0])

# .insert()
# print(list2.index(6))
# list2.insert(2,20)
# print(list2)
# print(list2.index(6))

# .pop()
# lis=[23,32,45,54]
# lis.pop(2)
# print(lis)
# print(lis.pop(2))
# print(lis)

# .remove()
# lis=[23,32,45,54]
# lis.remove(23)
# print(lis)

# reverse()
# lis=[23,32,45,0,54]
# lis.reverse()
# print(lis)

# sort
# lis=[23,32,45,0,54]
# # lis.sort()
# # print(lis)
#
# lis=[23,32,45,0,54]
# print(lis.insert(0,22))


lista = list(x for x in range(0, 20, 2))
print(lista)
