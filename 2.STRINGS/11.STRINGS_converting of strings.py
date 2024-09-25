# Under CONVERTING STRINGS operations, cases(upper or lower cases) are converted using functions like:

name = "GoViNd iS a gOoD"
print(name.capitalize())  # Govind is a good
print(name.lower())  # govind is a good
print(name.upper())  # GOVIND IS A GOOD
print(name.title())  # Govind Is A Good
print(name.swapcase())  # gOvInD Is A GoOd
print(name.replace("a", ""))  # GoViNd iS  gOoD

# capitalize():returns a copy of string with 1st char capitalized and rest other chars in lower.
a = "govind is a good boy"
print(a.capitalize())  # OUTPUT: Govind is a good boy

# lower():returns string by converting every char to lower case
b = "GoVinD Is a GooD BoY"
print(b.lower())  # OUTPUT: govind is a good boy

# upper():returns string by converting every char to upper case
c = "govind is a good boy"
print(c.upper())  # OUTPUT: GOVIND IS A GOOD BOY

# title():returns first letter of every word of string by converting to upper case
d = "govind is a good boy"
print(d.title())  # OUTPUT: Govind Is A Good Boy

# swapcase():returns copy of a string by converting upper case letters to lower case and vice-versa
e = "GoVinD Is a GooD BoY"
print(e.swapcase())  # OUTPUT: gOvINd iS A gOOd bOy

# replace("old string1","new string2"):returns copy of a string by replacing 'old string1' by 'new string2'
f = "govind is a good boy"
print(f.replace("vin", "win"))  # OUTPUT: gowind is a good boy
