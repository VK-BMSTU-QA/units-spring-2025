import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(5, 3), 8)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 3), 9)
        self.assertEqual(self.calculator.multiplication(3, -3), -9)
        self.assertEqual(self.calculator.multiplication(3, -3.0), -9.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(5, -3), 8)
        self.assertEqual(self.calculator.subtraction(5, -3.0), 8.0)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2.0)
        self.assertEqual(self.calculator.division(6, 0), None)
        self.assertEqual(self.calculator.division(6, -3.0), -2.0)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(-5.0), 5.0)
        self.assertEqual(self.calculator.absolute(5), 5)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 2), 9)
        self.assertEqual(self.calculator.degree(3, 0), 1)
        self.assertEqual(self.calculator.degree(2, -2.0), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1.0)
        self.assertEqual(self.calculator.ln(1), 0.0)

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2.0)
        self.assertEqual(self.calculator.log(1, 10), 0.0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4.0)
        self.assertEqual(self.calculator.sqrt(0), 0.0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2.0)
        self.assertEqual(self.calculator.nth_root(27, 3), 3.0)


if __name__ == "__main__":
    unittest.main()
