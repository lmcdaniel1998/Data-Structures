import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr_0(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")
    
    def test_repr_1(self):
        loc = Location("LA", -90.0, -115.0)
        self.assertEqual(repr(loc), "Location('LA', -90.0, -115.0)")

    def test_repr_2(self):
        loc = Location("MA", -25.0, 36.3)
        self.assertEqual(repr(loc), "Location('MA', -25.0, 36.3)")

    def test_repr_3(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(repr(loc), "Location('CO', 35.3, -120.7)")

    def test_eq_0(self):
        loc_0 = Location("WA", 45.0, 60.0)
        loc_1 = Location("WA", 45.0, 60.0)
        self.assertEqual(loc_0, loc_1)

    def test_eq_1(self):
        loc_0 = Location("VA", -200.0, -33.2)
        loc_1 = Location("VA", -199.0, -33.2)
        self.assertNotEqual(loc_0, loc_1)

    def test_eq_2(self):
        loc_0 = Location("OH", 45.0, 60.0)
        loc_1 = Location("oH", 0.0, 0.0)
        self.assertNotEqual(loc_0, loc_1)


if __name__ == "__main__":
        unittest.main()
