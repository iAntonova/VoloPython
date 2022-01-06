# Lesson 12 - 1
# Re-write the program to solve quadratic equations, so that coefficients
# are given from the command line: –a <coeff_a> -b <coeff_b> -c <coeff_c>.
# Provide necessary info for auto-generated help.
# Quadratic Equation must be created as a class.
# Discriminant must be declared as a static method.
# Provide __str__ to print the equation in a human- readable form.
# Use Terminal: py '12.20_Level 1_Lesson 12-1_AV.py' -a 4 -b 5 -c 8

import sys
from math import sqrt
import argparse


class QuadraticEquation:
    def __init__(self, coeff_a: float, coeff_b: float, coeff_c: float):
        """
        Class solving quadratic equation
        :param coeff_a:
        :param coeff_b:
        :param coeff_c:
        """
        self._a = coeff_a
        self._b = coeff_b
        self._c = coeff_c

    @staticmethod
    def discriminant(a: float, b: float, c: float) -> float:
        """
        Calculate discriminant for a, b, c coefficients
        :param a:
        :param b:
        :param c:
        :return:
        """

        return b ** 2 - 4 * a * c

    def solve(self) -> tuple:
        """
        Solve equation and return roots
        :return: tuple with (x1, x2), or (x), or () when no solutions
        """

        dt = QuadraticEquation.discriminant(self._a, self._b, self._c)
        if dt < 0:
            return ()
        elif dt == 0:
            return (self._b / (2 * self._a))
        else:
            x1 = (-self._b - sqrt(dt)) / (2 * self._a)
            x2 = (-self._b + sqrt(dt)) / (2 * self._a)
            return x1, x2

    def __str__(self):
        eq_str = f"{self._a}*X^2"
        if self._b != 0:
            sign = "+" if self._b > 0 else "-"
            eq_str += f" {sign} {abs(self._b)}*X"
        if self._c != 0:
            sign = "+" if self._c > 0 else "-"
            eq_str += f" {sign} {abs(self._c)}"
        eq_str += " = 0"
        return eq_str


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