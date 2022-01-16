# Given a list of 10 names. Implement a generator, which generates N randomly selected names from the list.
# Use module random to select randomly from the list.
# Example:
# name_list = ["John", "Paul", "Ringo", "George","Mick", "Keith", "Bill", "Ronnie", "Charlie", "Brian"]
# Generator with the argument 3 may result the following sequence: "Mick","Bill","Ringo“
# Names may be declared as a global variable

import random

name_list = ["John", "Paul", "Ringo", "George", "Mick", "Keith", "Bill", "Ronnie", "Charlie", "Brian"]


def my_gen(people_list):
    name = 0
    while name < 3:
        yield random.choice(people_list)
        name += 1


if __name__ == "__main__":
    _result = my_gen(name_list)
    _count = 0
    while _count != 3:
        print(next(_result))
        _count += 1
