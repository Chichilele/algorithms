class Method:
    """ Generic method class for calculating and 
        visualizing a root-finding algorithm.

    Attributes:
        f (function): function to search root against
        tol (float): tolerance
        max_iter (int): maximum number of iteration
    """

    def __init__(self, f, tol, max_iter):
        self.f = f
        self.tol = tol
        self.max_iter = max_iter

        self.epochs = None

    def plot_epochs(self):

        """ plot the epochs from solve.
        """

        if None == self.epochs: return "Nothing solved yet."

        import matplotlib.pyplot as plt

        plt.scatter(self.epochs, self.f(self.epochs), c=range(len(self.epochs)))
        plt.ylabel("Epochs")
        plt.show()

    def __repr__(self):
        return f"{self.__class__.__name__}: tolerance({self.tol})\tmax iter({self.max_iter})"

    def example(self,):

        """Description. Input description. Function description.
				
		Args:
			arg1 (type): description
		
		Returns:
			type: description
		
		"""

        pass


if __name__ == "__main__":
    print(Method(lambda x: x * x, 1e-1, 100))

