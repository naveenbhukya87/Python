#Here we learn about formatting output with % & {} i.e. output can be produced by using %, {}.
# Let's understand
# with the following data in various approaches, viz,

name="Govind"
age=26
ht=5.9

#Approach:0
print("name:",name,"\nage:",age,"\nheight:",ht)
#name:Govind
#age:26
#height:5.9

#approach_1 :
print(name,age,ht)
#output: Govind 26 5.9

#approach_2
print("Name is:",name)
print("Age is:",age)
print("Height is:",ht)
#output
# Name is: Govind
# Age is: 26
# Height is: 5.9

#approach_3:using % operator. Here data type is important.
print("Name:%s,Age:%d,height:%f"%(name,age,ht))
#Note: After closing inverted commas " comma (,) is not used.
#output: Name:Govind,Age:26,height:5.900000

#approach_4:using {} operator. Here data type is not important but order of value is important.
print("Name:{},Age:{},Height:{}".format(name,age,ht))
#note: Here after closing inverted commas " comma (,) is not used but ".format" is used.
#output: Name:Govind,Age:26,Height:5.9
#note: Here one's value can be assigned to another element like in below example
print("Name:{},Age:{},Height:{}".format(age,ht,name))
#Output: Name:26,Age:5.9,Height:Govind

#approach_5:using {} operator and INDEX OF THE VARIABLES. Here data type is not important
# but order of value is important.
print("Name:{0},Age:{1},Height:{2}".format(name,age,ht))
#OUTPUT:Name:Govind,Age:26,Height:5.9
#Note: Index starts from 0
#note: Here one's value can be assigned to another element like in below example
# by changing indicies of cariables
print("Name:{0},Age:{1},Height:{2}".format(age,ht,name))
#Output:Name:26,Age:5.9,Height:Govind
#note: Here one's value can be assigned to another element like in below example changing indicies of variables
print("Name:{1},Age:{1},Height:{1}".format(age,ht,name))
#Output:Name:5.9,Age:5.9,Height:5.9


