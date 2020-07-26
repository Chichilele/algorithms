import unittest

from algorithms.root_finding import Bisection


class TestBisectionClass(unittest.TestCase):
    def setUp(self):
        f = lambda x: x
        self.bisection = Bisection(f, -1, 0.5)

    def test_initialization(self):
        self.assertEqual(self.bisection.f(0), 0, "incorrect function")
        self.assertEqual(self.bisection.a, -1, "incorrect a init")
        self.assertEqual(self.bisection.b, 0.5, "incorrect b init")
        self.assertEqual(self.bisection.tol, 1e-2, "incorrect tol init")
        self.assertEqual(self.bisection.max_iter, 1000, "incorrect max_iter init")
        self.assertEqual(
            self.bisection.__repr__(),
            "Bisection: tolerance(0.01)\tmax iter(1000)",
            "incorrect repr init",
        )

    def test_solve(self):
        self.bisection.a = -1
        self.bisection.b = 1
        self.assertEqual(self.bisection.solve(), 0, "incorrect exact solution")

        self.bisection.a = -1
        self.bisection.b = 0.5
        self.assertEqual(
            self.bisection.solve(), 1 / (2 ** 9), "incorrect approx solution"
        )
        with self.assertRaises(ValueError):
            self.bisection.a = 5
            self.bisection.b = 5
            self.bisection.solve()
        with self.assertRaises(Exception):
            self.bisection.a = 1.0001
            self.bisection.b = 2.99
            self.bisection.max_iter=1
            self.bisection.solve()


if __name__ == "__main__":
    unittest.main()
