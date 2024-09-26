# Instance method:
# By default methods in class are instance methods and
# to invoke/call these methods, object reference variable is required.
# self parameter is required

# Static method:
# keyword "@staticmethod" is required
# they can be invoked/called directly
# "self parameter" is not required

# Example:
class myclass():
    def mymeth(self):
        print("This is instance method")

    @staticmethod  # keyword for: Static method
    def mystat(self):
        print(self)

    @staticmethod
    def mystat1(a):
        print("this is static method")
        print(a)


obj = myclass()
obj.mymeth()  # This is instance method
obj.mystat(10)  # 10
obj.mystat1(20)  # this is static method
# #20
