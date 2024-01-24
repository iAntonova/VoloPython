# let's say we have a python dictionary 
# and we want to convert it to json
# this is called serialization or encoding

import json
# we have a python dictionary called person
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)
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

