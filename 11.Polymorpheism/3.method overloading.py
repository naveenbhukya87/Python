# Method_Overloading:
# Calling a variable in multiple ways and through which parameters are specified to call them
class A:
    def a(self, name=None):
        if name is not None:
            print("Hello "+name)
        else:
            print("Hello")


# Approach:1 without giving parameters
obA = A()
obA.a()  # Hello

# Approach:1 with giving parameters
obB = A()
obB.a("govi")  # Hello govi

# i.e same variable behaved in different way depending upon the input we have given
