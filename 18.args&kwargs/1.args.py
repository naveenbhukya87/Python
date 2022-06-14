# *args is not a keyword in general and we can also *govind for suppose :-(
# *args comes into play if we want to pass more arguments than required
print("sum by args")
def sum(*args):
    s=0
    for i in args:
        s=s+i
    print(s)  #55
sum(1,2,3,4,5,6,7,8,9,10)

print("multiplication by govi")
def multi(*govi):
    s=1
    for i in govi:
        s=s*i
    print(s)  #55
multi(1,2,3,4,5)   #120

print("Passing numbers from list")
def num(a,b,c,d,e):
    print(a+b+c+d+e)
arguments = [1,2,3,4,5]
num(*arguments)  #Here '*' should be mentioned.