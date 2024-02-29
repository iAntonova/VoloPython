# https://www.youtube.com/watch?v=CsLsGCbnlJY&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=12
# Random module:
import random # this used to generate sudo random numbers

import secrets # this is used to generate secure random numbers

import numpy as np # this is used to generate random numbers with arrays

# it is called sudo random because it is not truly random
a = random.random() # this will generate a random number between 0 and 1
print(a) # 0.7674219548629084

# if we mant a specific range we can use random.uniform:
b = random.uniform(1, 10) # this will generate a random number between 1 and 10
# and give it start and stop values 
print(b) # 2.351951838569433

# if we want to generate a random integer we can use random.randint:
c = random.randint(1, 6) # this will generate a random integer between 1 and 6
print(c) # 4 - and this will include the upper and lower bounds

# if you expect to not include the upper bound you can use random.randrange:
d = random.randrange(1, 6) # this will generate a random integer between 1 and 6    
print(d) # 4 - and this will not include the upper bound
# so this never pick the upper bound 6 here

e = random.normalvariate(0, 1) # this will generate a random number from a normal distribution
print(e) # 0.1713118127692926
# mu = 0 and sigma = 1
# this might be useful for machine learning or statistics
# this will pick a random number from a normal distribution

# Random functions with different functions to work with sequences:
mylist = list("ABCDEFGH")
print(mylist) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# now we can use random.choice to pick a random element from the list:
f = random.choice(mylist) # this will pick a random element from the list
print(f) # D

# if we want to pick several elements from the list we can use random.sample:
g = random.sample(mylist, 3) # this will pick 3 random elements from the list,
# and it will pick unique elements
print(g) # ['G', 'F', 'A'] - this will pick 3 unique elements from the list

# if we want to pick multiple elements from the list we can use random.choices:
h = random.choices(mylist, k=3) # this will pick 3 random elements from the list, 
# and it will pick the same element several times
print(h) # ['G', 'F', 'A'] - this will pick 3 same elements from the list several times

# if we want to shuffle the list we can use random.shuffle:
random.shuffle(mylist) # this will shuffle the list in place
print(mylist) # ['H', 'A', 'D', 'E', 'F', 'B', 'C', 'G']

# these are the most common functions to generate random numbers and work with sequences.
# I said that these are pseudo- random numbers because they are reproducible and 
# you can do this with the random.seed function:

random.seed(1) # this will generate the same random numbers every time
# then I can do different random operations
print(random.random()) # 0.13436424411240122
print(random.randint(1, 10)) # 2
# and then I can reseed again with this value with the same value
random.seed(1) # this will generate the same random numbers every time
print(random.random()) # 0.13436424411240122
print(random.randint(1, 10)) # 2
# and if I run this then we see than these are now exactly the same numbers here
# now I can seed it with a different value here
random.seed(1)
print(random.random()) # 0.13436424411240122
print(random.randint(1, 10)) # 2

random.seed(2)
print(random.random()) # 0.9560342718892494
print(random.randint(1, 10)) # 1

random.seed(2)
print(random.random()) # 0.9560342718892494
print(random.randint(1, 10)) # 1

random.seed(1)
print(random.random()) # 0.13436424411240122
print(random.randint(1, 10)) # 2

# 0.13436424411240122
# 2
# 0.13436424411240122
# 2
# 0.13436424411240122
# 2
# 0.9560342718892494
# 1
# 0.9560342718892494
# 1
# 0.13436424411240122
# 2

# and now we see that all our operations or our random numbers with a seed of 1 
# are now the same and then all where I use to seed to all these random pick are now the same

# so this is how you reproduce ur data with this random seed functions and 
# because these numbers are reproducible they are not recommended to use for
# security purposes
# and for this purpose u should use the secrets module
# this only has three functions and they should be used for things like passwords,
# security tokens, or account authentification things.
# The disadvantage is that it's slower than the random module for these algorithms
# but it's more secure (they will generate a true random number).

# First we have secrets.randbelow:
a = secrets.randbelow(10) # it has an exclusive upper bound
# this will generate a random int between 0 and 9
print(a) # 3

# Second we have secrets.randbits:
b = secrets.randbits(4) # this will generate a random int with 4 bits
# so this will return an int with K random bits
# here 4 bits means that it can has 4 different random binary values
# sp the highest possible number here in this case would be 1111
# so this 15 in decimal, so this is 2^3=(8) + 2^2=(4) + 2^1=(1) + 2^0=(1) = 15
# so this will generate a random int between 0 and 15
print(b) # 10 - this will generate a random int with 4 bits

# Third we have secrets.choice:
# let's say we have a list of chars in here 
mylist = list("ABCDEFGH")
# and then I can use a secrets.choice to pick a random element from the list
c = secrets.choice(mylist) # this will pick a random element from the list
print(c) # D # this will pick a random choice that is not reproducible

# If you working with arrays then u can use the numpy module
# it has a random module that has a lot of functions to work with arrays
# pip install numpy
# import numpy as np
# and then I can use np.random to generate random floats with arrays
a = np.random.rand(3) # this will generate a 3x1 array with random floats
print(a) # [0.5488135  0.71518937 0.60276338]

a = np.random.rand(3, 3) # this will generate a 3x3 array with random floats
print(a) 
# [[0.5488135  0.71518937 0.60276338]
#  [0.54488318 0.4236548  0.64589411]
#  [0.43758721 0.891773   0.96366276]]

# if I want to generate random integers I can use np.random.randint:
a = np.random.randint(0, 10, 3) # this will generate a 3x1 array with random integers
print(a) # [3 6 5]

# If I want to have an array with higher dimensions I have to use a tuple:
a = np.random.randint(0, 10, (3, 4)) # this will generate a 3x4 array with random integers
print(a)
# [[3 7 9 3]
#  [5 2 4 7]
#  [6 8 8 1]]
# a three by four array with random integers
# this will aslo have a random shuffle function
# so let's say I have a numpy array with different dimensions
arr = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(arr)
np.random.shuffle(arr) # this will shuffle the array in place
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# [[4 5 6]
#  [1 2 3]
#  [7 8 9]]
# and this will only shuffle the elements along our first axis
# so this will never switch the elements between the rows
# but only switch the elements within the rows (in the first axis)

# important thing to know that numpy random generaor uses a different random number generator 
# than the random module from the python standard library
# and it also has a different seed function:
np.random.seed(1) # this will generate the same random numbers every time
print(np.random.rand(3, 3))
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]
# this will generate the same random numbers every time
np.random.seed(1) #
print(np.random.rand(3, 3))
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04]
#  [3.02332573e-01 1.46755891e-01 9.23385948e-02]
#  [1.86260211e-01 3.45560727e-01 3.96767474e-01]]
# important thing is you should use the numpy random generator if you are working with arrays





#### 3:45