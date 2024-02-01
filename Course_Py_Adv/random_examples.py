# https://www.youtube.com/watch?v=CsLsGCbnlJY&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=12
# Random module:
import random # this used to generate sudo random numbers
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

#### 3:45