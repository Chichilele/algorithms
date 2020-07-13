class Method:
    def __init__(self, f):

        """ Generic method class for calculating and 
		visualizing a root-finding algorithm.
	
		Attributes:
	        f (function): function to search root against
		"""
        self.f = f
        self.epochs = None

    def plot_epochs(self):

        """ plot the epochs from solve.
        """

        import matplotlib.pyplot as plt

        plt.scatter(self.epochs, self.f(self.epochs), c=range(len(self.epochs)))
        plt.ylabel("Epochs")
        plt.show()

    def example(self,):

        """Description. Input description. Function description.
				
		Args:
			arg1 (type): description
		
		Returns:
			type: description
		
		"""

        pass
