#MULTIPLE METHODS
#multiple methods can be created for same class because:
        #Methods are independent to each other
        #Each method occupies different memory location
#Nameless_object: no referenece obj is required and function can be called directly. SYNTAX: "class().method()"
#Named_object: referenece obj is required

class myclass():
    def mymeth(self):
        print("This is instance method")
obj1=myclass()
obj1.mymeth()       #This is instance method           #Named_object
obj2=myclass()
obj2.mymeth()       #This is instance method           #Named_object
obj3=myclass()
obj3.mymeth()       #This is instance method           #Named_object
obj4=obj3
obj4.mymeth()       #This is instance method           #Named_object
myclass().mymeth()  #This is instance method           #Nameless_object
print(id(obj1))                     #23041768
print(id(obj2))                     #23041840
print(id(obj3))                     #24221872
print(id(obj4))                     #24221872....///Since obj4=obj3 both have same addresses///
print(id(myclass().mymeth()))       #1688408184 (This address is fixed and rest other addresses are varying)


#Checking objects
print(obj1 is obj2)     #False
print(obj3 is obj2)     #False
print(obj3 is obj4)     #True as obj4=obj3 and both have same addresses
print(obj3 is myclass().mymeth())     #False




