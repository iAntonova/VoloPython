from functools import reduce

# lambda arguments: expression -
# lambda function - anonymous function, function without a name, one-line function

add10 = lambda x: x + 10
add10(5) # 15

def add10_func(x):
    return x + 10

# there is no difference between lambda function and regular function
# except lambda function is anonymous
# lambda function is not bound to any name
# lambda function is much shorter than regular function and in one line
# lambda function is not a statement, it is an expression
# lambda function can be used inside other functions

# lambda function can have multiple arguments
mult = lambda x, y: x * y
print(mult(2, 7)) # 14  

# lambda function used when we need a simple function that we will use only once
# or it is used as an argument to higher-order functions (functions that take other functions as arguments)
# for example, they are used along with built-in functions like filter, map, reduce

# Sorting method with lambda as key argument:

# 1st use case - sorting a list of tuples:

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# u can think of this as the x and y values of our points
# and now if we want to sort this list of points by x value, we can do this
points2D_sorted = sorted(points2D)

print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)]
# so by default, sorted method sorts our list of tuples by the first argument so by x value
# but we also can give it a specific rule gow to sort is by using key parameter

points2D_sorted = sorted(points2D, key=lambda x: x[1]) # sort by y value
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]

# also we can give it or define a fubction let's say Sort By Y:
def sort_by_y(x): # x is a tuple in our case, then we return x[1] - y value
    return x[1]
# we can use this function here:
points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D_sorted) # [(5, -1), (15, 1), (1, 2), (10, 4)]
# so this will return the same result as using lambda function

# 2nd use case - let's sort this according to the sum of each
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1]) # sort by sum of x and y values
print(points2D) # [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted) # [(1, 2), (5, -1), (10, 4), (15, 1)] - sorted according to the sum of each tuple

# Let's talk about map function:
# So the map function transforms each element with a function so it looks like this:
# map(func, seq) - func is a function, seq is a sequence (for example, list)
# so it applies a function to each element in the sequence
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a) # multiply each element by 2
print(b) # <map object at 0x7f9b1c0b6f10> - map object
print(list(b)) # [2, 4, 6, 8, 10] - list of mapped elements

# u can achieve the same result using list comprehension:
c = [x * 2 for x in a] # list comprehension a bit easier to read than map function
print(c) # [2, 4, 6, 8, 10] - list of mapped elements

# Let's talk about filter function:
# So the filter function filters elements in a sequence
# filter(func, seq) - also func is a function, seq is a sequence (for example, list)
# and this function returns only those elements for which the function returns True
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a) # filter only even numbers

print(list(b)) # [2, 4, 6] - list of filtered elements

c = [x for x in a if x % 2 == 0] # list comprehension a bit easier to read than filter function
print(c) # [2, 4, 6] - list of filtered elements

# Let's talk about reduce function:
# So the reduce function applies a rolling computation to sequential pairs of values in a list
# reduce(func, seq) - also takes func is a function, seq is a sequence (for example, list)
# it repeatedly applies the function to the elements and returns a single value
a = [1, 2, 3, 4]

product_a = reduce(lambda x, y: x * y, a) # multiply all elements
print(product_a) # 24 - product of all elements in the list

def multiplier(n):
    # Внутренняя функция, лямбда, запоминает значение n из внешней функции
    return lambda x: x * n

# Создаем функцию для удвоения числа
doubler = multiplier(2)

# Создаем функцию для утроения числа
tripler = multiplier(3)

# Теперь можем использовать эти функции
print(doubler(5))  # Результат будет 10
print(tripler(5))  # Результат будет 15
