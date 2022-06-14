#Since we are calling classes, we have to create object to call the classes.

#Approach_[1]: Importing module==>class==>creating obj==>invoking method
import class_1
obj1=class_1.inter()
import class_2
obj2=class_2.engg()
print("Importing module==>class==>creating obj==>invoking method")
obj1.math()   #Max Inter marks:75
obj2.math()   #Max Engg marks:70


#Approach_[2]: Importing class from module directly
from class_1 import inter
print("Importing class from module directly")
objA=inter()
objA.math()
from class_2 import engg
objB=engg()  #Max Inter marks:75
objB.math()  #Max Engg marks:70
