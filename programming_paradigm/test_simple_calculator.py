#!/usr/bin/env python3
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(-1.1, -2.2), -3.3, places=7)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 1), -1)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertAlmostEqual(self.calc.divide(7, 3), 7/3, places=7)

if __name__ == "__main__":
    unittest.main()

