import numpy as np

from .general_method import Method


class Bisection(Method,):
    """Bisection method class for bisection algorithm (https://en.wikipedia.org/wiki/Bisection_method).

    Attributes:
        f (function): function to search root against
    """

    def __init__(self, f=None):
        Method.__init__(self)
        self.f = f

    def solve(self, a, b, tol=10e-3, max_iter=100):

        """
        """

        if self.f(a) == 0:
            return a
        elif self.f(b) == 0:
            return b

        if np.sign(self.f(a)) == np.sign(self.f(b)):
            raise ValueError(
                f"Same sign. f(a): {np.sign(self.f(a))},\tf(b): {np.sign(self.f(b))}"
            )

        for n in range(max_iter):
            c = (a + b) / 2
            if (0 == self.f(c)) or ((b - a) / 2 < tol):  # solution found
                return c

            if np.sign(self.f(c)) == np.sign(self.f(a)):  # new interval
                a = c
            else:
                b = c
        
        raise Exception("Reached maximum number of iterations without finding a solution")

