# https://www.youtube.com/watch?v=FXUUSfJO_J4&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=13

# There are 2 types of decorators:
# 1. Function decorators - most common
# 2. Class decorators

# this is how decorator syntax looks like:
@mydecorator
def dosomething():
    pass
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

def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def print_name():
    print("Alex")
    
    # 2:43