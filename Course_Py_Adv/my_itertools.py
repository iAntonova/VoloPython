# itertools: https://docs.python.org/3/library/itertools.html
# https://www.youtube.com/watch?v=3ecISAkioPc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=8
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b) 
print(prod) # <itertools.product object at 0x7f9b1c0b6f10> - iterator
print(list(prod)) # [(1, 3), (1, 4), (2, 3), (2, 4)] - list of tuples

a = [1, 2]
b = [3, 4]
prod = product(a, b, repeat=2) # repeat=2 - repeat the product 2 times 
print(list(prod)) 
# [(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), 
# (1, 3, 2, 4), (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4), 
# (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4), (2, 4, 1, 3), 
# (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)] - list of tuples

a = [1, 2]
b = [3]
prod = product(a, b, repeat=2) # repeat=2 - repeat the product 2 times 
print(list(prod)) 
# [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)] - list of tuples

# permutations - order matters - no repeat
a = [1, 2, 3]
perm = permutations(a)
print(perm) # <itertools.permutations object at 0x7f9b1c0b6f10> - iterator
print(list(perm)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] - list of tuples

perm = permutations(a, 2) # 2 - length of each tuple
print(list(perm)) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)] - list of tuples

# combinations - order does not matter - no repeat
a = [1, 2, 3, 4]
comb = combinations(a, 2) # 2 - length of each tuple
print(list(comb)) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)] - list of tuples

# combinations_with_replacement - order does not matter - repeat
a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(a, 2) # 2 - length of each tuple
print(list(comb_wr)) # [(1, 1), (1, 2), (1, 3), (1, 4),
# (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)] - list of tuples

# accumulate function - default is sum, but can be changed to other functions
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a) # [1, 2, 3, 4] - list
print(list(acc)) # [1, 3, 6, 10] - list of accumulated sums

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul) # func=operator.mul - multiply
print(a) # [1, 2, 3, 4] - list
print(list(acc)) # [1, 2, 6, 24] - list of accumulated products

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=operator.max) # func=operator.max - max
print(a)    # [1, 2, 5, 3, 4] - list
print(list(acc))    # [1, 2, 5, 5, 5] - list of accumulated max

# groupby function - groups elements by a key function
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) # key=smaller_than_3 - function
print(group_obj) # <itertools.groupby object at 0x7f9b1c0b6f10> - iterator
for key, value in group_obj:
    print(key, value) 
    # True <itertools._grouper object at 0x7f9b1c0b6f10> - iterator
    # False <itertools._grouper object at 0x7f9b1c0b6f10> - iterator

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3) # key=smaller_than_3 - function
print(group_obj) # <itertools.groupby object at 0x7f9b1c0b6f10> - iterator
for key, value in group_obj:
    print(key, list(value)) 
    # True [1, 2] - list
    # False [3, 4] - list
    
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3) # key=lambda x: x < 3 - lambda function
print(group_obj) # <itertools.groupby object at 0x7f9b1c0b6f10> - iterator
for key, value in group_obj:
    print(key, list(value)) 
    # True [1, 2] - list
    # False [3, 4] - list

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(a, key=lambda x: x['age']) # key=lambda x: x['age'] - lambda function
print(group_obj)
for key, value in group_obj:
    print(key, list(value)) 
    # 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
    # 27 [{'name': 'Lisa', 'age': 27}]
    # 28 [{'name': 'Claire', 'age': 28}] 

# infinite iterators: count, cycle, repeat
for i in count(10): # count(10) - start from 10
    print(i) # 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 - infinite loop


for i in count(10): # count(10) - start from 10
    print(i)
    if i == 15:
        break
    # 10
    # 11
    # 12
    # 13
    # 14
    # 15 - stop at 15

# cycle
a = [1, 2, 3]
for i in cycle(a):
    print(i) # 1 2 3 1 2 3 1 2 3 1 2 3 - infinite loop
    
# repeat - repeat the same element infinite number of times
a = [1, 2, 3]
for i in repeat(1):
    print(i) # 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 - infinite loop
    
a = [1, 2, 3]
for i in repeat(1, 4): # repeat(1, 4) - repeat 1 four times
    print(i) # 1 1 1 1 - stop at 4th element
