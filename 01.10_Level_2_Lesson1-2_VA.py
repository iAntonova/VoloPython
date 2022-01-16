# Given functions that calculate the median and average of the given list.
# Create a decorator that:
# * checks input values and asserts if it is empty
# * keeps count of calls for each wrapped function  in some global
# structure (function.__name__ can be used – see example in the lesson).

count_median_times = 0
count_average_times = 0
my_list = [2, 3, 9, 8, 1, 0, 7, 15]


def count_func(func):
    def wrapper(*args, **kw):
        if args is False:
            raise AssertionError("Empty!")
        result = func(*args, **kw)
        func_name = func.__name__
        if func_name in "list_median":
            global count_median_times
            count_median_times += 1
            print(f"Function {func_name} was called {count_median_times} times")

        if func_name in "list_average":
            global count_average_times
            count_average_times += 1
            print(f"Function {func_name} was called {count_average_times} times")
        return result
    return wrapper

@count_func
def list_median(name_list):
    median_list = name_list.copy()
    median_list.sort()
    position = int(len(median_list) / 2)
    if len(median_list) % 2 == 0:
        median = (median_list[position - 1] + median_list[position]) / 2
    else:
        median = median_list[position]
    return median

@count_func
def list_average(name_list):
    try:
        average = sum(name_list) / len(name_list)
        return average
    except:
        print("List can consist only from numbers")


if __name__ == "__main__":
    print(list_median(my_list))
    print(list_average(my_list))
