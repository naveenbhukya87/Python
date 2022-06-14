#Creation of 'class' and 'syntax' meaning

class myclass:           #Here 'myclass' is a 'class' and it contains functions
    def mymethod(self):    #'mymethod' is a 'method' and a function in class is called as method,
                           #parameter 'self' represents this mymethod belongs to myclass class.
        print("This is first message printed from mymethod of myclass")
        #OUTPUT: #This is first message printed from mymethod of myclass
obj=myclass()              #myclass is called 'object' which create 'exact memory location'
                           #obj is an 'object reference variable' and identifies 'memory location' of object
                           #many objects can be created for just one class
obj.mymethod()             #obj: 'object'
                           #mymethod is 'method' created under myclass class


#calling one method from another method using 'self' method
print("calling one method from another method")
class mycla():
    def m1(self):
        print("This is m1")
        self.m2()
    def m2(self):
        print("this is m2")

obj=mycla()
#obj.m1()
obj.m2()





