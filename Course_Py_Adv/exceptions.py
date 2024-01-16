# Errors and Exceptions
# https://www.youtube.com/watch?v=qOuOV4pDVGY&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=9

# syntax error 
# a = 5 print(a)  # SyntaxError: invalid syntax
#print(a))  # SyntaxError: invalid syntax

# exception error 
# a = 5 + '10'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# import error
#import somemodule  # ModuleNotFoundError: No module named 'somemodule'

# name error
a = 5   
#b = c  # NameError: name 'c' is not defined

# file error
# f = open('somefile.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

# value error
a = [1, 2, 3]
#a.remove(4)  # ValueError: list.remove(x): x not in list
print(a)

# index error
a = [1, 2, 3]
#a[4]  # IndexError: list index out of range    # 4 is out of range

# key error
my_dict = {'foo': 1, 'bar': 2, 'baz': 3}
# my_dict['qux']  # KeyError: 'qux' - qux is not in the dictionary

## raising an exception - raise
x = -5
# if x < 0:
#     raise Exception('x should be positive') # Exception: x should be positive

## as an alternative to raise, we can use assert
## assert is used to check if a condition in our code returns True
x = -5
# assert (x >= 0), 'x is not positive'  # AssertionError: x is not positive

# if we want to handle exception, we can catch an exception, we can use try and except
# a = 5 / 0 # ZeroDivisionError: division by zero
# then we can catch the exception:
# try:
#     a = 5 / 0
# except: # we can catch all exceptions
#     print('an error happened') # an error happened

#     # we can also print the exception:
# try:
#     a = 5 / 0
# except Exception as e: 
#     print(e) # division by zero

# we can use multiple except blocks to catch different exceptions
# try:
#     a = 5 / 1   
#     b = a + '10' # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# except ZeroDivisionError as e: 
#     print(e)    
# except TypeError as e:
#     print(e)    

# then:
# try:
#     a = 5 / 0 # ZeroDivisionError: division by zero
#     b = a + '10' # TypeError: unsupported operand type(s) for +: 'float' and 'str'
# except ZeroDivisionError as e: 
#     print(e) # ZeroDivisionError: division by zero
# except TypeError as e:
#     print(e) 

# we can also use else 
# try:
#     a = 5 / 1 
#     b = a + 4
# except ZeroDivisionError as e: 
#     print(e)
# except TypeError as e:
#     print(e) 
# else: # if there is no exception
#     print('everything is fine') # everything is fine
    
# we can also use else and finally:
# try:
#     a = 5 / 1 
#     b = a + 4
# except ZeroDivisionError as e: 
#     print(e)
# except TypeError as e:
#     print(e) 
# else: # if there is no exception
#     print('everything is fine')
# finally: # finally will always run
#     print('cleaning up...') # use this to clean up resources, like closing a file
    
# try:
#     a = 5 / 0 
#     b = a + 4
# except ZeroDivisionError as e: 
#     print(e) # division by zero
# except TypeError as e:
#     print(e) 
# else: # if there is no exception
#     print('everything is fine')
# finally: # finally will always run
#     print('cleaning up...') # cleaning up...
    
# # How to define your own exceptions:
# class ValueTooHighError(Exception): # we can inherit from Exception
#     pass

# # def test_value(x):
# #     if x > 100:
# #         raise ValueTooHighError('value is too high')
# # test_value(200) # __main__.ValueTooHighError: value is too high

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('value is too high')
# try:
#     test_value(200) # __main__.ValueTooHighError: value is too high
# except ValueTooHighError as e:
#     print(e) # value is too high

class ValueTooHighError(Exception): # we can inherit from Exception
    pass  

class ValueTooSmallError(Exception): 
    def __init__(self, message, value): # we can define custom init method
        self.message = message # we can store the message
        self.value = value
# and now inside our test_value function, we can raise our custom exception
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e) 
except ValueTooSmallError as e:
    print(e.message, e.value)
