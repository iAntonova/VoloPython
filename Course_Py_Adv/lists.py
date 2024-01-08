# Lists: ordered, mutable, allows duplicate elements
# https://youtu.be/QLTdOEn79Rc

"""-----------"""
# List comprehension: way to create new list from existing with one line
mylyst = [1, 2, 3, 4, 5, 6]
b = [i * i for i in mylyst]
print(b)  # [1, 4, 9, 16, 25, 36]

"""-----------"""
# # Copying the list
# list_org = ['banana', 'cherry', 'apple']
# list_cpy = list_org
# print(list_cpy)  # ['banana', 'cherry', 'apple']
# list_cpy.append('lemon')
# print(list_cpy)  # ['banana', 'cherry', 'apple', 'lemon']
# print(list_org)  # ['banana', 'cherry', 'apple', 'lemon']
# # because these both refer to the same list
# # so if u wana do an actial copy of ur list:
# list_org1 = ['banana', 'cherry', 'apple']
# list_cpy1 = list_org1.copy()
# list_cpy1.append('lemon')
# print(list_cpy1)  # ['banana', 'cherry', 'apple', 'lemon']
# print(list_org1)  # ['banana', 'cherry', 'apple']
# # Also we can do it with original .list() function
# list_org2 = ['banana', 'cherry', 'apple']
# list_cpy2 = list(list_org2)
# list_cpy2.append('lemon')
# print(list_cpy2)  # ['banana', 'cherry', 'apple', 'lemon']
# print(list_org2)  # ['banana', 'cherry', 'apple']
# # And as third option we can use .slicing()
# list_org3 = ['banana', 'cherry', 'apple']
# list_cpy3 = list_org3[:]
# list_cpy3.append('lemon')
# print(list_cpy3)  # ['banana', 'cherry', 'apple', 'lemon']
# print(list_org3)  # ['banana', 'cherry', 'apple']

"""-----------"""
# # Slicing
# mylyst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a = mylyst[1:5]
# print(a)  # [2, 3, 4, 5]
# b = mylyst[:5]
# print(b)  # [1, 2, 3, 4, 5]
# c = mylyst[1:]
# print(c)  # [2, 3, 4, 5, 6, 7, 8, 9]
# # specify step:
# d = mylyst[::1]
# print(d)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# e = mylyst[::2]  # takes every second item
# print(e)  # [1, 3, 5, 7, 9]
# e = mylyst[::-1]  # specify negative index - to reverse ur list
# print(e)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

"""-----------"""
# Create a new list with the same elements multiple times
# mylyst = [0] * 5
# print(mylyst) # [0, 0, 0, 0, 0]
#
# # Concat the list with plus operator:
# mylyst2 = [1, 2, 3, 4, 5]
#
# new_list = mylyst + mylyst2
# print(new_list) # [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
"""-----------"""

# mylyst = ['banana', 'cherry', 'apple']
# print(mylyst)

# mylyst2 = [4, 3, 1, -1, -5, 10]
# print(mylyst2)

# Sort the list (ut chenge ur list):
# [4, 3, 1, -1, -5, 10]
# item = mylyst2.sort()
# print(mylyst2) # [-5, -1, 1, 3, 4, 10]
# but if u don't want to chenge ur list, build insorted method
# new_list = sorted(mylyst2)
# print(mylyst2) # [4, 3, 1, -1, -5, 10]
# print(new_list) # [-5, -1, 1, 3, 4, 10]

# Reverse the list:
# ['banana', 'cherry', 'apple']
# item = mylyst.reverse()
# print(mylyst) # ['apple', 'cherry', 'banana']

# Remove all elements:
# ['banana', 'cherry', 'apple']
# item = mylyst.clear()
# print(mylyst) # []

# Remove specific element:
# ['banana', 'cherry', 'apple']
# item = mylyst.remove('cherry')
# print(mylyst) # ['banana', 'apple']

# Remove items:
# ['banana', 'cherry', 'apple']
# item = mylyst.pop()
# print(item) # apple
# print(mylyst) # ['banana', 'cherry']

# Append items at the specific position:
# mylyst.insert(1, "blueberry")
# print(mylyst)

# Append items:
# mylyst.append("lemon")
# print(mylyst)

# find length
# print(len(mylyst))

# mylist2 = [5, True, "apple", "apple"]
# print(mylist2)

# item = mylyst[-1] # refers to the last item
# print(item)

# iterate
# for i in mylyst:
#     print(i)

# check if element is in the list
# if 'banana' in mylyst:
#     print("yes")
# else:
#     print("no")
