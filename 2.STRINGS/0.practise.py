#IMMUTABILITY
# a="govi"
# b="govi"
# print(id(a))
# print(id(b))
# a=5
# b=5
# print(id(a))
# print(id(b))

#OPERATIONS ON STRING: + and *
# a="govi"
# b="UPSC"
# c=4
# print(a+b) #goviUPSC
# print(a*c) #govigovigovigovi

#slicing and Operations on string
# a="govind is studying"
# b="UPSC"
# print(a[0:3]*3) #govgovgov

#ord and chr functions
# a="⒮"
# print(chr(93907))
# print(ord(a))

#string functions
# a="govind"
# print(len(a))
# print(max(a))
# print(min(a))
# print(len("govind"))
# print(max("govind"))
# print(min("govind"))

# #logical operators in string: in and not in
# a="govind"
# print("in" in a)
# print("win" not in a)
# print("in" in "govind")
# print("win" not in "govind")

#COMPARISON OF STRINGS
# print("govind">"excel") #True
# print("govind"<"excel") #False
# print("Govind">"excel") #False
# print("Govind"<"excel") #True
# print("govind"<"Excel") #False
# print("govind">"Excel") #True
# print("govind">"gowind") #False
# print("govind">"goVind") #True
# print("goVind">"govind")  #False


#ITERATION OF STRINGS USING for loop
# a="govind is good"
# for i in a:
#     print(i,end="") #govind is good

#TESTING OF STRING
# a="g0vind"
# b="govi"
# c="123"
# d="govind"
# e="g0vind"
# f="g)vi"
# g="_val__143"
# H="GOVIND"
# # print(H.isupper())
# i="Govind"
# print(i.islower())
# print(a.isidentifier())
# print(a.isidentifier())
# print("govind".isalpha())
# print(a.isalnum()) #True
# print(b.isalpha()) #True
# print(c.isdigit()) #True
# print(d.isdigit()) #False
# print(e.isdigit()) #False
# print(f.isdigit()) #False
# print(type(c)) #str
# z="a"
# print(z.isspace())


#SEARCHING OF STRINGS
# a="programming helps in communicating with computer."
# print(a.startswith("pro")) #True
# print(a.endswith("ter")) #True
# print(a.find("gram")) #3
# print(a.find("g")) #3
# print(a.rfind("m")) #42
# print(a.count("m")) #5

#CONVERSION of strings
a="govind is novice in programming"
b="GoViNd"
# c="___abc123"
# print(a.capitalize()) #Govind............
# print(b.lower())  #govind
# print(a.upper()) #GOVIND IS NOVICE IN PROGRAMMING
# print(b.swapcase()) #gOvInD
# print(c.swapcase())
# print(a.title()) #Govind Is Novice In Programming
print(a.replace("novice","expert"))


