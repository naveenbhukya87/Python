# STRING COMPARISON: 2 strings are compared at a time by using <,>,<=,>=,==,!=
# python compares strings LEXICOGRAPHICALLY i.e., by using ASCII values of corresponding characters of strings.
# Corresponding first strings are checked and if they are similar, then goes for next characters irrespective
# of condition exists between them. If condition b/w chars satisfied, returns True,otherwise returns False
print("all" > "alla")  # False
# program logic: a=a, l=l, l=l so neglected irrespective of '>' or '<'. Now for 4th char 'a' in 2nd string, there
# no 4th char in 1st string. So its like 0>Some ASCII, it is false. So Ans:False)
# True  (a=a, l=l, l=l, alla had extra 'a' and makes it larger, so ans: true)
print("all" < "alla")
# program logic: a=a, l=l, l=l so neglected irrespective of '>' or '<'. Now for 4th char 'a' in 2nd string,
# there no 4th char in 1st string. So its like 0<Some ASCII, it is true. So Ans:True)
print("bbbb" < "abbb")  # False
# Program logic: Here 2nd,3rd,4th chars are same, for corresponding 1st letters b<a is false. So Ans: False
print(" " < "a")  # True (0<something)
print("yellow" == "yell")  # False
print("yellow" >= "yell")  # True
print("yellow" != "yell")  # True
print("yellow" <= "yell")  # False
print("yellow" <= "yellp")  # True (YELL=YELL, o<=p is true, so ans: true)
print("bbbb" < "abbbzzzzzzzzzzzzzzzzzzz ")  # False.
# This is because at first instance, b<a is false, so retruns FALSE irrespective of length of string.
