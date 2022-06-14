#SLICING OF STRINGS
#It menas taking subsets of strings from original strings by using [] operator.
# [] is also called as  SLICING OPERATORS
#SYNTAX: str(start: end) #NOTE ==> ending value is neglected
#String's indices start from '0' i.e for a word "WELCOME" indicies are: W(0),E(1),L(2),C(3),O(4),M(5),E(6)
#Indices for a word from backside are as follows: e(-1),m(-2)......w(-7)
name="govind"
print(name[0:4]) #OUTPUT: govi {g(0) o(1) v(2) i(3), NOTE:- n(4) is discareded}
print(name[:6])  #OUTPUT: govind {If start value is not given, by default it starts from 1st letter}
print(name[2:])  #OUTPUT:vind {If end value is not given, by default it continues upto last letter}
print(name[2:-1]) #OUTPUT: vin {Since end value is -1, it leaves last character and returns remaining)
print(name[2:-2]) #OUTPUT: vi {Since end value is -2, it leaves last 2 characters and returns remaining)
