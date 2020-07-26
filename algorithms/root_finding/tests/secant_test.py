import unittest

from algorithms.root_finding import Secant


class TestSecantClass(unittest.TestCase):
    def setUp(self):
        f = lambda x: x ** 3 - x + 13
        x0 = -1
        x1 = 10

        self.secant = Secant(f, x0, x1)

    def test_initialization(self):
        self.assertEqual(self.secant.f(-3), -11, "incorrect f init")
        self.assertEqual(self.secant.x0, -1, "incorrect x0 init")
        self.assertEqual(self.secant.x1, 10, "incorrect x0 init")
        self.assertEqual(self.secant.tol, 1e-2, "incorrect tol init")
        self.assertEqual(self.secant.max_iter, 1000, "incorrect max_iter init")
        self.assertEqual(
            self.secant.__repr__(),
            "Secant: tolerance(0.01)\tmax iter(1000)",
            "incorrect repr init",
        )

    def test_solve(self):
        self.assertLessEqual(self.secant.solve(), 10e-1)
        self.secant.max_iter = 1
        with self.assertRaises(Exception):
            self.secant.solve()


if __name__ == "__main__":
    unittest.main()
