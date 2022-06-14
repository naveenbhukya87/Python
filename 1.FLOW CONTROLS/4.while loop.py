#Here we discuss about While-loop.
#NOTE:
   #1: while loop is used when initial value, final value and condition (increment/decrement) are not known.
   #2: For loop, "RANGE" specification is not required.

#To print 1-10 numbers in increasing order:
i=1          #(INITIALIZATION)
while i<=10: #(CONDITION)
    print(i)
    i=i+1    #(INCREMENT or DECREMENT)
    #Output: 1 2 3 4 5 6 7 8 9 10
# #Here increment or decrement is need, if not loop executes infinite times.

#To print 1-10 numbers in decreasing order:
i=10
while i>=1:
    print(i)
    i=i-1 #Output: 10 9 8 7 6 5 4 3 2 1

#To print even numbers b/w 1-10
i=2
while i<=10:
    print(i)
    i=i+2 #Output: 2 4 6 8 10

#To print odd numbers b/w 1-10
i=1
while i<=10:
    print(i)
    i=i+2 #Output: 1 3 5 7 9

