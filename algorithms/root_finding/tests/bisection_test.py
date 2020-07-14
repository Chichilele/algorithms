# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from algorithms.root_finding import Bisection


class TestBisectionClass(unittest.TestCase):
    def setUp(self):
        f = lambda x: x
        self.bisection = Bisection(f)

    def test_initialization(self):
        self.assertEqual(self.bisection.f(0), 0, "incorrect function")

    def test_solve(self):
        with self.assertRaises(ValueError):
            self.bisection.solve(5, 5)
        with self.assertRaises(Exception):
            self.bisection.solve(1.0001, 2.99, max_iter=0)
        self.assertEqual(self.bisection.solve(-1, 1), 0, "incorrect exact solution")
        self.assertEqual(
            self.bisection.solve(-1, 0.5), 1 / (2 ** 9), "incorrect approx solution"
        )


if __name__ == "__main__":
    unittest.main()
