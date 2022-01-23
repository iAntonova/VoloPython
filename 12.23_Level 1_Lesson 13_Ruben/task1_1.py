from random import randint

NAME_LIST = [
"John", "Paul", "Ringo", "George",
"Mick", "Keith", "Bill", "Ronnie", "Charlie", "Brian"
]

def name_gen(count: int) -> str:
    for i in range(count):
        yield NAME_LIST[randint(0, len(NAME_LIST) - 1]


if __name__ == "__main__":
    for rnd_name in name_gen(4):
        print(rnd_name)
