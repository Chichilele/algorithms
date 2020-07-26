import numpy as np

from .general_method import Method


class Secant(Method):
    """Secant class for Secant root-finding method.
    """

    def __init__(self, f, x0, x1, tol=1e-2, max_iter=1000):
        Method.__init__(self, f=f, tol=tol, max_iter=max_iter)

        self.x0 = x0
        self.x1 = x1

    def solve(self,):
        """run the secant root-finding method starting with points x0 and x1. 
        Stops if tolerance is matched or raise error if max iteration reached.

        x_n = x_(n-1) - f(x_(n-1)) * [ x_(n-1) - x_(n-2) ] / [ f(x_(n-1)) - f(x_(n-2)) ] 

        Returns:
            float: computed root within interval.
        """

        ## init
        self.epochs = [self.x0, self.x1]

        ## lucky initial guess
        if 0 == self.f(self.epochs[-1]):
            return self.epochs[-1]
        if 0 == self.f(self.epochs[-2]):
            return self.epochs[-2]

        ## loop until max iter
        for _ in range(self.max_iter):
            dx = self.epochs[-1] - self.epochs[-2]
            df_x = self.f(self.epochs[-1]) - self.f(self.epochs[-2])
            self.epochs.append(self.epochs[-1] - self.f(self.epochs[-1]) * dx / df_x)

            convergence = np.abs(self.f(self.epochs[-2]) - self.f(self.epochs[-1]))
            if self.tol >= convergence:
                return self.epochs[-1]

        raise Exception(
            "Convergence error. Reached maximum number of iterations without finding a stable enough solution"
        )
