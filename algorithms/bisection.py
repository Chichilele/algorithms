from numpy import sign

from .general_method import Method


class Bisection(Method,):
    """Bisection method class for bisection algorithm (https://en.wikipedia.org/wiki/Bisection_method).

    Attributes:
        f (function): function to search root against
    """

    def __init__(self, f=None):
        Method.__init__(self)
        self.f = f
        self.epochs = None

    def solve(self, a, b, tol=10e-3, max_iter=100):

        """run the Bisection root-finding method starting between points a and b. 
        Stops if tolerance is matched or raise error if max interation reached.

        Args:
            a (float): first interval boundary
            b (float): second interval boundary
            tol (float): tolerance error on objective (c)
            max_iter (int): maximum number of iterations before interrupting the algorithm.

        Returns:
            float: compute root within interval.
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

        for n in range(max_iter):
            c = (a + b) / 2
            self.epochs.append(c)
            if (0 == self.f(c)) or ((b - a) / 2 < tol):  # solution found
                return c

            if sign(self.f(c)) == sign(self.f(a)):  # new interval
                a = c
            else:
                b = c
        
        raise Exception("Reached maximum number of iterations without finding a solution")

    def plot_epochs(self):

        """ plot the epochs from solve.
        """

        import matplotlib.pyplot as plt
        plt.scatter(self.epochs, self.f(self.epochs), c=range(len(self.epochs)))
        plt.ylabel('Epochs')
        plt.show()
