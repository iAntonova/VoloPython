CALL_STAT = {}


def safe_call(func):
    def wrapper(*args):
        assert args, "No empty lists are allowed"

        global CALL_STAT
        func_name = func.__name__

        if func_name in CALL_STAT:
            CALL_STAT[func_name] += 1
        else:
            CALL_STAT[func_name] = 1

        return func(*args)
    
    return wrapper

@safe_call
def median(*args):
    data = sorted(args)
    num_elems = len(data)
    middle = int(num_elems / 2)
    if num_elems % 2 == 0:
        return (data[middle - 1] + data[middle]) / 2
    else:
        return data[middle]

@safe_call
def average(*args):
    return sum(args) / len(args)


if __name__ == "__main__":
    print(average(1, 2, 3))
    print(median(1, 2, 3, 4))

    print(average(3, 5, 6))

    print(CALL_STAT)
