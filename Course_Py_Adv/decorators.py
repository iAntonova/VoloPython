# https://www.youtube.com/watch?v=FXUUSfJO_J4&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=13

# There are 2 types of decorators:
# 1. Function decorators - most common
# 2. Class decorators

# this is how decorator syntax looks like:
# @mydecorator
# def dosomething():
#     pass
# and what this does a decorator is a function that takes another function as an argument 
# and extends its behavior without explicirly modifying it.
# In other words, it allows you add new functionality to an existing function.
# Functions in Python are first-class objects, which means that like any other object,
# they can be defined inside another function, passed as an argument to another function, 
# and even returned from a function.

# now let's have a closer look at the concept. Let's say we have a function and call it print_name
# def print_name():
#     print("Alex")
    
# and then we have a decorator fubction call it start_end_decorator. And now as an argument it takes
# another function inside our decorator fubction we have an inner fubction called wrapper.

# def start_end_decorator(func):
#     # inside our decorator fubction we have an inner fubction called wrapper.
#     def wrapper():
#         print("Start")
#         # insede our wrapper function we execute the function
#         # and then I can extend the behavior of the function
#         # so I can do something before and after it
#         func()
#         print("End")
#         # and then after creating this inner wrapper function
#         # I also have to return it and now
#     return wrapper

# # def print_name():
# #     print("Alex")
    
# # # to apply this let's firs of all simply let's execute our print_name function
# # # print_name() # Alex
# # # and in order to apply the decorator I assign this print_name function to 
# # # our decorator function start_end_decorator

# # print_name = start_end_decorator(print_name)
# # print_name() # Start
# #              # Alex
# #              # End
# # # so now this name function has this new functionallity 

# # another way to do this (line 38-50) is to use the @ symbol:
# @start_end_decorator
# def print_name():
#     print("Alex")
    
# print_name() # Start
#                 # Alex
#                 # End
# # this is how we can extend the behavior of a function with a decorator               

# so let's see what happens if our function has some arguments

# def start_end_decorator(func):
#     # "*args, **kwargs" with this we can pass any number of arguments to our function
#     def wrapper(*args, **kwargs):
#         print("Start")
#         # and inside our wrapper function I also call this function
#         # with the arguments and keyword arguments
#         func(*args, **kwargs)
#         print("End")
#     return wrapper

# @start_end_decorator
# # let's say we have a function called add5 and it takes an argument
# def add5(x):
#     # and then it returns x + 5
#     return x + 5
# # and then we call this function
# add5(10) # Start
#             # End
#             # 15
# so this is how we apply arguments

# and now about the return value
def start_end_decorator(func):
    # "*args, **kwargs" with this we can pass any number of arguments to our function
    def wrapper(*args, **kwargs):
        print("Start")
        # and inside our wrapper function I also call this function
        # with the arguments and keyword arguments
        # we save the result of our function in a variable called result
        result = func(*args, **kwargs)
        print("End")
        # and then we return this result
        return result
    return wrapper

@start_end_decorator
# let's say we have a function called add5 and it takes an argument
def add5(x):
    # and then it returns x + 5
    return x + 5
# and then we call this function
result = add5(10) 
print(result) # Start
             # End
             # 15
             
             
    # 6:40