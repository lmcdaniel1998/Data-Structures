import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")

    def test_base3(self):
        self.assertEqual(convert(16, 3), "121")

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")

    def test_base5(self):
        self.assertEqual(convert(111, 5), "421")

    def test_base6(self):
        self.assertEqual(convert(3, 6), "3")

    def test_base7(self):
        self.assertEqual(convert(42, 7), "60")

    def test_base8(self):
        self.assertEqual(convert(234, 8), "352")

    def test_base9(self):
        self.assertEqual(convert(95, 9), "115")

    def test_base10(self):
        self.assertEqual(convert(67, 10), "67")

    def test_base11(self):
        self.assertEqual(convert(1156, 11), "961")

    def test_base12(self):
        self.assertEqual(convert(23, 12), "1B")

    def test_base13(self):
        self.assertEqual(convert(13, 13), "10")

    def test_base14(self):
        self.assertEqual(convert(23451, 14), "8791")

    def test_base15(self):
        self.assertEqual(convert(23, 15), "18")

    def test_base16(self):
        self.assertEqual(convert(316, 16), "13C")


if __name__ == "__main__":
        unittest.main()
