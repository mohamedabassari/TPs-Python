from exercice1 import safe_division
from exercice2 import convert_to_int
from exercice4 import NegativeAgeError, set_age


import unittest

class TestExceptions(unittest.TestCase):
    def test_safe_division(self):
        self.assertEqual(safe_division(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            safe_division(10, 0)
    
    def test_convert_to_int(self):
        self.assertEqual(convert_to_int("42"), 42)
        with self.assertRaises(ValueError):
            convert_to_int("ABC")

    def test_set_age(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-1)

if __name__ == "__main__":
    unittest.main()