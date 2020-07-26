import numpy as np

from .general_method import Method


class Newton(Method):
    """Newton class for Newton-Raphson root-finding method.
    """

    def __init__(self, f, fprim, x0, tol=1e-2, max_iter=1000):
        Method.__init__(self, f=f, tol=tol, max_iter=max_iter)

        self.fprim = fprim
        self.x0 = x0

    def solve(self):
        """Run the Newton-Raphson root-finding method starting with points x0 and x1. 
        Stops if tolerance is matched or raise error if max iteration reached.

        Returns:
            float: computed root within interval.
        """

        ## init
        self.epochs = [self.x0]

        ## lucky initial guess
        if 0 == self.f(self.epochs[-1]):
            return self.epochs[-1]

        ## loop until max iter
        for _ in range(self.max_iter):
            self.epochs.append(
                self.epochs[-1] - self.f(self.epochs[-1]) / self.fprim(self.epochs[-1])
            )

            convergence = np.abs(self.f(self.epochs[-2]) - self.f(self.epochs[-1]))
            if self.tol >= convergence:
                return self.epochs[-1]

        raise Exception(
            "Convergence error. Reached maximum number of iterations without finding a stable enough solution"
        )

    def __repr__(self):
        return super().__repr__()
