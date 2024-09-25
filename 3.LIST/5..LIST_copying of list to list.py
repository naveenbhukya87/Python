# copying of one list to another list can be done by 2 ways viz,
# 1).copy()
# list1=[1,2,3]
# list2=list(list1) #[1, 2, 3]
# print(list2)


# 2) for loop and .append()
# lista=[1,2,3]
# listb=["a,b,c"]
# print(lista)
# print(listb)
# # for i in listb:
# #     lista.append(i)
# # print(lista)  #[1, 2, 3, 'a,b,c']
# for i in lista:
#     listb.append(i)
# print(listb)  #['a,b,c', 1, 2, 3]


# 3).extend()
lista = [1, 2, 3]
listb = ["a,b,c"]
# lista.extend(listb) #MEANING: lista is extended with listb
# print(lista)  #[1, 2, 3, 'a,b,c']
# listb.extend(lista) #['a,b,c', 1, 2, 3, 'a,b,c']
# print(listb)

# 4) concate method using "+"
# lista=[1,2,3]
# listb=["a,b,c"]
# print(lista+listb) #[1, 2, 3, 'a,b,c']
