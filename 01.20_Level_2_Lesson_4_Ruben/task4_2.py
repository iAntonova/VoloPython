import sys
import csv
import timeit
import argparse

last_call_duration = None


def timed_function(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        global last_call_duration
        last_call_duration = timeit.default_timer() - start_time
        return result
    return wrapper


@timed_function
def factorial_r(num: int) -> int:
    """
    Calculate factorial of num (recursive)
    :param num: number to calculate factorial for
    :return: factorial value
    """

    if num <= 1:
        return 1
    else:
        return num * factorial_r(num - 1)


@timed_function
def factorial_n(num: int) -> int:
    """
    Calculate factorial of num (non-recursive)
    :param num: number to calculate factorial for
    :return: factorial value
    """

    if num == 0:
        return 1
    else:
        fct = 1
        for i in range(1, num + 1):
            fct *= i
        return fct


def natural(in_value: str) -> int:
    try:
        val = int(in_value)
    except (TypeError, ValueError) as x:
        raise argparse.ArgumentTypeError(str(x))

    if val <= 0:
        raise argparse.ArgumentTypeError("value must be >= 0 ")

    return val


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("-n", "--start", type=natural,
                        default=1, help="Start number")
    parser.add_argument("-m", "--end", type=natural,
                        required=True, help="End number")
    parser.add_argument("-o", "--out", type=str,
                        default="out.csv", help="Output CSV")

    try:

        args = parser.parse_args()

        if args.end <= args.start:
            raise argparse.ArgumentTypeError(
                "-m value must be greater than -n value")

        out_data = []
        for i in range(args.start, args.end + 1):
            record = {'num': i}
            factorial_n(i)
            record['non-rec'] = last_call_duration
            factorial_r(i)
            record['rec'] = last_call_duration
            out_data.append(record)

        with open(args.out, "w") as fp:
            writer = csv.DictWriter(fp, dialect=csv.excel,
                                    fieldnames=['num', 'rec', 'non-rec'])

            writer.writeheader()
            writer.writerows(out_data)

    except Exception as x:
        sys.stderr.write(str(x))
        sys.exit(-1)

    sys.exit(0)
