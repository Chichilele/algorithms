from numpy import sign

from .general_method import Method


class Bisection(Method,):
    """Bisection method class for bisection algorithm (https://en.wikipedia.org/wiki/Bisection_method).

    Attributes:
        f (function): function to search root against
        tol (float): tolerance
        max_iter (int): maximum number of iteration
    """

    def __init__(self, f, tol=1e-2, max_iter=1000):
        Method.__init__(self, f=f, tol=tol, max_iter=max_iter)

    def solve(
        self, a, b,
    ):

        """run the Bisection root-finding method starting between points a and b. 
        Stops if tolerance is matched or raise error if max interation reached.

        Args:
            a (float): first interval boundary
            b (float): second interval boundary

        Returns:
            float: computed root within interval.
        """

        self.epochs = []
        if 0 == self.f(a):
            return a
        elif 0 == self.f(b):
            return b

        if sign(self.f(a)) == sign(self.f(b)):
            raise ValueError(
                f"Same sign. f(a): {sign(self.f(a))},\tf(b): {sign(self.f(b))}"
            )

        for _ in range(self.max_iter):
            c = (a + b) / 2
            self.epochs.append(c)
            if (0 == self.f(c)) or ((b - a) / 2 < self.tol):  # solution found
                return c

            if sign(self.f(c)) == sign(self.f(a)):  # new interval
                a = c
            else:
                b = c
        raise Exception(
            "Convergence error. Reached maximum number of iterations without finding a stable enough solution"
        )

    def __repr__(self):
        return super().__repr__()


if __name__ == "__main__":
    print(Bisection(lambda x: x * x, 1e-1, 100))

