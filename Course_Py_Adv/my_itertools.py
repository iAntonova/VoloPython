# itertools: https://docs.python.org/3/library/itertools.html
# https://www.youtube.com/watch?v=3ecISAkioPc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=8
# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

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

# permutations



