# String's indices start from '0' i.e
# for a word "WELCOME" indicies are: W(0),E(1),L(2),C(3),O(4),M(5),E(6)
# Indices for a word from backside are as follows: e(-1),m(-2)......w(-7)
# "+" operator is used for "CONCATENATION"
# "*" is used for repetition of a string
line1 = "welcome"
line2 = "all"
print(line1+line2)  # OUTPUT: welcomeall
print(line1*3)  # OUTPUT: welcomewelcomewelcome
print(line2*10)  # OUTPUT: allallallallallallallallallall
print("My name is ", "Veera:Nooka:Govind".split(":")[2])  # My name is  Govind

# [3, 11, 55, 55, 222, 555, 1345, 5673]
print(sorted([555, 3, 222, 5673, 55, 11, 1345, 55]))

print(sorted(['g', 'o', 'v', 'i', 'n', 'd']))  # ['d', 'g', 'i', 'n', 'o', 'v']
