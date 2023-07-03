# Tuple: ordered, immutable, allows duplicate elements
# https://youtu.be/Kes8YRV73Io

""" ------   """
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)  # Max
print(age)  # 28
print(city)  # Boston
""" ------   """
# # Slicing w/ tuples:
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# b = a[2:5]
# print(b)  # (3, 4, 5)
#
# c = a[:5]
# print(c)  # (1, 2, 3, 4, 5)
#
# d = a[2:]
# print(d)  # (3, 4, 5, 6, 7, 8, 9, 10)
# # optional step argument
# e = a[::3]
# print(e)  # (1, 4, 7, 10)
# # trick to reverse tuple
# f = a[::-1]
# print(f)  # (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
""" ------   """
# my_tuple = ('a', 'p', 'p', 'l', 'e')
# # to get number of elements inside:
# print(len(my_tuple))  # 5
# # to count some elements inside:
# print(my_tuple.count('p'))  # 2
# # find first index of some specific el:
# print(my_tuple.index('l'))  # 3
# # convert tuples to a list and vs.
# my_list = list(my_tuple)
# print(my_list)  # ['a', 'p', 'p', 'l', 'e']
#
# my_tuple2 = tuple(my_list)
# print(my_tuple2)  # ('a', 'p', 'p', 'l', 'e')
""" ------   """
# # Check if element is iside tuple:
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)  # ('Max', 28, 'Boston')
#
# if "Max" in mytuple:
#     print("yes")  # yes
# else:
#     print("no")
""" ------   """
# #  Iterate:
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)  # ('Max', 28, 'Boston')
#
# for i in mytuple:
#     print(i)
#     # Max
#     # 28
#     # Boston
""" ------   """
# # If we wana change item inside tuple
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)  # ('Max', 28, 'Boston')
#
# mytuple[0] = "Tim"  # Tuples don't support item assignment
#  because tuple is immutable

""" ------   """
# # Use build-in Tuple function for ex. from a list:
# mytuple = tuple(["Max", 28, "Boston"])
# print(mytuple)  # ('Max', 28, 'Boston')
# # To access the element:
# item = mytuple[0]
# print(item)  # Max
#
# item1 = mytuple[-1]
# print(item1)  # Boston
""" ------   """
# mytuple = ("Max")
# print(type(mytuple))  # <class 'str'>
#
# mytuple = ("Max",)
# print(type(mytuple))  # <class 'tuple'>
""" ------   """
# # Parentheses are optional
# mytuple = "Max", 28, "Boston"
# print(mytuple)  # ('Max', 28, 'Boston')

# mytuple = ("Max", 28, "Boston")
# print(mytuple)  # ('Max', 28, 'Boston')
