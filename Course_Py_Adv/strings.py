# Strings: ordered, immutable, text representation
from timeit import default_timer as timer





""" Strings formatting: start"""
# %, .format(), f-Strings

# % - old way of formatting strings
var = "Tom"
my_string = "the variable is %s" % var
print(my_string) # the variable is Tom - %s - string

var = 3
my_string = "the variable is %d" % var
print(my_string)  # the variable is 3 - %d - integer

var = 3.142435345
my_string = "the variable is %d" % var
print(my_string) # the variable is 3 - %d - integer
# %d - integer, %f - float, %s - string

var = 3.142435345
my_string = "the variable is %f" % var
print(my_string)   # the variable is 3.142435 - %f - float - 6 digits after the decimal point

var = 3.142435345
my_string = "the variable is %.2f" % var
print(my_string)    # the variable is 3.14 - %.2f - float - 2 digits after the decimal point
# this is an old way of formatting strings

# .format() - old way of formatting strings
var = 3.142435345
my_string = "the variable is {}".format(var)
print(my_string) # the variable is 3.142435345 - {} - float - 6 digits after the decimal point

var = 3.142435345
my_string = "the variable is {:.2f}".format(var)
print(my_string) # the variable is 3.14 - {:.2f} - float - 2 digits after the decimal point

var = 3.142435345
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string) # the variable is 3.14 and 6 
# this one is also an old way of formatting strings

print("!!!!!   Check current text here: !!!!!!!!!!!!!")
# f-Strings - new way of formatting strings
var = 3.142435345
var2 = 6
my_string = f"the variable is {var} and {var2}"
print(my_string) # the variable is 3.142435345 and 6


var = 3.142435345
var2 = 6
my_string = f"the variable is {var*2} and {var2}"
print(my_string) # the variable is 6.28487069 and 6

""" Strings formatting ^^^ end"""
# ---------------------------------------------
""" Strings join: start"""

my_list = ['a'] * 6
print(my_list) # ['a', 'a', 'a', 'a', 'a', 'a'] - list of 6 elements 'a'
# but, this bad python code: 
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start)
print(my_string) # aaaaaa - concatenate all elements in the list into a string
# better python code:
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
print(my_string) # aaaaaa - concatenate all elements in the list into a string
# same but much cleaner and faster code



my_list = ['a'] * 1000000

# but, this bad python code: 
start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop - start) # 8.20753904099547

# better python code:
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start) # 0.003577916999347508

""" Strings join ^^^ end"""
# ---------------------------------------------
""" Strings iteration: end"""

my_string = 'how,are,you,doing'
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)  # how are you doing - join by space ' '
print(new_string)


my_string = 'how,are,you,doing'
my_list = my_string.split(",")  # ['how', 'are', 'you', 'doing'] - split by comma ','
print(my_list)


my_string = 'how,are,you,doing'
my_list = my_string.split() # ['how,are,you,doing']
print(my_list) # there is no space in the string, so the whole string is one element in the list

my_string = 'how are you doing'
my_list = my_string.split() # ['how', 'are', 'you', 'doing']
print(my_list) # and default separator is space ' ' - split by each space

my_string = "Hello World"
print(my_string.replace("Worrrld", "Universe")) # Hello World - does NOT replace Worrrld with Universe
# because there is no Worrrld in Hello World

my_string = "Hello World"
print(my_string.replace("World", "Universe")) # Hello Universe - replace World with Universe
# and the result is a new string, because strings are immutable

my_string = "Hello World"
print(my_string.count("o")) # 2 - count the number of occurrences of the letter 'o'

my_string = "Hello World"
print(my_string.find("rr")) # -1 - substring 'rr' is not in 'Hello World'


my_string = "Hello World"
print(my_string.find("lo")) # 3 - index of the first occurrence of the substring 'lo'


my_string = "Hello World"
print(my_string.find("o")) # 4 - index of the first occurrence of the letter 'o'


my_string = "Hello World"
print(my_string.endswith("World")) # True - ends with World


my_string = "Hello World"
print(my_string.startswith("World")) # False - does not start with World


my_string = "Hello World"
print(my_string.startswith("Hello")) # True - starts with Hello


my_string = "Hello World"
print(my_string.startswith("H")) # True - starts with H


my_string = "Hello World"
print(my_string.lower()) # hello world - lower case


my_string = "Hello World"
print(my_string.upper()) # HELLO WORLD - upper case


my_string = "    Hello World    "
my_string.strip() # Hello World - does not remove spaces at the beginning and at the end
                  # because strip() returns a new string, it does not change the original one
print(my_string)


my_string = "    Hello World    "
my_string = my_string.strip() # Hello World - remove spaces at the beginning and at the end
                              # we assign the new string to the variable my_string
print(my_string)


my_string = "    Hello World    "
print(my_string) #     Hello World  - spaces at the beginning and at the end


greeting = "Hello"
if 'ell' in greeting:
    print('yes') # yes - substring 'ell' is in 'Hello'
else:
    print('no')


greeting = "Hello"
if 'e' in greeting:
    print('yes') # yes - 'e' is in 'Hello'
else:
    print('no')


greeting = "Hello"
for i in greeting:
    print(i) # H e l l o - each letter in new line


greeting = "Hello World"
name = "John"
sentence = greeting + " " + name
print(sentence) # Hello World John - concatenation

""" Strings iteration ^^^ start"""
# ---------------------------------------------
""" Strings: end """

my_string = "Hello World"
substring = my_string[::-1] # dlroW olleH - reverse string
print(substring)

my_string = "Hello World"
substring = my_string[::2]  # HloWrd - every second element
print(substring)

my_string = "Hello World"
substring = my_string[:] # Hello World - copy of the string
print(substring)

my_string = "Hello World"
substring = my_string[:6] # Hello - from 0 to 6
print(substring)

my_string = "Hello World"
substring = my_string[1:6] # ello - from 1 to 6
print(substring)

my_string = "Hello World"
# my_string[0] = 'h' # TypeError: 'str' object does not support item assignment
print(my_string)

my_string = "Hello World"
char = my_string[-1] # d - last element
print(char)

my_string = "Hello World"
char = my_string[0] # H - first element
print(char) # H

my_string = """Hello \
World"""    # \ - for multyline strings or comments in one line
print(my_string)   

my_string = """Hello 
World""" # triple quotes - for multyline strings or comments
print(my_string)   
# Hello 
# World

my_string = "I\'m programmer"
print(my_string) # I'm programmer

my_string = 'I\'m programmer' 
print(my_string) # I'm programmer

my_string = "Hello World" # double quotes
print(my_string) # Hello World

my_string = 'Hello World' # single quotes - more common
print(my_string) # Hello World

""" Strings: ^^^ start """
# ---------------------------------------------