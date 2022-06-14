#Here we see how to take input from user
#in Python 2.x
    #intput(): input function takes any type of data
    #raw_input(): raw_input function takes only string data
#in python 3.x
    #intput(): input function takes only string data
    #raw_input function is changed to input()
    #To change string to int: type casting or type conversion is needed.
num1=input("Value of num1:")  #input:10
num2=input("Value of num2:")  #input:20
print(num1+num2)
#output: 1020
#Reason: input() by default takes string value. so num1 and num2 are now assigned with string values. In output,
# assigned values got concatenation. This problem can be solved by 'type casting'. let's see by 2 type. viz.
#NOTE: If we use input function, by default print op is not used for inputting variables
#type1
#example__1
num1=int(input("Value of num1:"))  #input:10
num2=int(input("Value of num2:"))  #input:20
print(num1+num2)
#output: 30

#example__2
num1=float(input("Value of num1:"))  #input:10.5
num2=float(input("Value of num2:"))  #input:20.5
print(num1+num2)
#output: 31

#type2
#example__1
num1=input("Value of num1:")  #input:10
num2=input("Value of num2:")  #input:20
print(int(num1)+int(num2))
#output: 30
#example__2
num1=input("Value of num1:")  #input:10
num2=input("Value of num2:")  #input:20
print(float(num1)+float(num2))
#output: 30

#ANOTHER WAY
print("value of a:")
a=int(input())           #10
print("value of b:")
b=int(input())           #20
print(a+b)               #30

