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

# import functools
# # and now about the return value
# def start_end_decorator(func):
#     # "*args, **kwargs" with this we can pass any number of arguments to our function
#     # and here we'll apply also a decorator called functools.wraps
#     @functools.wraps(func) # this is a decorator that copies the metadata of the function
#     def wrapper(*args, **kwargs):
#         print("Start")
#         # and inside our wrapper function I also call this function
#         # with the arguments and keyword arguments
#         # we save the result of our function in a variable called result
#         result = func(*args, **kwargs)
#         print("End")
#         # and then we return this result
#         return result
#     return wrapper

# @start_end_decorator
# # let's say we have a function called add5 and it takes an argument
# def add5(x):
#     # and then it returns x + 5
#     return x + 5
# # and then we call this function
# result = add5(10) 
# print(result) # Start
#              # End
#              # 15
# # Now about the function identity
# # so let's print the help function  
# print(help(add5)) # Help on function wrapper in module __main__:
#                     # wrapper(*args, **kwargs)
# # and aslo let's print the name of the function with double underscore method
# print(add5.__name__) # wrapper      
#     # so Python thinks that the function is called wrapper and get confused
# # to fix this we can use the wraps module from the functools module
# # result:
# #add5(x)
#     # "*args, **kwargs" with this we can pass any number of arguments to our function
#     # and here we'll apply also a decorator called functools.wraps

# # None
# # add5
# # result end

# so this is ur template for a decorator:

# import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something before
#         result = func(*args, **kwargs)
#         # Do something after
#         return result
#     return wrapper
# we see here a decorator that takes a function as an argument
# so decorators can also take arguments and what
# this means this is basically now two inner functions so 
# an inner function within and in a function and to make this clearer we loook at the following example

# # 10:34
# import functools

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(num_times): # _ is a throwaway variable
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("World") # Hello World

# Now let's talk about nested decorators (12:41)
# u can stack multiple decorators on top of each other

# import functools

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper

# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting

# # here how u can apply multiple decorators:
# import functools

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper

# def debug(func):

#     @functools.wraps(func)
#     # this debug decorator extracts the name and arguments and keyword arguments of the function
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         # and then prints the information of this function:
#         print(f"Calling {func.__name__}({signature})")
#         # executes the function and saves the result
#         result = func(*args, **kwargs)
#         # prints the information about return value
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# # when we apply multiple decorators to a function, the order matters
# # the order in which we apply the decorators is the order in which they are executed
# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting

# say_hello("Alex") # Calling say_hello('Alex')
#                     # Start
#                     # Hello Alex
#                     # End
#                     # 'say_hello' returned 'Hello Alex'

# ----------------------------

# Class decorators (15:42)
# so instead of decorating a function, we can also define a class decorator
# so class decorators same as function decorators, but they are typically
# used if we want to maintain and update a state as we call the function
# in this example, we'll create a class decorator that counts the number of times
# that I have executed a function:

class CountCalls:
    # it has init method that takes a function as an argument
    # just like a decorator function
    def __init__(self, func):
        # inside the init method, we store this function in a variable called func
        self.func = func
        # and we also initialize a variable called num_calls
        self.num_calls = 0 # and we set it to 0 at the beginning

    # and in order to write a class decorator, we need to 
    # implement the call method
    def __call__(self, *args, **kwargs): # this is the same as inner function in our function decorator
        # call method allows me to execute an object of this class
        # just like a function
        self.num_calls += 1     
        print(f"This is executed {self.num_calls} times")  
        # I also have to execute and  return the function that I have passed
        return self.func(*args, **kwargs)
#         print('hi there')
#         # return self.func(*args, **kwargs)

# # create an object of this class called cc
# # equals count calls and this takes a function here so in this example
# # we don't have a function so we'll pass none
# cc = CountCalls(None)
# # and now since I've implemented this call method
# # I can say cc() and this will execute the call method
# cc()
# # so now if I run this code, I see hi there
# # but in out example, we want to count the number of times
# # and now I'll update the state of this class

@CountCalls
def say_hello():
    return "Hello"

# now if I run this:
say_hello() # This is executed 1 times
say_hello() # This is executed 2 times

# ----------------------------------------

# (20:34) typical use case for decorators 
# for example, you can implement a timer decorator that measures how long a function takes to run
# u can use a debug decorator to print out the arguments a function is called with
# u can use a check decorator to check the arguments passed to a function fill some
# specific criteria
# u can register functions in a global dictionary using a decorator (like plugins)
# u can cash a return value of a function using a decorator
# u can add information to the function using a decorator or update the state of the function