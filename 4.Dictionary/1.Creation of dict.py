key = {"govind": '21-07', "dob": '21/07'}
############ ONLY THIS IS DICTIONARY#########BECOZ OF THIS CURLY BRACES{}#######
print(key)  # {'govind': '21-07', 'dob': '21/07'}
# FORMAT: {"same datatype:variable data type","same datatype:variable data type"}
print(len(key))  # Length of Dictionary: 2

ram = {"243": 143, 555: 343}
print(type(ram))  # <class 'dict'>
print(ram)  # {'243': 143, 555: 343}
print(len(ram))  # Length of Dictionary: 2

# REST ARE NOT DICTIONARIES
# List
key1 = ["govind:21-07", "dob:21/07"]
print(key1)  # ['govind:21-07', 'dob:21/07']
print("key1:", type(key1)) # key1: <class 'list'>

# Tuple
key2 = ("govind:21-07", "dob:21/07")
print(key2)  # ('govind:21-07', 'dob:21/07')
print("key2:", type(key2)) # key2: <class 'tuple'>
