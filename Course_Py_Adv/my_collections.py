# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter) # Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items()) # dict_items([('a', 5), ('b', 4), ('c', 3)])
print(my_counter.keys()) # dict_keys(['a', 'b', 'c'])
print(my_counter.values()) # dict_values([5, 4, 3])
print(my_counter.most_common(1)) # [('a', 5)] - most common element
print(my_counter.most_common(2)) # [('a', 5), ('b', 4)] - two most common elements
print(my_counter.most_common(1)[0]) # ('a', 5) - most common element
print(my_counter.most_common(1)[0][0]) # a - most common element
print(my_counter.elements()) # <itertools.chain object at 0x7f9b1c0b6f10> - iterator
print(list(my_counter.elements())) # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
