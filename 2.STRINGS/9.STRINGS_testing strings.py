#String class in python has various in-built methods which allow to check for different types of strings
'''
isalnum()
isalpha()
isdigital()
isidentifier()
islower()
isupper()
isspace()
'''

#isalnum(): returns "True" if string has atleast one alphabet or number
s="welc0me"
print(s.isalnum()) #True (becoz it welcome has 0 in place of o)
x="123"
print(x.isalnum()) #True (Now x is string and it has contained with only numbers, so it returned True)
x="welcome"
print(x.isalnum()) #True (it has either alphabets or numbers)
x="___"
print(x.isalnum()) #False (it has neither alphabets nor numbers)

#isalpha(): returns "True" if string contains only alphabet
s="welc0me"
print(s.isalpha()) #False
x="123"
print(x.isalpha()) #False
x="welcome"
print(x.isalpha()) #True
x="___"
print(x.isalpha()) #False

#isdigit(): returns "True" if string contains only digits
s="welc0me"
print(s.isdigit()) #False
x="123"
print(x.isdigit()) #True
x="welcome"
print(x.isdigit()) #False
x="___"
print(x.isdigit()) #False

#isidentifier(): returns "True" if string contains true identifier
#IDENTIFIER: Group of letters, numbers or underscores. !,@,*,#,$,% are not allowed.
s="welc0me"
print(s.isidentifier()) #True
a="123"
print(a.isidentifier()) #False
a="1_23"
print(a.isidentifier()) #True
b="Wel"
print(b.isidentifier()) #True
c="___"
print(c.isidentifier()) #True
d="_abc1___3"
print(d.isidentifier()) #True

#islowers():return 'True' if string is totally in lower case.
a="welcome"
print(a.islower()) #True
b="welocoMe"
print(b.islower()) #False

#isupper():return 'True' if string is totally in upper case.
a="welcome"
print(a.isupper()) #False
b="WELCOME"
print(b.isupper()) #True

#isspace():return 'True' if string contains white space only.
a="wel come"
print(a.isspace()) #False
b=""
print(b.isspace()) #False
c=" "
print(c.isspace()) #True




