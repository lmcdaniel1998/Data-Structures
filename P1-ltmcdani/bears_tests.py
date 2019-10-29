import unittest
from bears import *


class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_0(self):
        self.assertFalse(bears(16))

    def test_bear_1(self):
        self.assertFalse(bears(251))

    def test_bear_2(self):
        self.assertTrue(bears(168))


if __name__ == "__main__":
    unittest.main()
