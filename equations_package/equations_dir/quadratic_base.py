# Create a package for the quadratic equation solver class (reuse the class created in task 12.1).
# Re-write the program created for task 12.1 to use the newly created package.
#
# Check the PEP-8 conformance of the program code using pycodestyle.
# Learn yourself how to configure pycodestyle to increase line length from 80 to 90 characters.
# Disable line length checking for all  print() calls in program.
# Hint: the first setting requires configuration file, the second one should be done in code.
# Send ZIP or tar.gz file with package, program file, pycodestyle config file.
# Do not include any venv stuff there.

from math import sqrt


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