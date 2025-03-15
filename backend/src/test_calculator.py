import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 2), 4)
        self.assertEqual(self.calculator.multiplication(2, -2), -4)
        self.assertEqual(self.calculator.multiplication(2, -2.0), -4.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(2, -2), 4)
        self.assertEqual(self.calculator.subtraction(2, -2.0), 4.0)

    def test_division(self):
        self.assertEqual(self.calculator.division(2, 2), 1.0)
        self.assertEqual(self.calculator.division(2, 0), None)
        self.assertEqual(self.calculator.division(2, -2.0), -1.0)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-2), 2)
        self.assertEqual(self.calculator.absolute(-2.0), 2.0)
        self.assertEqual(self.calculator.absolute(2), 2)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 2), 4)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(2, -2.0), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1.0)
        self.assertEqual(self.calculator.ln(1), 0.0)

    def test_log(self):
        self.assertEqual(self.calculator.log(10, 10), 1.0)
        self.assertEqual(self.calculator.log(1, 10), 0.0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2.0)
        self.assertEqual(self.calculator.sqrt(0), 0.0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2.0)
        self.assertEqual(self.calculator.nth_root(8, 3), 2.0)


if __name__ == "__main__":
    unittest.main()
