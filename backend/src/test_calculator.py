import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_strings(self):
        self.assertEqual(self.calculator.addition('abc', 'def'), 'abcdef')

    def test_add_different_types(self):
        self.assertRaises(TypeError, self.calculator.addition, 'abc', 1)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_strings(self):
        self.assertEqual(self.calculator.multiplication('a', 5), 'aaaaa')

    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 2), 5)

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-9), 9)
        self.assertEqual(self.calculator.absolute(9), 9)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)
    
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_less_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertRaises(ValueError, self.calculator.log, -1, 10)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 2, 0)


if __name__ == "__main__":
    unittest.main()
