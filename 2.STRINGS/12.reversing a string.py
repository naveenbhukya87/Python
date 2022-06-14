a="govind"
rev="" #empty string
#method-1
for i in a:      #i=g          /o    /v    /i      /n       /d
    rev=i+rev    #rev=g+''=g   /o+g  /v+og /i+vog  /n+ivog  /d+nivog
    print(rev)  #g             /og   /vog  /ivog   /nivog   /dnivog
print(rev)
# g
# og
# vog
# ivog
# nivog
# dnivog

name="reverse"
reverse=""
print(name[::-1])  #esrever