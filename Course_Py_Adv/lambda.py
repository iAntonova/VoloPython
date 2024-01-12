# lambda arguments: expression -
# lambda function - anonymous function, function without a name, one-line function

add10 = lambda x: x + 10
add10(5) # 15

def add10_func(x):
    return x + 10

# there is no difference between lambda function and regular function
# except lambda function is anonymous
# lambda function is not bound to any name
# lambda function is much shorter than regular function and in one line
# lambda function is not a statement, it is an expression
# lambda function can be used inside other functions

# lambda function can have multiple arguments
mult = lambda x, y: x * y
print(mult(2, 7)) # 14  

# lambda function used when we need a simple function that we will use only once
# or it is used as an argument to higher-order functions (functions that take other functions as arguments)


