# Sets: unordered, mutable, no duplicatss


print("15: * frozen set *")
# it is also collection data type, it's immutable version of normal set
a = frozenset([1, 2, 3, 4])

print(a)    # frozenset({1, 2, 3, 4})

# now u can't change it after it's creation

a.add(2)
print(a)    # AttributeError: 'frozenset' object has no attribute 'add'

# but union, intersection & difference methods will work

print("14: * copping two sets *")
setP = {1, 2, 3, 4, 5, 6}

setQ = setP
print(setQ)     # {1, 2, 3, 4, 5, 6}

setQ.add(7)
print(setQ)     # {1, 2, 3, 4, 5, 6, 7}
print(setP)     # {1, 2, 3, 4, 5, 6, 7}

# so if u wana make an actual reference:
setU = setP.copy()
setU.add(8)

print(setU)     # {1, 2, 3, 4, 5, 6, 7, 8}
print(setP)     # {1, 2, 3, 4, 5, 6, 7}

# or use set() method

setV = set(setP)
setV.add(9)

print(setV)     # {1, 2, 3, 4, 5, 6, 7, 9}
print(setP)     # {1, 2, 3, 4, 5, 6, 7}


print("13: * disjoint *")
setM = {1, 2, 3, 4, 5, 6}
setN = {1, 2, 3}
setO = {7, 8}

print(setM.isdisjoint(setN))      # False - because they have same elements
print(setN.isdisjoint(setO))      # True

print("13: * superset & subset *")
setK = {1, 2, 3, 4, 5, 6}
setL = {1, 2, 3}

print(setK.issubset(setL))      # False
print(setL.issubset(setK))      # True

# and the opposite:

print(setK.issuperset(setL))     # True
print(setL.issuperset(setK))     # False

print("13: * symmetric difference update method *")
setI = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setJ = {1, 2, 3, 10, 11, 12}

setI.symmetric_difference_update(setJ)

print(setI)     # {4, 5, 6, 7, 8, 9, 10, 11, 12}

print("12: * difference update method *")
setG = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setH = {1, 2, 3, 10, 11, 12}

setG.difference_update(setH)

print(setG)     # {4, 5, 6, 7, 8, 9}

print("11: * intersection_update set *")
setE = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setF = {1, 2, 3, 10, 11, 12}

setE.intersection_update(setF)

print(setE)     # {1, 2, 3}

print("10: * update set *")
# Both methods will not modify original sets
# they always return a new set.
# but we can also modify our sets in place

setC = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setD = {1, 2, 3, 10, 11, 12}

setC.update(setD)

print(setC)     # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

print("10: * difference from two sets II method *")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.symmetric_difference(setB)

print(diff)     # {4, 5, 6, 7, 8, 9, 10, 11, 12}

# Both methods will not modify original sets
# they always return a new set.
# but we can also modify our sets in place

print("9: * difference from two sets I method *")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)

print(diff)     # {4, 5, 6, 7, 8, 9}

diff = setB.difference(setA)

print(diff)     # {10, 11, 12}

print("8: * union & intersection *")
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
# now we can calculate unions - combines both from two sets w/o duplication
u = odds.union(evens)
print(u)    # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# also we can calculate intersection from two sets
# so will be print only elements found from two sets:
i = odds.intersection(primes)
print(i)   # {3, 5, 7}

print("7: * we can check if our element inside set *")
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

if 1 in myset:
    print("yes")


print("6: * we can iterate inside *")
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print(i)
                # 1
                # 2
                # 3


print("5: * mutable *")
# myset = set()
#
# myset.add(1)
# myset.add(2)
# myset.add(3)

# print(myset)    # {1, 2, 3}
#
# myset.remove(3)
# print(myset)    # {1, 2}
#
# # same as remove - discard
# myset.discard(2)
# print(myset)    # {1}
#
# # #  delete not existing element:
# # myset.remove(4)
# # print(myset)  # KeyError: 4
# myset.discard(4)
# print(myset)    # {1}
# myset.clear()
# print(myset)    # set()


myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())  # 1
print(myset)        # {2, 3}

print("4: * do empty set *")
myset = {}
print(type(myset))  # <class 'dict'>
# so to c:
myset = set()
print(type(myset))  # <class 'set'>

print("3: * unordered *")
myset = set("Hello")    # {1, 2, 3}
print(myset)    # {'l', 'e', 'o', 'H'} - unordered (order not important). able to coutn amount of unique
print(type(myset))      # <class 'set'>

print("2: * * *")
myset = set([1, 2, 3])    # {1, 2, 3}
print(myset)


print("1: * no duplicates *")
myset = {1, 2, 2, 3}

print(myset)    # {1, 2, 3}

