# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from algorithms.root_finding.general_method import Method


class TestMethodClass(unittest.TestCase):
    def setUp(self):
        f = lambda x: x
        self.method = Method(f, 1e-1, 100)

    def test_initialization(self):
        self.assertEqual(self.method.f(0), 0, "incorrect function init")
        self.assertEqual(self.method.tol, 1e-1, "incorrect tol init")
        self.assertEqual(self.method.max_iter, 100, "incorrect max_iter init")
        self.assertEqual(self.method.__repr__(), 'Method: tolerance(0.1)\tmax iter(100)', "incorrect repr init")

    def test_plot_epochs(self):
        self.assertEqual(self.method.plot_epochs(), "Nothing solved yet.")


if __name__ == "__main__":
    unittest.main()
