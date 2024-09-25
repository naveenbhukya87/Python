# In this we learn how to use if-else: used for checking single condition and
# if there are many conditions, then elif is used.

# 1
a = 15
if a > 10:
    print("Statement is true")
# NOTE: Indention is very important as it represents a bloc of code. Just after writing if condition, when we press
# enter', it just locates 1 tab space from starting point as it represents 'will be written code' belongs to if
else:
    print("statement is false")
    # cursor to be started from starting for next lines bcoz whatever we write just below print will be in "else" loop
# output: As condition is true, output is: Statement is true
print("this statement has no connection with if-else")
# this statement has no connection with if - else
# 2
if a < 10:
    print("Statement is true")
else:
    print("statement is false")
# output: As statement is false, output will "statement is false"
# 3
if True:
    print("Statement is true")
else:
    print("statement is false")
# Output: As condition is giving result 1 in form of "True", output will be "Statement is true"
# 4
if False:
    print("Statement is true")
else:
    print("statement is false")
# Output: As condition is giving result 0 in form of "False", output will be "Statement is false"
# 5
if 1:
    print("Statement is true")
else:
    print("statement is false")
# Output: As condition is giving result 1 in form of "1", output will be "Statement is true"
# 6
if 0:
    print("Statement is true")
else:
    print("statement is false")
# Output: As condition is giving result 1 in form of "False", output will be "Statement is false"

# 7 Printing multiple statements
if 1:
    print("Statement is true")
    print("Statement was true")
    print("Statement will true")
else:
    print("statement is false")
# output :Statement is true Statement was true Statement will true

if 0:
    print("Statement is true")
    print("Statement was true")
    print("Statement will true")
else:
    print("Statement will true")
    print("statement was false")
    print("Statement is true")
# output
# Statement will true
# statement was false
# Statement is true

# Single line if-else
print("statement of single line is true") if a > 10 else print(
    "statement of single line is false")
# output: statement of single line is true
print("statement of single line is true") if a < 10 else print(
    "statement of single line is false")
# output: statement of single line is false

# Single line if-else for printing multiple lines
{print("If Line 1"), print("If Line 2")} if a > 10 else {
    print("Else Line a"), print("Else Line b")}
# OUTPUT: If Line 1 If Line 2
{print("If Line 1"), print("If Line 2")} if a < 10 else {
    print("Else Line a"), print("Else Line b")}
# OUTPUT: Else Line a Else Line b

# If-else for even number or not
if a % 2 == 0:
    print("a is even number")
else:
    print("a is odd number")  # output: a is odd number for a=15

# if-else loop
a = 20
if a > 10:
    print("Statement is true")
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd and enter into else loop")
else:
    print("statement is false")
# output: Statement is true  a is even
