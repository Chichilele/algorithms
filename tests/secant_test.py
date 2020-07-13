# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from algorithms import Secant


class TestSecantClass(unittest.TestCase):
    def setUp(self):
        self.secant = Secant()

    # def test_initialization(self):
    #     self.assertEqual(self.secant.p, 0.4, "p value incorrect")
    #     self.assertEqual(self.secant.n, 20, "n value incorrect")


if __name__ == "__main__":
    unittest.main()
