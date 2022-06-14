# "==" & "!=" are used to compare dictionaries
#NOTE: >,>= and rest other are not used in dictionary

dic1={"good":4,"goo":"3",2:"go",1:1}
dic2={"good":4,"goo":"3",2:"go",1:1}
dic3={"good":4,"goo":"3",2:"go",1:12}
dic4={"good":4,2:"go",1:1,"goo":"3"}
print(dic1==dic2) #True
print(dic2==dic3) #False
print(dic1==dic1) #True
print(dic2!=dic3) #True
print(dic2>=dic3) #'>=' not supported between instances of 'dict' and 'dict'
print(dic1==dic4) #True , #order is not important but keyvalues must be same





