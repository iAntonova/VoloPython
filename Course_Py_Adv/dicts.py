# Dictionary: Key-Value pairs, Unordered, Mutable

""" ------   """
# Key types:
# u can use any immutable type as a key, also numbers
my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)  # {3: 9, 6: 36, 9: 81}

value = my_dict[3]
print(value)  # 9
# or tuple with immutable elements
mytuple = (8, 7)
my_dict = {mytuple: 15}
print(my_dict)  # {(8, 7): 15}

# using list not alowed
mylist = [8, 7]
my_dict = {mylist: 15}
print(my_dict)  # TypeError: unhashable type: 'list'
""" ------   """
# # Update dictionaries:
# my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
# my_dict_2 = dict(name="Mary", age=27, city="Boston")
#
# my_dict.update(my_dict_2)
# # value will be overiten
# print(my_dict)  # {'name': 'Mary', 'age': 27, 'email': 'max@xyz.com', 'city': 'Boston'}

""" ------   """
# # Copy a dictionary:
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}

# mydict_cpy = mydict
#
# mydict_cpy["email"] = "max@zyx"
# print(mydict_cpy)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@zyx'}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@zyx'}

# # if u need actual copy:
# mydict_cpy = mydict.copy()
#
# mydict_cpy["email"] = "max@zyx"
# print(mydict_cpy)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@zyx'}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}

# # or use dict function:
# mydict_cpy = dict(mydict)
#
# mydict_cpy["email"] = "max@zyx"
# print(mydict_cpy)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@zyx'}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}

""" ------   """
# # Loop through dictionary:
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}
#
# for key in mydict:
#     print(key)
# # name
# # age
# # city
#
# # Or
# for key in mydict.keys():
#     print(key)
# # name
# # age
# # city

# # Look over the value:
# for value in mydict.values():
#     print(value)
# # Max
# # 28
# # New York

# for key, value in mydict.items():
#     print(key, value)
# # name Max
# # age 28
# # city New York

""" ------   """
# # IF statement - to check if key in dict:
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}
# # 1st way:
# if "name" in mydict:
#     print(mydict["name"])  # Max
# # 2nd way;
#
# try:
#     print(mydict["lastname"])  # Max
# except:
#     print("Error")  # Error
""" ------   """
# # it is Mutable, so we can add or change items after it's creation
# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}
# mydict["email"] = "max@xyz.com"
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@xyz.com'}
#
# mydict["email"] = "coolmax@xyz.com"
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'coolmax@xyz.com'}
#
# Delete item using del:
# del mydict["name"]
# print(mydict)  # {'age': 28, 'city': 'New York'}
# Delete item using pop:
# mydict.pop("age")
# print(mydict)  # {'name': 'Max', 'city': 'New York'}
# # Delete item using popitem:
# mydict.popitem()
# print(mydict)  # {'name': 'Max', 'age': 28}
""" ------   """

# mydict = {"name": "Max", "age": 28, "city": "New York"}
# print(mydict)  # {'name': 'Max', 'age': 28, 'city': 'New York'}
#
# mydict2 = dict(name="Mary", age=27, city="Boston")
# print(mydict2)  # {'name': 'Mary', 'age': 27, 'city': 'Boston'}
#
# # access the values:
# value = mydict["name"]
# print(value)  # Max
