#Here values are iterated by using for loop
#NOTE:
   #1: For loop is used when initial value, final value and condition (increment/decrement) are known.
   #2: For loop, "RANGE" specification is very important.
#To print 1-10 numbers
for i in range(11):  #by default 'i' is assigned with value '0'
    print(i)                        #OUTPUT: 0 1 2 3 4 5 6 7 8 9 10
#PROGRAM LOGIC: By default 0 is entered in 'i' and as it is below 0, 0 is printed & again enters the program and 1 is
# added & goes on until 10 & loop gets exit when i=11=11
#NOTE: Maximum value or range is not included. Here range is 11 but loop continued upto 10 only.

#To print even numbers from 1-10
for i in range(2,11,2): #(intial value,maximum value, increment)
    print(i)                        #output: 2 4 6 8 10
#PROGRAM LOGIC:2 is printed & again enters program & 2 is added & goes on until it becomes i=10+2=13 & get exited from loop
#NOTE: Here by default i is assigned with '2'
##########NOTE: For block goes on executed for said range and then comes out of that block and

#To print odd numbers from 1-10
for i in range(1,10,2): #(intial value,maximum value, increment)
#NOTE: Here by default i is assigned with '1'
    print(i)                    #output: 1 3 5 7 9
#PROGRAM LOGIC:1 is printed & again enters program & 2 is added & goes on until it becomes i=9+2=11 & get exited from loop
#NOTE: Here by default i is assigned with '2'

#To print numbers using decrement:
#To print 1-10 numbers in decreasing order
for i in range(10,0,-1): #(intial value,maximum value, decrement)
#Here by default i is assigned with '10' and continues till 1 and
    print(i)                #output: 10 9 8 7 6 5 4 3 2 1
#PROGRAM LOGIC:10 is printed & again enters program & -1 is decreased & goes on until it becomes i=1-1=0 & get exited from loop
#NOTE: Here by default i is assigned with '2'
