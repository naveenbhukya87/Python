# Decorators are used to modify the functions externally
def div(a, b):
    print(a/b)
# division(10,2) #5.0
# division(2,5)  #0.4
# let's say I want to switch numbers if b>a:
# 1) This can be done by swapping but has to modify the code
# 2)This can also be done from externally and that ,method is called "Decorators"


def smart_div(func):

    def modified(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return modified


div = smart_div(div)
div(2, 5)
