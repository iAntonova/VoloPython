# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
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

# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt) # Point(x=1, y=-4)  - namedtuple
print(pt.x, pt.y) # 1 -4 - access to namedtuple elements

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1 # OrderedDict([('a', 1)])
ordered_dict['b'] = 1 # OrderedDict([('a', 1), ('b', 1)])
ordered_dict['c'] = 1 # OrderedDict([('a', 1), ('b', 1), ('c', 1)])
ordered_dict['d'] = 1 # OrderedDict([('a', 1), ('b', 1), ('c', 1), ('d', 1)])
print(ordered_dict) # OrderedDict([('a', 1), ('b', 1), ('c', 1), ('d', 1)])

ordered_dict = OrderedDict()
ordered_dict['b'] = 2 # OrderedDict([('b', 2)])
ordered_dict['c'] = 3 # OrderedDict([('b', 2), ('c', 3)])
ordered_dict['d'] = 4 # OrderedDict([('b', 2), ('c', 3), ('d', 4)])
ordered_dict['a'] = 1 # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
print(ordered_dict) # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])

ordered_dict = {}
ordered_dict['b'] = 2 # OrderedDict([('b', 2)])
ordered_dict['c'] = 3 # OrderedDict([('b', 2), ('c', 3)])
ordered_dict['d'] = 4 # OrderedDict([('b', 2), ('c', 3), ('d', 4)])
ordered_dict['a'] = 1 # OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 1)])
print(ordered_dict) # {'b': 2, 'c': 3, 'd': 4, 'a': 1}

# defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) # 1 - access to element
print(d['b']) # 2 - access to element
print(d['c']) # 0 - default value for new element

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) # 1.0 - access to element
print(d['b']) # 2.0 - access to element
print(d['c']) # 0.0 - default value for new element

d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d) # defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(d['a']) # 1 - access to element
print(d['b']) # 2 - access to element
print(d['c']) # [] - default value for new element

d = {}
d['a'] = 1
d['b'] = 2
print(d) # {'a': 1, 'b': 2}
print(d['a']) # 1 - access to element
print(d['b']) # 2 - access to element
print(d['c']) # KeyError: 'c' - no default value for new element

# deque - double ended queue, can add and remove elements from both ends, faster than lists
d = deque()

d.append(1) # deque([1])
d.append(2) # deque([1, 2])
print(d) # deque([1, 2]) - add element to the end

d.appendleft(3) # deque([3, 1, 2]) - add element to the beginning

d.pop() # 2 - remove element from the end of the deque
print(d) # deque([3, 1])

d.popleft() # 3 - remove element from the beginning of the deque
print(d) # deque([1])

d.clear() # deque([]) - remove all elements from the deque

d.extend([4, 5, 6]) # deque([4, 5, 6]) - add multiple elements to the end

d.extendleft([1, 2, 3]) # deque([3, 2, 1, 4, 5, 6]) - add multiple elements to the beginning

d.rotate(1) # deque([6, 3, 2, 1, 4, 5]) - rotate elements to the right

d.rotate(2) # deque([5, 6, 3, 2, 1, 4]) - rotate elements to the right

d.rotate(-1) # deque([3, 2, 1, 4, 5, 6]) - rotate elements to the left
