#Approach__(1): Importing modules and accessing elements
import inter    #Importing modules
import engg     #Importing modules
print("Importing modules and accessing elements")
inter.sub()     #accessing elements from module       #Subject is Maths
inter.marks()   #accessing elements from module       #Max marks:75
engg.sub()      #accessing elements from module       #Subject is Engg. Maths
engg.marks()    #accessing elements from module       #Max marks:70

#Approach__(2): Importing elements from modules directly
print("Importing elements from modules directly")
from inter import sub,marks
from engg import sub,marks
sub()
marks()
sub()
marks()

#Subject is Engg. Maths
#Max marks:70
#Subject is Engg. Maths
#Max marks:70
#NOTE: Output is same because content we called from 2 modules have same names and this conflict can be solved by
#      following method:
print("Importing elements from modules directly by correct way")
from inter import sub,marks
sub()
marks()
from engg import sub,marks
sub()
marks()
# Importing elements from modules directly by correct way
# Subject is Maths
# Max marks:75
# Subject is Engg. Maths
# Max marks:70
