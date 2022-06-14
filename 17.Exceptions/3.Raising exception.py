#Using 'raise' keyword one can raise exceptions from their own methods
#SYNTAX: raise ExceptionClass("Your argument")

def age(a):
    if a<0:
        raise ValueError("Only positives are allowed")
    if a%2==0:
        print("Even")
    else:
        print("Odd")
age(10)     #Even
age(5)      #Odd
#age(-5)     #ValueError: Only positives are allowed

#exception handling for above sum
try:
    age(-5)
except ValueError:
    print("Exception raised is handled")  #Exception raised is handled
