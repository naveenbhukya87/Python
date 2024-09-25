# .popitem(): deletes last element from the list
key = {"govi": '4', "gov": '3', "go": 2, " ": 0, 555: "hello",
       "govin": '4', "govj": '3', "goj": 2, "15 ": 0}
# key.popitem()
# print(key) #{'govi': '4', 'gov': '3', 'go': 2, ' ': 0, 555: 'hello', 'govin': '4', 'govj': '3', 'goj': 2}

# .clear(): clears all elements from the dictionary and returns {}
# key.clear()
# print(key) #{}

# .keys():returns keys as tuples
# print(key.keys()) #dict_keys(['govi', 'gov', 'go', ' ', 555, 'govin', 'govj', 'goj', '15 '])
# print(type(key.keys())) #<class 'dict_keys'>

# .values(): returns values as tuples
# print(key.values()) #dict_values(['4', '3', 2, 0, 'hello', '4', '3', 2, 0])

# get(): return value of key and if nothing found, it returns "NONE"
# print(key.get(0)) #None
# print(key.get("govi")) #4

# pop(key): rremoves item from the dictionary and returns the value
print(key.pop("govi"))  # 4
# {'gov': '3', 'go': 2, ' ': 0, 555: 'hello', 'govin': '4', 'govj': '3', 'goj': 2, '15 ': 0}
print(key)
