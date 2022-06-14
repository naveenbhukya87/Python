#String is a sequence type and it also gets iterable by using 'for loop'
s="welcome"
for i in s:
    print(s) #==> print(s,(end\n")
    # OUTPUT: welcome (7=no. of chars in welcome)
    # welcome
    # welcome
    # welcome
    # welcome
    # welcome
    # welcome
    # welcome
    # PROGRAM LOGIC: first letter w enters in i and its in s and condition gets satisfied and s=welcome is printed until it
    # reached i=e.
    print(s,end=" ") #welcome welcome welcome welcome welcome welcome welcome
    #end=" " prints string without a new line.
    # print(s,end="foo\n")
s = "welcome"
for i in s:
    print(i)
#OUTCOME:
# w
# e
# l
# c
# o
# m
# e

#PROGRAM LOGIC: first letter w enters in i and it gets printed and so on..until e printed.