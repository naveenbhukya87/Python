#List type is another sequence type defines by list class of python. It's similar to arrays.
list1=list()
print(list1) #==list9=[] #[] i.empty list

list9=[]
print(list9) #[] i.empty list

list2=list[1,2]
print(list2) #list[1, 2]

list3=[1,2,3,4,5]
print(list3) #[1, 2, 3, 4, 5] i.e.without printing list word

list4=["govind","handsome"]
print(list4) #['govind', 'handsome']

#NOTE:
list5=list("govind") #NOTE: [] is not used but word "list" is used to access input as characters
print(list5) #['g', 'o', 'v', 'i', 'n', 'd'] i.e., characters can be stored
listex=("govind") #HERE list keyword is not used, thus input argument is returned as one single string.
print(listex) #govind

list6=list("govind genious")
print(list6) #['g', 'o', 'v', 'i', 'n', 'd', ' ', 'g', 'e', 'n', 'i', 'o', 'u', 's'] i.e., even space is considered

list7=["govind genious"]
print(list7) #govind genious

list7=list["govind genious"]
print(list7) #list['govind genious']
print(type(list7))  #<class 'types.GenericAlias'>


li=["govind is good"] #['govind is good']
lii=list("govind is good") #['g', 'o', 'v', 'i', 'n', 'd', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']
liii=list["govind is good"] #list['govind is good']
liiii=list[liii,lii,li] #list[list['govind is good'], ['g', 'o', 'v', 'i', 'n', 'd', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'], ['govind is good']]
print(li)
print(lii)
print(liii)
print(liiii)