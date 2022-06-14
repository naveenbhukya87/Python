#Assigning of strings: ' ' or " " or """ """ can be used
x=('a',"b","""c""")
print(x)  #OUTPUT: ('a', 'b', 'c')

#Immutability of strings: Once the string is created, it can't be modified.
str1="govind"
str2="govind"
print(id(str1)) #OUTPUT: 26481696
print(id(str2)) #OUTPUT: 26481696
#Since the string "govind" is same, its address is fixed even if we assigned it to another variable called 'str2'
str2=str2+' is a good boy'
print(str2) #OUTPUT: govind is a good boy (CONCATENATION)
print(id(str1)) #OUTPUT:26481696
print(id(str2)) #OUTPUT:31573200
#address of a string changes with time to time.