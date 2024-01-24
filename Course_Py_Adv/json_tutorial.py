# let's say we have a python dictionary 
# and we want to convert it to json
# this is called serialization or encoding
# https://www.python-engineer.com/

# import json
# # we have a python dictionary called person
# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# # print(personJSON)

# # I can convert it (from python object) or dump it to a file
# with open('Course_Py_Adv/person.json', 'w') as file:
#     json.dump(person, file, indent=4) # not dumps - s for string

# (person, indent=4, sort_keys=True)
# {
#     "age": 30,
#     "city": "New York",
#     "hasChildren": false,
#     "name": "John",
#     "titles": [
#         "engineer",
#         "programmer"
#     ]
# }
# (person, indent=4, separators=('; ', '= '), sort_keys=True)
# {
#     "age"= 30; 
#     "city"= "New York"; 
#     "hasChildren"= false; 
#     "name"= "John"; 
#     "titles"= [
#         "engineer"; 
#         "programmer"
#     ]
# }
# but better to use the default separators

# # Now we want to convert json to python object
# # this is called deserialization or decoding
# import json

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4, sort_keys=True)
# # print(personJSON)

# with open('Course_Py_Adv/person.json', 'r') as file:
#     person = json.load(file)
#     print(person) 
#     # {'name': 'John', 'age': 30, 'city': 'New York', 'hasChildren': False, 'titles': ['engineer', 'programmer']}

# # Let's say we have custom class
# import json

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# user = User('Max', 27)

# # userJSON = json.dumps(user)
# # print(userJSON) # TypeError: Object of type User is not JSON serializable
# # so what I have to do is to create a custom encoding function:
# def encode_user(o):
#     if isinstance(o, User):
#         return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
#     else:
#         raise TypeError('Object of type User is not JSON serializable')

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON) # {"name": "Max", "age": 27, "User": true}

# and there is a second way to do it
# u can implement a custom json encoder
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

# userJSON = json.dumps(user)
# print(userJSON) # TypeError: Object of type User is not JSON serializable
# so what I have to do is to create a custom encoding function:
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder
class UserEncoder(JSONEncoder): # and then we overwrite the default method
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
#     # and now in our dump or dumps method we can use cls parameter
# userJSON = json.dumps(user, cls=UserEncoder)
# print(userJSON) # {"name": "Max", "age": 27, "User": true}

# and as a last option we can use encoder directly
userJSON = UserEncoder().encode(user)
print(userJSON) # {"name": "Max", "age": 27, "User": true}

# now let's say we want to decode our object back

