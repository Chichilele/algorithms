# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from algorithms import Newton


class TestNewtonClass(unittest.TestCase):
    def setUp(self):
        self.newton = Newton()

    # def test_initialization(self):
    #     self.assertEqual(self.newton.p, 0.4, "p value incorrect")
    #     self.assertEqual(self.newton.n, 20, "n value incorrect")


if __name__ == "__main__":
    unittest.main()
