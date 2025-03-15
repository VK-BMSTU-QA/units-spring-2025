import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(1.5, 2.5), 4.0)
        self.assertEqual(self.calculator.addition(-1.5, -2.5), -4.0)
        self.assertEqual(self.calculator.addition(1.5, -2.5), -1.0)
        with self.assertRaises(TypeError):
            self.calculator.addition("а", 2)
        with self.assertRaises(TypeError):
            self.calculator.addition(None, 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)
        self.assertEqual(self.calculator.multiplication(2.5, 4), 10.0)
        self.assertEqual(self.calculator.multiplication(-2.5, -4), 10.0)
        self.assertEqual(self.calculator.multiplication(2.5, -4), -10.0)
        self.assertEqual(self.calculator.multiplication("3", 2), "33")
        self.assertEqual(self.calculator.multiplication([2], 3), [2, 2, 2])

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(3, 5), -2)
        self.assertEqual(self.calculator.subtraction(2.5, 1.5), 1.0)
        self.assertEqual(self.calculator.subtraction(-2.5, -1.5), -1.0)
        self.assertEqual(self.calculator.subtraction(2.5, -1.5), 4.0)
        with self.assertRaises(TypeError):
            self.calculator.subtraction("5", 3)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(7, 2), 3.5)
        self.assertEqual(self.calculator.division(-9, 3), -3)
        self.assertEqual(self.calculator.division(0, 5), 0)
        self.assertEqual(self.calculator.division(-7.5, 2.5), -3.0)
        self.assertEqual(self.calculator.division(7.5, -2.5), -3.0)
        self.assertIsNone(self.calculator.division(5, 0))
        with self.assertRaises(TypeError):
            self.calculator.division("6", 3)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertEqual(self.calculator.absolute(-5.7), 5.7)
        self.assertEqual(self.calculator.absolute(5.7), 5.7)
        with self.assertRaises(TypeError):
            self.calculator.absolute("-5")

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertEqual(self.calculator.degree(-4.2, 2), 17.64)
        self.assertEqual(self.calculator.degree(4.2, -2), 1 / 17.64)
        with self.assertRaises(TypeError):
            self.calculator.degree("2", 3)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertEqual(self.calculator.log(100, 10), 2)
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(-9), 1.8369701987210297e-16+3j)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
        self.assertEqual(self.calculator.nth_root(2, 2), math.sqrt(2))
        self.assertEqual(self.calculator.nth_root(8.0, 3), 2.0)
        # self.assertEqual(self.calculator.nth_root(-8.0, 3), -2.0)
        self.assertEqual(self.calculator.nth_root(-8.0, 2), 1.7319121124709868e-16+2.8284271247461903j)

        with self.assertRaises(TypeError):
            self.calculator.nth_root("27", 3)
        with self.assertRaises(TypeError):
            self.calculator.nth_root(27, "3")

if __name__ == "__main__":
    unittest.main()
