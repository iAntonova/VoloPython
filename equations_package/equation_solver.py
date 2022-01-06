# Use terminal: py 'equation_solver.py' -a 4 -b 6 -c 0

import sys
import argparse

from equations_dir.quadratic_base import QuadraticEquation

if __name__ == "__main__":

    try:

        parser = argparse.ArgumentParser(prog=sys.argv[0],
                                         description="Solver for quadratic equations")
        parser.add_argument("-a", "--coeff_a", help="Coefficient A", dest="a", type=float, required=True)
        parser.add_argument("-b", "--coeff_b", help="Coefficient B", dest="b", type=float, default=0)
        parser.add_argument("-c", "--coeff_c", help="Coefficient C", dest="c", type=float, default=0)

        args = parser.parse_args()
        if args.a == 0:
            raise argparse.ArgumentError("-a must not be 0")
        equation = QuadraticEquation(args.a, args.b, args.c)
        print("Equation: ", equation)
        print("Real roots for the equation: ", equation.solve())

    except (argparse.ArgumentError, argparse.ArgumentTypeError) as x:
        sys.stderr.write(str(x) + "\n")
        sys.exit(1)
    else:
        sys.exit(0)