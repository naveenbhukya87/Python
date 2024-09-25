# Following functions are used to search a string in another string, viz:

# endswith("string1"):returns 'True' if a string ends with string1.
a = "internation"
print(a.endswith("nation"))  # True
print(a.endswith("natio"))  # False

# startswith("string1"):returns 'True' if a string starts with string1.
b = "internation"
print(b.startswith("int"))  # True
print(b.startswith("nt"))  # False

# find("string1"):returns 'index (lowest index)' from where the string1 starts in string. If nothing matches,returns -1
c = "assassination"
print(c.find("ass"))  # 0 (Answer could be 0 or 3 but lowest is 0, so returns 0)
print(c.find("ah"))  # -1 (no ah in given string 'c')

# rfind("string1):returns 'index (highest index)' from where the string1 starts in string. If nothing matches,returns -1.
# NOTE: Spaces are also counted
d = "govind is good and genious"
# 19 (indicies of g in d are: 0,10,19 and maximum is 19 and it's returned)
print(d.rfind("g"))
# 23 (indicies of o in d are: 1,11,12,23 and maximum is 23 and it's returned)
print(d.rfind("o"))
print(d.rfind("z"))  # -1 (No z in str d, so answer is -1)

# count("string1"):returns number of occurences of string1 in a string. \
e = "Accommodation is not mandatory in programmee"
print(e.count("m"))  # 5 (m is repeated for 5 times)
print(e.count("mm"))  # 2 (mm is repeated for 2 times)
print(e.count("x"))  # 0 (As z is repeated 0, it returns 0 but not -1)

name = "engineering"
print(name.endswith("ing"))  # True
print(name.startswith("engine"))  # True
print(name.find("e"))  # 0
print(name.rfind("e"))  # 6
print(name.count("e"))  # 3
