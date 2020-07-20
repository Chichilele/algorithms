# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from algorithms.root_finding import Newton


class TestNewtonClass(unittest.TestCase):
    def setUp(self):
        f = lambda x: x ** 2
        fprim = lambda x: 2 * x
        x0 = -1

        self.newton = Newton(f, fprim, x0)

    def test_initialization(self):
        self.assertEqual(self.newton.f(2), 4, "incorrect f init")
        self.assertEqual(self.newton.fprim(3), 6, "incorrect fprim init")
        self.assertEqual(self.newton.tol, 1e-2, "incorrect tol init")
        self.assertEqual(self.newton.max_iter, 1000, "incorrect max_iter init")
        self.assertEqual(
            self.newton.__repr__(),
            "Newton: tolerance(0.01)\tmax iter(1000)",
            "incorrect repr init",
        )

    def test_solve(self):
        self.assertLessEqual(self.newton.solve(), 10 - 1)
        self.newton.max_iter = 1
        with self.assertRaises(Exception):
            self.newton.solve()


if __name__ == "__main__":
    unittest.main()
